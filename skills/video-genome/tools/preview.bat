@echo off
rem Live preview of {{VIDEO}}. Open the Studio link below; edits to the draft reload in about 5 seconds.
rem Made from video-genome tools/preview.bat: {{VERSION}} = the HyperFrames version written in this video's log.
cd /d "%~dp0hf"
call npx hyperframes@{{VERSION}} preview
echo.
echo The preview runs in the background. Press any key here when you are done watching to stop it.
pause >nul
call npx hyperframes@{{VERSION}} preview . --stop
