(()=>{
  if(window.__pghBubblesLoaded)return; window.__pghBubblesLoaded=true;
  const script=document.currentScript; const base=script&&script.src?script.src.replace(/bubbles\.js(?:\?.*)?$/,''):'';
  const icon=base+'bubbles.svg';
  const path=location.pathname.toLowerCase();
  const page=path.includes('/specials')?'specials':path.includes('/hekla-saunas')?'hekla':path.includes('/cal-saunas')?'cal':path.includes('/learning-center')?'learning':'home';
  const root=page==='home'?'':'../';
  const css=`
  #bb-wrap{position:fixed;right:18px;bottom:18px;z-index:9999;font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;color:#172326}
  #bb-launch{display:flex;align-items:center;gap:10px;border:0;background:transparent;padding:0;cursor:pointer;filter:drop-shadow(0 8px 18px rgba(0,0,0,.18))}
  #bb-launch img{width:66px;height:66px;border-radius:50%;display:block;background:#fff}
  #bb-teaser{background:#fffaf2;border:1px solid #d9cfbf;border-radius:999px;padding:11px 15px;font-size:13px;font-weight:800;max-width:230px;box-shadow:0 8px 24px rgba(0,0,0,.14);opacity:0;transform:translateX(8px);transition:.22s ease;pointer-events:none}
  #bb-teaser.show{opacity:1;transform:translateX(0)}
  #bb-panel{position:absolute;right:0;bottom:82px;width:min(365px,calc(100vw - 32px));background:#fffaf2;border:1px solid #d9cfbf;border-radius:18px;box-shadow:0 18px 48px rgba(0,0,0,.23);overflow:hidden;display:none}
  #bb-panel.open{display:block}
  .bb-head{background:#0e1719;color:white;padding:14px 15px;display:flex;align-items:center;gap:10px}.bb-head img{width:42px;height:42px;border-radius:50%;background:#fff}.bb-head b{display:block}.bb-head small{color:#efc57c}.bb-close{margin-left:auto;border:0;background:transparent;color:#fff;font-size:24px;cursor:pointer;line-height:1}
  .bb-body{padding:15px;max-height:430px;overflow:auto}.bb-msg{background:#fff;border:1px solid #e4dbce;border-radius:14px 14px 14px 4px;padding:11px 12px;margin:0 0 10px;font-size:13px;line-height:1.45}.bb-msg.me{background:#eaf3fb;border-color:#c8dfef;border-radius:14px 14px 4px 14px;margin-left:36px}
  .bb-actions{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 4px}.bb-actions button,.bb-actions a{border:1px solid #bba889;background:#fff;color:#172326;border-radius:999px;padding:8px 11px;font-size:11px;font-weight:800;cursor:pointer;text-decoration:none}.bb-actions .gold{background:#c48a26;color:white;border-color:#c48a26}
  .bb-input{display:flex;gap:8px;border-top:1px solid #e1d8ca;padding:11px;background:#fff}.bb-input input{flex:1;border:1px solid #cfd5d2;border-radius:10px;padding:10px;font:inherit;font-size:13px}.bb-input button{border:0;background:#0e1719;color:white;border-radius:10px;padding:0 13px;font-weight:800;cursor:pointer}
  .heater-reco{margin-top:14px;padding:12px 13px;background:#f3ede4;border-top:1px solid #ded5c8;font-size:11px;line-height:1.45}.heater-reco b{display:block;color:#76542d;text-transform:uppercase;letter-spacing:.07em;font-size:9px;margin-bottom:4px}.heater-reco strong{font-size:12px;color:#172326}.heater-reco .alt-heater{display:block;color:#687477;margin-top:4px}.heater-reco .heater-note{display:block;color:#778184;margin-top:5px;font-size:9px}
  @media(max-width:600px){#bb-wrap{right:12px;bottom:12px}#bb-launch img{width:52px;height:52px}#bb-teaser{display:none}#bb-panel{position:fixed;right:12px;left:12px;bottom:74px;width:auto;max-height:70vh}.bb-body{max-height:48vh}}
  `;
  const style=document.createElement('style');style.textContent=css;document.head.appendChild(style);

  if(page==='hekla'){
    const traditional=document.querySelector('#traditional');
    if(traditional){
      traditional.querySelectorAll('.model').forEach(card=>{
        const title=card.querySelector('h3');
        if(!title||!/^Traditional\s+(160|210|210X|220)$/i.test(title.textContent.trim()))return;
        const price=card.querySelector('.price');
        if(!price||card.querySelector('.heater-reco'))return;
        const rec=document.createElement('div');
        rec.className='heater-reco';
        rec.innerHTML='<b>Recommended Heater — Sold Separately</b><strong>Harvia Cilindro PC90E · 9 kW — $1,318</strong><span class="alt-heater">Wall-mount alternative: Harvia Spirit SP90E · 9 kW — $1,930</span><span class="heater-note">Heater pricing shown separately from sauna price. Controls, stones and electrical installation are separate unless specifically included in your quote.</span>';
        price.insertAdjacentElement('afterend',rec);
      });
    }
  }

  const wrap=document.createElement('div');wrap.id='bb-wrap';
  wrap.innerHTML=`<div id="bb-panel" role="dialog" aria-label="Chat with Bubbles"><div class="bb-head"><img src="${icon}" alt="Bubbles"><div><b>Bubbles</b><small>Your sauna sidekick</small></div><button class="bb-close" aria-label="Close Bubbles">×</button></div><div class="bb-body" id="bb-body"></div><div class="bb-input"><input id="bb-input" aria-label="Ask Bubbles a question" placeholder="Ask me about saunas, heaters, savings…"><button id="bb-send">Send</button></div></div><button id="bb-launch" aria-label="Open Bubbles"><span id="bb-teaser"></span><img src="${icon}" alt="Bubbles"></button>`;
  document.body.appendChild(wrap);
  const panel=wrap.querySelector('#bb-panel'),body=wrap.querySelector('#bb-body'),teaser=wrap.querySelector('#bb-teaser'),input=wrap.querySelector('#bb-input');
  const add=(txt,me=false)=>{const d=document.createElement('div');d.className='bb-msg'+(me?' me':'');d.innerHTML=txt;body.appendChild(d);body.scrollTop=body.scrollHeight};
  const actions=(items)=>{const d=document.createElement('div');d.className='bb-actions';items.forEach(i=>{const el=i.href?document.createElement('a'):document.createElement('button');el.textContent=i.label;if(i.href)el.href=i.href;if(i.gold)el.classList.add('gold');if(i.on)el.onclick=i.on;d.appendChild(el)});body.appendChild(d);};
  const answer=(q)=>{
    const t=q.toLowerCase();
    if(/traditional|infrared/.test(t)){add('Traditional gives you the classic high-heat sauna experience with stones and optional steam. Infrared heats you more directly at a lower air temperature and is easy for everyday use. If you tell me how you plan to use it, the Sauna Finder can narrow it down.');actions([{label:'Use Sauna Finder',href:root+'#finder',gold:true}]);return;}
    if(/heater|harvia|9 ?kw|kilowatt/.test(t)){add(page==='hekla'?'Hekla traditional sauna prices are shown without the heater. For the traditional models, we recommend the 9 kW Harvia Cilindro PC90E, with the wall-mounted Spirit SP90E as an alternative. Heater pricing is shown separately so you can see exactly what you are buying.':'Some sauna models include their heating system and others use a separate heater. I can send you to the Sauna Finder so we match the heater to the room instead of guessing.');actions(page==='hekla'?[{label:'See Heater Options',href:'#heaters',gold:true}]:[{label:'Use Sauna Finder',href:root+'#finder',gold:true}]);return;}
    if(/price|sale|special|saving|deal|discount/.test(t)){add('There may be additional special savings available on the sauna or outdoor product you’re considering. We keep the offer itself private until you request it.');actions([{label:'Get Special Savings',href:root+'specials/',gold:true}]);return;}
    if(/showroom|visit|location|monroeville|wexford/.test(t)){add('We have showrooms in Monroeville and Wexford. If you want to see products in person, I can take you to the showroom section.');actions([{label:'Show Me the Showrooms',href:root+'#showrooms',gold:true}]);return;}
    if(/people|person|size|fit|room|space/.test(t)){add('The right size depends on how many people will use it and the space you have. The Sauna Finder is the fastest way to narrow that down without overbuying.');actions([{label:'Help Me Choose',href:root+'#finder',gold:true}]);return;}
    add('Good question. I don’t want to bluff when the exact answer depends on the model. I can help you narrow the choices, take you to current special savings, or get you to a showroom.');actions([{label:'Sauna Finder',href:root+'#finder'},{label:'Special Savings',href:root+'specials/',gold:true},{label:'Call 412-326-0361',href:'tel:+14123260361'}]);
  };
  const start=()=>{
    body.innerHTML='';
    if(page==='specials'){
      add('Hey — Bubbles here. I can help you get the current special savings without making you hunt around for it.');
      actions([{label:'Take Me to the Questionnaire',href:'#questionnaire',gold:true},{label:'What happens next?',on:()=>add('Complete the questionnaire and we’ll prepare the current offer in your name and email it to you.')}]);
    } else if(page==='hekla'){
      add('Looking at Hekla? I can help you compare the traditional, infrared and outdoor options — and match a separately priced heater where one is required.');
      actions([{label:'Traditional',href:'#traditional'},{label:'Infrared',href:'#infrared'},{label:'Outdoor',href:'#outdoor'},{label:'Heater Options',href:'#heaters'},{label:'Special Savings',href:'../specials/',gold:true}]);
    } else if(page==='cal'){
      add('Looking at Cal Saunas? I can help you narrow the type and size first, then point you toward current special savings when you’re ready.');
      actions([{label:'Help Me Choose',href:'../#finder',gold:true},{label:'Traditional vs Infrared?',on:()=>answer('traditional infrared')},{label:'Special Savings',href:'../specials/'}]);
    } else if(page==='learning'){
      add('Doing your homework? Good move. Ask me about traditional vs. infrared, sauna sizing, heaters, or where to see them in person.');
      actions([{label:'Sauna Finder',href:'../#finder',gold:true},{label:'Special Savings',href:'../specials/'}]);
    } else {
      add('Hey — I’m Bubbles. I can help you narrow down the right sauna without turning this into homework.');
      actions([{label:'Help Me Choose a Sauna',href:'#finder',gold:true},{label:'Traditional or Infrared?',on:()=>answer('traditional infrared')},{label:'Special Savings',href:'specials/'}]);
    }
  };
  wrap.querySelector('#bb-launch').onclick=()=>{panel.classList.toggle('open');teaser.classList.remove('show');if(panel.classList.contains('open')&&!body.children.length)start()};
  wrap.querySelector('.bb-close').onclick=()=>panel.classList.remove('open');
  const send=()=>{const q=input.value.trim();if(!q)return;add(q,true);input.value='';answer(q)};wrap.querySelector('#bb-send').onclick=send;input.addEventListener('keydown',e=>{if(e.key==='Enter')send()});
  const nudge=(txt)=>{teaser.textContent=txt;teaser.classList.add('show')};
  setTimeout(()=>nudge(page==='specials'?'Want the current special savings?':'Need help choosing?'),4500);
  if(page==='home'){
    const finder=document.querySelector('#finder');if(finder&&'IntersectionObserver'in window)new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting)nudge('Want me to narrow this down?')})},{threshold:.25}).observe(finder);
  }
  if(page==='hekla'||page==='cal'){
    let done=false;addEventListener('scroll',()=>{if(!done&&scrollY>document.documentElement.scrollHeight*.22){done=true;nudge('Want me to help compare these?')}},{passive:true});
  }
})();