# Swipe-file pull. Reads saved links from the drop folder(s), downloads each public video, writes batch.json.
# Public videos only, NO login. One failure does not stop the rest. Moves nothing: links leave the drop folder at review.
# usage: powershell -ExecutionPolicy Bypass -File swipe_pull.ps1 -Drop "G:\My Drive\Saves" [-Drop "...second folder"] -Out "C:\...\_swipe"
param([string[]]$Drop, [string]$Out, [switch]$NoPause)
$ErrorActionPreference = "Continue"
if (-not $Drop -or -not $Out) { "usage: swipe_pull.ps1 -Drop <folder> [-Drop <folder>] -Out <work folder>"; exit 1 }
New-Item -ItemType Directory -Force -Path $Out | Out-Null
$log = Join-Path $Out "pull-log.txt"
"Pull: $(Get-Date)" | Out-File $log -Encoding utf8

$cands = @("$env:LOCALAPPDATA\Microsoft\WinGet\Links\yt-dlp.exe", "$env:USERPROFILE\Downloads\yt-dlp.exe", "$env:USERPROFILE\Desktop\yt-dlp.exe")
$cands += Get-ChildItem "$env:APPDATA\Python\Python*\Scripts\yt-dlp.exe", "$env:LOCALAPPDATA\Programs\Python\Python*\Scripts\yt-dlp.exe" -ErrorAction SilentlyContinue | ForEach-Object FullName
$ytdlp = $cands | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $ytdlp) { $c = Get-Command yt-dlp -ErrorAction SilentlyContinue; if ($c) { $ytdlp = $c.Source } }
if (-not $ytdlp) { "yt-dlp not found. Install it: winget install yt-dlp.yt-dlp" | Tee-Object -FilePath $log -Append; if (-not $NoPause) { Read-Host "Press Enter to close" }; exit 1 }

$items = @(); $seen = @{}
foreach ($d in $Drop) {
  if (-not (Test-Path $d)) { "Drop folder not found: $d" | Tee-Object -FilePath $log -Append; continue }
  foreach ($f in Get-ChildItem $d -File) {
    $text = (Get-Content -Raw -LiteralPath $f.FullName -ErrorAction SilentlyContinue)
    if (-not $text -or $text -notmatch 'https?://\S+') { continue }
    $url = ($Matches[0] -split '[?#]')[0].TrimEnd('/') + '/'   # strip tracking params
    if ($url -match 'instagram\.com/(?:[^/]+/)?(?:reel|reels|p)/([A-Za-z0-9_-]+)') { $id = $Matches[1]; $url = "https://www.instagram.com/reel/$id/" }
    else { $id = (($url.TrimEnd('/') -split '/')[-1] -replace '[^A-Za-z0-9_-]', ''); if (-not $id) { continue } }
    if ($seen[$id]) { $seen[$id].link_files += $f.FullName; continue }   # same Reel saved twice
    $item = [ordered]@{ id = $id; url = $url; link_files = @($f.FullName); status = "" }
    $seen[$id] = $item; $items += $item
  }
}
if (-not $items) { "No saved links found. Share a Reel to the drop folder, then run this again." | Tee-Object -FilePath $log -Append; if (-not $NoPause) { Read-Host "Press Enter to close" }; exit 0 }

$n = 0
foreach ($it in $items) {
  $n++
  $dir = Join-Path $Out $it.id
  $have = Get-ChildItem $dir -Filter "video.mp4" -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($have) { $it.status = "ok"; "[$n/$($items.Count)] $($it.id) already downloaded" | Tee-Object -FilePath $log -Append; continue }
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  & $ytdlp --no-playlist --no-progress --write-info-json --merge-output-format mp4 -o (Join-Path $dir "video.%(ext)s") $it.url *>> $log
  $got = Get-ChildItem $dir -Filter "video.mp4" -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($got) { $it.status = "ok"; "[$n/$($items.Count)] OK $($it.id) $([math]::Round($got.Length/1MB,1)) MB" | Tee-Object -FilePath $log -Append }
  else { $it.status = "failed"; "[$n/$($items.Count)] FAILED $($it.id) (private, deleted or rate-limited; the link stays in the drop folder)" | Tee-Object -FilePath $log -Append }
  Start-Sleep -Seconds 3   # be gentle: avoids rate limits
}

$json = ConvertTo-Json @($items | ForEach-Object { [pscustomobject]$_ }) -Depth 4
[IO.File]::WriteAllText((Join-Path $Out "batch.json"), $json, (New-Object Text.UTF8Encoding $false))
$ok = @($items | Where-Object { $_.status -eq "ok" }).Count
"DONE. $ok of $($items.Count) ready. Tell Claude: review my saves." | Tee-Object -FilePath $log -Append
if (-not $NoPause) { Read-Host "Press Enter to close" }
