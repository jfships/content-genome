// YouTube thumbnails (1280x720) from a still of the speaker + brand.
// usage: NODE_PATH=motion/node_modules node thumbs.js motion/thumbs.json
// thumbs.json:
// { "frame":"work/thumb_frame.png",            // pick a still where the speaker looks good (mouth closed or smiling)
//   "photo":{"height":900,"left":-50,"top":-60}, // place/zoom the still so the face sits in the right half
//   "brand":"brand/brand.json", "out":"out/thumbs",
//   "options":[
//     {"name":"A-hook","layout":"headline","headline":"12 years<br>in kitchens.","accent":"Now I build software."},
//     {"name":"B-proof","layout":"card","headline":"It runs<br>without me.","items":["Cash close reconciled","Bookings synced"],"toggle":"Owner on site"},
//     {"name":"C-name","layout":"name","kicker":"Hi, I'm","name":"Sam","pills":["Product designer","Software engineer"],"note":"Native English"} ] }
// Paths are relative to thumbs.json. Headlines: 2-6 words, from the video's own words, no claims the video doesn't make.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{
 const specP=path.resolve(process.argv[2]);const base=path.dirname(specP);const S=JSON.parse(fs.readFileSync(specP));
 const rel=p=>path.resolve(base,p);const b64=p=>fs.readFileSync(p).toString('base64');
 const E=path.join(__dirname,'..','engine','fonts');
 let B={colors:{},fonts:{}};const bp=S.brand?rel(S.brand):null;if(bp&&fs.existsSync(bp))B=JSON.parse(fs.readFileSync(bp));
 const C=Object.assign({canvas:'#0F1117',surface:'#141824',inset:'#1E2433',line:'#2A3346',ink:'#F8FAFC',muted:'#94A3B8',accent:'#FF5A1F',ok:'#22C55E'},B.colors);
 const font=(role,fallback)=>{const f=B.fonts&&B.fonts[role];return f&&bp?path.resolve(path.dirname(bp),f):fallback;};
 const ff=(fam,p)=>p&&fs.existsSync(p)?`@font-face{font-family:${fam};src:url(data:font/woff2;base64,${b64(p)});font-weight:100 900}`:'';
 const css=ff('UI',font('ui',path.join(E,'Geist-Variable.woff2')))+ff('DISP',font('display',font('ui',path.join(E,'Geist-Variable.woff2'))))+ff('NUM',font('mono',path.join(E,'GeistMono-Medium.woff2')));
 const ph=S.photo||{height:900,left:-50,top:-60};const img=`data:image/${S.frame.endsWith('.png')?'png':'jpeg'};base64,${b64(rel(S.frame))}`;
 const ck=`<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="${C.canvas}" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>`;
 const shell=body=>`<!doctype html><html><head><meta charset="utf-8"><style>${css}
 *{margin:0;box-sizing:border-box}body{width:1280px;height:720px;overflow:hidden;background:${C.canvas};font-family:UI,sans-serif;color:${C.ink}}
 .ph img{position:absolute;height:${ph.height}px;left:${ph.left}px;top:${ph.top}px}
 .shade{position:absolute;inset:0;background:linear-gradient(90deg,${C.canvas} 0%,${C.canvas} 34%,${C.canvas}8C 52%,${C.canvas}00 70%)}
 .tx{position:absolute;left:64px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;max-width:640px}
 .h{font-family:DISP,UI;font-weight:700;letter-spacing:-.03em;line-height:.95}.acc{color:${C.accent}}
 .card{background:${C.surface};border-radius:20px;box-shadow:0 0 0 2px ${C.inset},0 30px 60px -20px rgba(0,0,0,.8);padding:26px 30px;width:500px}
 .r{display:flex;align-items:center;gap:16px;font-size:26px;font-weight:500;height:52px;white-space:nowrap}
 .ck{width:34px;height:34px;border-radius:50%;background:${C.ok};display:flex;align-items:center;justify-content:center}
 .pill{display:inline-flex;align-items:center;height:52px;padding:0 24px;border-radius:26px;background:${C.surface};box-shadow:inset 0 0 0 2px ${C.line};font-size:26px;font-weight:500;white-space:nowrap}
 </style></head><body><div class="ph"><img src="${img}"></div><div class="shade"></div>${body}</body></html>`;
 const L={
  headline:o=>`<div class="tx"><div class="h" style="font-size:${o.size||124}px">${o.headline}</div>${o.accent?`<div class="h acc" style="font-size:${o.accentSize||64}px;margin-top:26px;letter-spacing:-.02em">${o.accent}</div>`:''}</div>`,
  card:o=>`<div class="tx" style="gap:30px"><div class="h" style="font-size:${o.size||104}px">${o.headline}</div><div class="card">${(o.items||[]).map(i=>`<div class="r"><span class="ck">${ck}</span>${i}</div>`).join('')}${o.toggle?`<div style="height:2px;background:${C.inset};margin:12px 0"></div><div class="r" style="color:${C.muted}">${o.toggle}<span style="margin-left:auto;width:78px;height:42px;border-radius:21px;background:${C.line};position:relative"><i style="position:absolute;left:5px;top:5px;width:32px;height:32px;border-radius:50%;background:#fff"></i></span></div>`:''}</div></div>`,
  name:o=>`<div class="tx">${o.kicker?`<div style="font-size:26px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:${C.muted}">${o.kicker}</div>`:''}<div class="h" style="font-size:${o.size||150}px;margin-top:6px">${o.name}</div><div style="display:flex;flex-direction:column;gap:14px;margin-top:30px;align-items:flex-start">${(o.pills||[]).map((p,i,a)=>`<span class="pill" ${i===a.length-1?`style="background:${C.accent};box-shadow:none"`:''}>${p}</span>`).join('')}</div>${o.note?`<div style="margin-top:28px;font-size:24px;color:${C.muted};font-weight:500">${o.note}</div>`:''}</div>`,
 };
 const out=rel(S.out||'out/thumbs');fs.mkdirSync(out,{recursive:true});
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
 for(const o of S.options){const f=path.join(out,`thumb-${o.name}.png`);const tmp=path.join(out,`.t-${o.name}.html`);fs.writeFileSync(tmp,shell(L[o.layout](o)));
   await p.goto('file://'+tmp);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);await p.screenshot({path:f});fs.unlinkSync(tmp);console.log('wrote',f);}
 await b.close();
})();
