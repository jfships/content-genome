// Pull fonts and colours out of an HTML brand kit / design-system page (works on bundled pages that unpack with JS).
// usage: NODE_PATH=motion/node_modules node brand_from_html.js path/to/kit.html motion/brand
// writes: brand/fonts/<Family>-<weight>.woff2 (Latin subset only, duplicates skipped), brand/kit.png (full-page screenshot to look at),
//         brand/found.json {fonts:[{family,weight,file}], colors:[{hex,count}], text:"page text"}.
// Then YOU write brand/brand.json (see reference/brand.md) choosing ui/display/mono fonts and the colour roles.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');const crypto=require('crypto');
(async()=>{
 const [kit,out]=process.argv.slice(2); fs.mkdirSync(path.join(out,'fonts'),{recursive:true});
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:1000}});
 await p.goto('file://'+path.resolve(kit));await p.waitForTimeout(4000);await p.evaluate(()=>document.fonts.ready);
 await p.screenshot({path:path.join(out,'kit.png'),fullPage:true});
 const r=await p.evaluate(()=>{
   const faces=[];for(const s of document.styleSheets){let rules;try{rules=s.cssRules}catch(e){continue}
     for(const ru of rules){if(ru.type===5)faces.push(ru.cssText)}}
   const cnt={};const add=c=>{const m=c&&c.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/);if(!m||(m[4]!==undefined&&+m[4]<0.5))return;
     const h='#'+[m[1],m[2],m[3]].map(x=>(+x).toString(16).padStart(2,'0')).join('').toUpperCase();cnt[h]=(cnt[h]||0)+1;};
   for(const el of document.querySelectorAll('*')){const cs=getComputedStyle(el);add(cs.color);add(cs.backgroundColor);add(cs.borderTopColor);}
   const txt=document.body.innerText;(txt.match(/#[0-9A-Fa-f]{6}\b/g)||[]).forEach(h=>{h=h.toUpperCase();cnt[h]=(cnt[h]||0)+5;});
   return {faces,colors:Object.entries(cnt).sort((a,b)=>b[1]-a[1]).map(([hex,count])=>({hex,count})),text:txt.slice(0,20000)};
 });
 await b.close();
 const seen=new Set();const fonts=[];
 for(const c of r.faces){
   const fam=(c.match(/font-family:\s*"?([^";]+)"?/)||[])[1];const w=((c.match(/font-weight:\s*([^;]+)/)||[])[1]||'400').trim().replace(/\s+/g,'-');
   const ur=(c.match(/unicode-range:\s*([^;]+)/)||[])[1]||'';const m=c.match(/url\("?data:[^;]+;base64,([^")]+)/);
   if(!fam||!m) continue; if(ur&&!/U\+0-FF|U\+0000-00FF/i.test(ur)) continue; // keep the Latin subset only
   const buf=Buffer.from(m[1],'base64');const h=crypto.createHash('md5').update(buf).digest('hex');if(seen.has(h))continue;seen.add(h);
   const file=`fonts/${fam.replace(/[^A-Za-z0-9]/g,'')}-${w}.woff2`;fs.writeFileSync(path.join(out,file),buf);fonts.push({family:fam,weight:w,file});
 }
 fs.writeFileSync(path.join(out,'found.json'),JSON.stringify({fonts,colors:r.colors.slice(0,40),text:r.text},null,1));
 console.log('fonts:',fonts.map(f=>f.file).join(', ')||'none embedded (check the page for font names and get the files)');
 console.log('top colours:',r.colors.slice(0,12).map(c=>c.hex).join(' '));
})();
