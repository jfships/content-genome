/* motion-kit engine: one shape that never cuts.
   Every style is a pure function of time inside seek(t). No CSS transitions, no timers. */
(function(){
const M = window.M = {};
const clamp = M.clamp = (x,a=0,b=1)=>Math.min(b,Math.max(a,x));
M.lerp = (a,b,u)=>a+(b-a)*u;
const eo = M.eo = x=>{x=clamp(x);return 1-Math.pow(1-x,3)};
const eio = M.eio = x=>{x=clamp(x);return x*x*x*(x*(6*x-15)+10)};

// closed-form spring step response 0 -> 1 (zero initial velocity)
const S = M.S = (tau,w,z)=>{
  if(tau<=0) return 0;
  if(!isFinite(w)) return 1;
  if(z<1){const wd=w*Math.sqrt(1-z*z);return 1-Math.exp(-z*w*tau)*(Math.cos(wd*tau)+z*w/wd*Math.sin(wd*tau));}
  return 1-Math.exp(-w*tau)*(1+w*tau);
};
M.MORPH=[15,0.84]; M.FAST=[27,0.86]; M.SLOW=[12.5,0.9]; M.SOFT=[10,0.95]; M.CAM=[7.5,1]; M.INSTANT=[Infinity,1];

// a value that changes target many times = the sum of one spring per change.
// period>0 and a closed loop adds the previous cycle's residue so t=period == t=0.
M.track = (v0,keys,def=M.MORPH,period=0)=>{
  let prev=v0; const ks=[];
  for(const k of keys){const d=k[1]-prev; prev=k[1]; const sp=k[2]||def; if(d!==0) ks.push([k[0],d,sp[0],sp[1]]);}
  const loop = period>0 && Math.abs(prev-v0)<1e-9;
  return t=>{let v=v0; for(const k of ks){v+=k[1]*S(t-k[0],k[2],k[3]); if(loop) v+=k[1]*(S(t+period-k[0],k[2],k[3])-1);} return v;};
};
const hex = M.hex = h=>[1,3,5].map(i=>parseInt(h.slice(i,i+2),16));
M.ctrack = (h0,keys,def=[20,1],period=0)=>{
  const c0=hex(h0); const tr=[0,1,2].map(i=>M.track(c0[i],keys.map(k=>[k[0],hex(k[1])[i],k[2]]),def,period));
  return t=>`rgb(${tr.map(f=>Math.round(clamp(f(t),0,255))).join(',')})`;
};
// step helper: pick the latest value whose time has passed
M.step = (v0,keys)=>t=>{let v=v0; for(const k of keys) if(t>=k[0]) v=k[1]; return v;};

// content swap: exit blurs out fast; enter waits, then blurs in (own timings -> no overlap)
M.vis = (t,tin,tout,o={})=>{
  const din=o.din??0.07, lin=o.lin??0.26, lout=o.lout??0.12, bl=o.blur??12;
  const a = tin==null?1:eo((t-tin-din)/lin);
  const b = tout==null?0:eo((t-tout)/lout);
  return {o:a*(1-b), blur:(1-a)*bl+b*bl*0.8, s:(0.94+0.06*a)*(1-0.03*b), a, b};
};
M.apply = (el,v,extra='')=>{
  if(v.o<0.002){el.style.display='none';return false;}
  el.style.display=''; el.style.opacity=v.o.toFixed(4);
  el.style.filter=v.blur>0.05?`blur(${v.blur.toFixed(2)}px)`:'none';
  el.style.transform=`scale(${v.s.toFixed(4)})${extra}`;
  return true;
};
M.setText = (el,s)=>{ if(el._t!==s){ el.textContent=s; el._t=s; } };

// one icon set, 24-grid, stroke normalised so every icon has the same world stroke width
M.IC = {
 arrow:['M5 12h14','M13 5l7 7-7 7'], check:['M20 6 9 17l-5-5'], x:['M18 6 6 18','M6 6l12 12'], plus:['M5 12h14','M12 5v14'],
 folder:['M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z'],
 terminal:['m4 17 6-6-6-6','M12 19h8'], file:['M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z','M14 2v4a2 2 0 0 0 2 2h4','M8 13h8','M8 17h5'],
 pencil:['M21.17 6.81a1 1 0 0 0-3.99-3.99L3.84 16.17a2 2 0 0 0-.5.83l-1.32 4.35a.5.5 0 0 0 .62.62l4.35-1.32a2 2 0 0 0 .83-.5z','m15 5 4 4'],
 coin:['M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20Z','M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8','M12 18V6'],
 clock:['M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20Z','M12 6v6l4 2'],
 chip:['M6 4h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z','M9 9h6v6H9z','M9 1v3','M15 1v3','M9 20v3','M15 20v3','M20 9h3','M20 14h3','M1 9h3','M1 14h3'],
 sparkle:['M9.94 15.5A2 2 0 0 0 8.5 14.06l-6.14-1.58a.5.5 0 0 1 0-.96L8.5 9.94A2 2 0 0 0 9.94 8.5l1.58-6.14a.5.5 0 0 1 .96 0L14.06 8.5A2 2 0 0 0 15.5 9.94l6.14 1.58a.5.5 0 0 1 0 .96L15.5 14.06a2 2 0 0 0-1.44 1.44l-1.58 6.14a.5.5 0 0 1-.96 0z'],
 castle:['M3 21V9l3-1v2h3V7l3-2 3 2v3h3V8l3 1v12','M3 21h18','M10 21v-4a2 2 0 0 1 4 0v4','M6 13h1','M17 13h1'],
 search:['M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16Z','m21 21-4.3-4.3'],
 calendar:['M8 2v4','M16 2v4','M5 4h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z','M3 10h18'],
 message:['M7.9 20A9 9 0 1 0 4 16.1L2 22Z'],
 sheet:['M5 3h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Z','M3 9h18','M3 15h18','M9 3v18'],
 receipt:['M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z','M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8','M12 17.5v-11'],
 bell:['M10.268 21a2 2 0 0 0 3.464 0','M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326'],
 user:['M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2','M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8Z'],
 spade:['M5 9c-1.5 1.5-3 3.2-3 5.5A5.5 5.5 0 0 0 7.5 20c1.8 0 3-.5 4.5-2 1.5 1.5 2.7 2 4.5 2a5.5 5.5 0 0 0 5.5-5.5c0-2.3-1.5-4-3-5.5l-7-7-7 7Z','M12 18v4'],
 workflow:['M5 3h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Z','M7 11v4a2 2 0 0 0 2 2h4','M15 13h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-4a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2Z'],
 link:['M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71','M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71'],
 image:['M5 3h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Z','M9 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z','m21 15-3.09-3.09a2 2 0 0 0-2.82 0L6 21'],
 zap:['M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z'],

};
M.icon = (name,size,color,sw=2.2)=>`<svg width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="${color}" stroke-width="${(sw*24/size).toFixed(3)}" stroke-linecap="round" stroke-linejoin="round">${M.IC[name].map(d=>`<path d="${d}"/>`).join('')}</svg>`;

// cursor path: keyframes [t,x,y] in world coords, eased between keys with a slight human arc
M.path = (CK)=>t=>{
  if(t<=CK[0][0]) return {x:CK[0][1],y:CK[0][2]};
  const L=CK[CK.length-1]; if(t>=L[0]) return {x:L[1],y:L[2]};
  let i=0; while(t>=CK[i+1][0]) i++;
  const [t0,x0,y0]=CK[i],[t1,x1,y1]=CK[i+1];
  const u=eio((t-t0)/(t1-t0)), dx=x1-x0, dy=y1-y0, arc=Math.sin(Math.PI*u)*0.06;
  return {x:x0+dx*u-dy*arc, y:y0+dy*u+dx*arc};
};
M.presses = (clicks=[],drags=[])=>{
  const k=[];
  for(const c of clicks){k.push([c-0.07,1,[45,1]],[c+0.035,0,[22,0.72]]);}
  for(const [a,b] of drags){k.push([a-0.04,1,[45,1]],[b,0,[22,0.72]]);}
  k.sort((a,b)=>a[0]-b[0]); return M.track(0,k);
};
// time at which a monotonic function first crosses a threshold (precomputed at 1ms)
M.crossTimes = (f,t0,t1,ths)=>ths.map(th=>{for(let t=t0;t<=t1;t+=0.001) if(f(t)>=th) return t; return Infinity;});

/* scene runner
 cfg = { W,H, center:[x,y], bg:'#hex'|null(alpha), SH:{name:{w,h,r,bg,cam}}, start:'name', SEQ:[[t,'name'],...],
         layers:[{el,tin,tout,anchor:'c'|'t'|'l',o,update(t,g)}], cursor:{keys,clicks,drags,size}, shapePress:[t],
         intro:t|null, geom(t,g) -> g, extra(t,g), T }                                                              */
M.scene = (cfg)=>{
  const $=id=>document.getElementById(id);
  const {W,H}=cfg; const [CX,CY]=cfg.center||[W/2,H/2];
  const stage=$('stage'), world=$('world'), shape=$('shape'), cur=$('cursor');
  stage.style.width=W+'px'; stage.style.height=H+'px'; $('wrap').style.width=W+'px'; $('wrap').style.height=H+'px';
  stage.style.background=cfg.bg||'transparent';
  if(!cfg.bg) document.documentElement.classList.add('alpha');
  const P0=cfg.SH[cfg.start], SEQ=cfg.SEQ;
  const sp=cfg.spring||M.MORPH;
  const tr=k=>M.track(P0[k],SEQ.map(([t,n])=>[t,cfg.SH[n][k]]),sp);
  const shW=tr('w'), shH=tr('h'), shR=tr('r');
  const shBG=M.ctrack(P0.bg,SEQ.map(([t,n])=>[t,cfg.SH[n].bg]),[20,1]);
  const cam=M.track(P0.cam,SEQ.map(([t,n])=>[t,cfg.SH[n].cam]),cfg.camSpring||M.CAM);
  const press=M.track(0,(cfg.shapePress||[]).flatMap(c=>[[c-0.07,1,[45,1]],[c+0.035,0,[22,.72]]]));
  const intro=cfg.intro===undefined?0.02:cfg.intro;
  const cpath=cfg.cursor?M.path(cfg.cursor.keys):null, cpress=cfg.cursor?M.presses(cfg.cursor.clicks,cfg.cursor.drags):null;
  if(cfg.cursor) cur.style.width=(cfg.cursor.size||46)+'px'; else cur.style.display='none';
  const layers=(cfg.layers||[]).map(L=>({...L,node:$(L.el)}));
  // speaker layer: the speaker's own footage (a JPEG frame sequence) in a box that springs between named boxes.
  // cfg.speaker = {src:'../work/frames/03/', fps:60, ext:'jpg', boxes:{full:[0,0,W,H,0], corner:[x,y,w,h,r]}, start:'full',
  //                SEQ:[[t,'corner'],[t2,'full']], spring:M.MORPH, focus:'auto' | [fx,fy], shadow:'css box-shadow'}
  // focus 'auto' follows the head per frame (window.SPK_FOCUS from speaker_frames.py -> focus.js, injected by build.py).
  const SP=cfg.speaker; let spk=null;
  if(SP){
    const bx=SP.boxes||{}; bx.full=bx.full||[0,0,W,H,0]; const st0=bx[SP.start||'full'], sseq=SP.SEQ||[];
    const trk=i=>M.track(st0[i],sseq.map(([t,n])=>[t,bx[n][i]]),SP.spring||M.MORPH);
    spk={el:$('spk'),img:$('spk').querySelector('img'),x:trk(0),y:trk(1),w:trk(2),h:trk(3),r:trk(4),fps:SP.fps||30,ext:SP.ext||'jpg',src:SP.src,focus:SP.focus||'auto'};
    spk.el.style.display='block'; if(SP.shadow) spk.el.style.boxShadow=SP.shadow;
    window.READY=async()=>{const im=spk.img; if(!im.complete) await new Promise(r=>{im.onload=r;im.onerror=r;}); try{await im.decode();}catch(e){}};
  }
  const seek=(t)=>{
    let g={t, w:shW(t), h:shH(t), r:shR(t), bg:shBG(t), s:cam(t), cx:0, cy:0, fx:0, fy:0, sc:1-0.035*press(t), op:1};
    if(intro!=null){const a=S(t-intro,13,0.78); g.sc*=0.55+0.45*a; g.op=clamp((t-intro)/0.12);}
    g.cursor=cpath?cpath(t):null;
    if(cfg.geom) g=cfg.geom(t,g)||g;
    g.r=Math.min(g.r,g.h/2,g.w/2);
    world.style.transform=`translate(${(CX-g.s*g.fx).toFixed(3)}px,${(CY-g.s*g.fy).toFixed(3)}px) scale(${g.s.toFixed(5)})`;
    const st=shape.style;
    st.left=(g.cx-g.w/2).toFixed(3)+'px'; st.top=(g.cy-g.h/2).toFixed(3)+'px';
    st.width=g.w.toFixed(3)+'px'; st.height=g.h.toFixed(3)+'px'; st.borderRadius=g.r.toFixed(3)+'px';
    st.background=g.bg; st.transform=`scale(${g.sc.toFixed(5)})`; st.opacity=g.op.toFixed(4);
    for(const L of layers){
      const v=M.vis(t,L.tin,L.tout,L.o||{});
      if(M.apply(L.node,v)){
        const an=L.anchor||'c';
        L.node.style.left=(an==='l'?0:g.w/2).toFixed(3)+'px';
        L.node.style.top=(an==='t'?0:g.h/2).toFixed(3)+'px';
        if(L.update) L.update(t,g,v);
      }
    }
    if(cfg.extra) cfg.extra(t,g);
    if(spk){
      const x=spk.x(t),y=spk.y(t),w=Math.max(1,spk.w(t)),h=Math.max(1,spk.h(t)),r=Math.max(0,spk.r(t));
      const s=spk.el.style; s.left=x.toFixed(2)+'px'; s.top=y.toFixed(2)+'px'; s.width=w.toFixed(2)+'px'; s.height=h.toFixed(2)+'px'; s.borderRadius=r.toFixed(2)+'px';
      const k=Math.max(w/W,h/H), iw=W*k, ih=H*k, is=spk.img.style;
      const n=Math.max(1,Math.floor(t*spk.fps+1e-6)+1), src=spk.src+String(n).padStart(5,'0')+'.'+spk.ext;
      // re-centre on the subject: put the head at the box's horizontal centre and 40% down, as far as the image still covers the box
      let f=spk.focus; if(f==='auto'){const F=window.SPK_FOCUS; f=(F&&F.f&&F.f.length)?F.f[Math.min(F.f.length-1,n-1)]:[0.5,0.4];}
      const cl=(v,a,b)=>Math.min(b,Math.max(a,v));
      is.width=iw.toFixed(2)+'px'; is.height=ih.toFixed(2)+'px';
      is.left=cl(w*0.5-f[0]*iw,w-iw,0).toFixed(2)+'px'; is.top=cl(h*0.4-f[1]*ih,h-ih,0).toFixed(2)+'px';
      if(spk.img._s!==src){spk.img.src=src;spk.img._s=src;}
    }
    if(cpath){
      const c=g.cursor, sx=CX+g.s*(c.x-g.fx), sy=CY+g.s*(c.y-g.fy);
      cur.style.transform=`translate(${(sx-3).toFixed(2)}px,${(sy-3).toFixed(2)}px) scale(${(1-0.13*cpress(t)).toFixed(4)})`;
    }
  };
  window.seek=seek; window.DURATION=cfg.T;
  // preview mode: loop in the browser, scaled to fit
  const RENDER=location.search.includes('render');
  document.body.classList.add(RENDER?'render':'preview');
  seek(0);
  if(!RENDER){
    const fit=()=>{const k=Math.min(innerWidth/W,(innerHeight-30)/H);const wr=$('wrap');wr.style.transform=`translate(-50%,-50%) scale(${k})`;};
    fit(); addEventListener('resize',fit);
    const t0=performance.now();
    const loop=()=>{seek(((performance.now()-t0)/1000)%(cfg.T+0.8));requestAnimationFrame(loop);};
    requestAnimationFrame(loop);
  }
  return seek;
};
})();
