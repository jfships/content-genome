// One video's edit, assembled from its picks. The picker page and the render both run this file,
// so what the creator picks on the page is exactly what renders.
//
//   browser: compose(spec, picks) -> composition HTML (the page inlines this file)
//   node:    node compose.js spec.json picks.json out/index.html
//
// spec  = build.py's output: {base, rows:[{id, default, options:[{id, css, html, js, hideCaptions}]}]}
// picks = {rowId: optionId}; a row with no pick uses its default.
// base  = the HyperFrames composition with three markers: /*@css*/ in its <style>,
//         <!--@html--> inside the root element, /*@js*/ before the timeline is registered.
(function (root) {
  function chosen(row, picks) {
    const id = picks && picks[row.id] != null ? picks[row.id] : row.default;
    return row.options.find(o => o.id === id) || row.options.find(o => o.id === row.default);
  }
  function compose(spec, picks) {
    let css = "", html = "", js = "";
    const hide = [];
    for (const row of spec.rows) {
      const o = chosen(row, picks);
      if (!o) continue;
      css += o.css || ""; html += o.html || ""; js += o.js || "";
      if (o.hideCaptions) hide.push(row.id);
    }
    // When a beat has on-screen text, that beat's captions are hidden: the two never show together.
    if (hide.length) css += hide.map(b => `[data-beat="${b}"]`).join(",") + "{visibility:hidden!important}";
    return spec.base.replace("/*@css*/", () => css).replace("<!--@html-->", () => html).replace("/*@js*/", () => js);
  }
  root.compose = compose;
  root.composeChosen = chosen;
  if (typeof module !== "undefined" && require.main === module) {
    const fs = require("fs");
    const [spec, picks, out] = process.argv.slice(2);
    if (!out) { console.error("usage: node compose.js spec.json picks.json out/index.html"); process.exit(1); }
    const s = JSON.parse(fs.readFileSync(spec, "utf8"));
    const p = JSON.parse(fs.readFileSync(picks, "utf8"));
    fs.writeFileSync(out, compose(s, p));
    for (const row of s.rows) console.log(`${row.name}: ${chosen(row, p).name}${p[row.id] == null ? " (default)" : ""}`);
  }
})(typeof module !== "undefined" ? module.exports : window);
