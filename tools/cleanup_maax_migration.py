from pathlib import Path
import re, html
ROOT=Path(__file__).resolve().parents[1]

def patch(rel, reps):
    p=ROOT/rel
    s=p.read_text(encoding='utf-8')
    for a,b in reps:
        s=s.replace(a,b)
    p.write_text(s,encoding='utf-8')
    print('patched',rel)

# Homepage: repair footer and remove fake MAAX traditional/outdoor model recommendations created by the broad brand swap.
patch('index.html',[
    ('href="#hekla">MAAX Saunas Saunas','href="#maax">MAAX Saunas'),
    ("'outdoor sauna Cabin','MAAX Saunas','Traditional Outdoor'","'Traditional Outdoor Sauna Consultation','Pittsburgh Sauna','Traditional Outdoor'"),
    ("'MAAX Saunas Larger Outdoor Cabin','MAAX Saunas','Traditional Outdoor'","'Larger Traditional Outdoor Sauna Consultation','Pittsburgh Sauna','Traditional Outdoor'"),
    ("'MAAX infrared Sauna','MAAX Saunas','Infrared'","'MAAX SaunaWellness PRO 5 / PRO 10','MAAX Saunas','Infrared'"),
    ("small?'traditional sauna 210X':'traditional sauna Sauna','MAAX Saunas','Traditional'","small?'Compact Traditional Sauna Consultation':'Traditional Sauna Consultation','Pittsburgh Sauna','Traditional'"),
    ("'MAAX Saunas Larger Traditional Model','MAAX Saunas','Traditional'","'Larger Traditional Sauna Consultation','Pittsburgh Sauna','Traditional'"),
    ("'traditional sauna Sauna','MAAX Saunas','Traditional'","'Traditional Sauna Consultation','Pittsburgh Sauna','Traditional'"),
])

# Cal page: MAAX is not an outdoor/traditional line in the verified SaunaWellness catalog.
patch('cal-saunas/index.html',[
    ('MAAX Saunas Saunas','MAAX Saunas'),
    ('against an outdoor MAAX Saunas','against other outdoor sauna choices'),
    ('outdoor MAAX Saunas','outdoor sauna'),
])

# Social-share redirect: repair image URL left by automated migration.
patch('launch/index.html',[
    ('https://pittsburghsauna.com/../assets/traditional-sauna.svg','https://pittsburghsauna.com/assets/site-images/Solara-Outdoor-product-img-2-a97e1336a8.webp'),
    ('MAAX Saunas Saunas','MAAX Saunas'),
])

# Learning center index cleanup.
patch('learning-center/index.html',[
    ('MAAX Saunas Saunas','MAAX Saunas'),
    ('When to look at MAAX Saunas, when Cal Saunas makes sense','When MAAX SaunaWellness makes sense, when Cal Saunas makes sense'),
])

# Replace Bubbles with clean MAAX-aware behavior. No Hekla model/heater logic remains.
bubbles=r'''(()=>{
  if(window.__pghBubblesLoaded)return; window.__pghBubblesLoaded=true;
  const script=document.currentScript; const base=script&&script.src?script.src.replace(/bubbles\.js(?:\?.*)?$/,''):'';
  if(!window.__pghAnalyticsLoader){window.__pghAnalyticsLoader=true;const ga=document.createElement('script');ga.src=base+'analytics.js?v=20260825-1';ga.defer=true;document.head.appendChild(ga);}
  const icon=base+'bubbles.svg';
  const path=location.pathname.toLowerCase().replace(/\/+$/,'')||'/';
  const page=path.includes('/specials')?'specials':path.includes('/maax-saunas')?'maax':path.includes('/cal-saunas')?'cal':path.includes('/learning-center')?'learning':'home';
  const depth=location.pathname.split('/').filter(Boolean).length; const root='../'.repeat(depth);
  const css=`#bb-wrap{position:fixed;right:18px;bottom:18px;z-index:9999;font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;color:#172326}#bb-launch{display:flex;align-items:center;gap:10px;border:0;background:transparent;padding:0;cursor:pointer;filter:drop-shadow(0 8px 18px rgba(0,0,0,.18))}#bb-launch img{width:66px;height:66px;border-radius:50%;display:block;background:#fff}#bb-teaser{background:#fffaf2;border:1px solid #d9cfbf;border-radius:999px;padding:11px 15px;font-size:13px;font-weight:800;max-width:230px;box-shadow:0 8px 24px rgba(0,0,0,.14);opacity:0;transform:translateX(8px);transition:.22s ease;pointer-events:none}#bb-teaser.show{opacity:1;transform:translateX(0)}#bb-panel{position:absolute;right:0;bottom:82px;width:min(365px,calc(100vw - 32px));background:#fffaf2;border:1px solid #d9cfbf;border-radius:18px;box-shadow:0 18px 48px rgba(0,0,0,.23);overflow:hidden;display:none}#bb-panel.open{display:block}.bb-head{background:#0e1719;color:white;padding:14px 15px;display:flex;align-items:center;gap:10px}.bb-head img{width:42px;height:42px;border-radius:50%;background:#fff}.bb-head b{display:block}.bb-head small{color:#efc57c}.bb-close{margin-left:auto;border:0;background:transparent;color:#fff;font-size:24px;cursor:pointer}.bb-body{padding:15px;max-height:430px;overflow:auto}.bb-msg{background:#fff;border:1px solid #e4dbce;border-radius:14px 14px 14px 4px;padding:11px 12px;margin:0 0 10px;font-size:13px;line-height:1.45}.bb-msg.me{background:#eaf3fb;border-color:#c8dfef;border-radius:14px 14px 4px 14px;margin-left:36px}.bb-actions{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 4px}.bb-actions button,.bb-actions a{border:1px solid #bba889;background:#fff;color:#172326;border-radius:999px;padding:8px 11px;font-size:11px;font-weight:800;cursor:pointer;text-decoration:none}.bb-actions .gold{background:#c48a26;color:white;border-color:#c48a26}.bb-input{display:flex;gap:8px;border-top:1px solid #e1d8ca;padding:11px;background:#fff}.bb-input input{flex:1;border:1px solid #cfd5d2;border-radius:10px;padding:10px;font:inherit;font-size:13px}.bb-input button{border:0;background:#0e1719;color:white;border-radius:10px;padding:0 13px;font-weight:800;cursor:pointer}@media(max-width:600px){#bb-wrap{right:12px;bottom:12px}#bb-launch img{width:52px;height:52px}#bb-teaser{display:none}#bb-panel{position:fixed;right:12px;left:12px;bottom:74px;width:auto;max-height:70vh}.bb-body{max-height:48vh}}`;
  const style=document.createElement('style');style.textContent=css;document.head.appendChild(style);
  const wrap=document.createElement('div');wrap.id='bb-wrap';wrap.innerHTML=`<div id="bb-panel" role="dialog" aria-label="Chat with Bubbles"><div class="bb-head"><img src="${icon}" alt="Bubbles"><div><b>Bubbles</b><small>Your sauna sidekick</small></div><button class="bb-close" aria-label="Close Bubbles">×</button></div><div class="bb-body" id="bb-body"></div><div class="bb-input"><input id="bb-input" aria-label="Ask Bubbles a question" placeholder="Ask me about saunas, sizes, savings…"><button id="bb-send">Send</button></div></div><button id="bb-launch" aria-label="Open Bubbles"><span id="bb-teaser"></span><img src="${icon}" alt="Bubbles"></button>`;document.body.appendChild(wrap);
  const panel=wrap.querySelector('#bb-panel'),body=wrap.querySelector('#bb-body'),teaser=wrap.querySelector('#bb-teaser'),input=wrap.querySelector('#bb-input');
  const add=(txt,me=false)=>{const d=document.createElement('div');d.className='bb-msg'+(me?' me':'');d.innerHTML=txt;body.appendChild(d);body.scrollTop=body.scrollHeight};
  const actions=items=>{const d=document.createElement('div');d.className='bb-actions';items.forEach(i=>{const el=i.href?document.createElement('a'):document.createElement('button');el.textContent=i.label;if(i.href)el.href=i.href;if(i.gold)el.classList.add('gold');if(i.on)el.onclick=i.on;d.appendChild(el)});body.appendChild(d)};
  const answer=q=>{const t=q.toLowerCase();
    if(/maax/.test(t)){add('MAAX SaunaWellness is our premium infrared line, with PRO 5 and PRO 10 cabins from one to four people. PRO 5 focuses on compact 110V installations; PRO 10 steps up to larger Red Cedar cabins and broader-spectrum infrared.');actions([{label:'Explore MAAX Saunas',href:root+'maax-saunas/',gold:true},{label:'Get Special Savings',href:root+'specials/'}]);return;}
    if(/traditional|infrared/.test(t)){add('Traditional uses a hot room, stones and optional steam. Infrared uses radiant heat at lower air temperatures. MAAX SaunaWellness and Cal Saunas are our current infrared choices; our traditional category is being updated.');actions([{label:'Use Sauna Finder',href:root+'#finder',gold:true}]);return;}
    if(/heater|harvia|kilowatt|kw/.test(t)){add('Electrical and heater requirements depend on the exact sauna. MAAX PRO 5 models are 110V/20A and PRO 10 models are 220V/20A. For traditional sauna projects, we will match the heater after the room and final product are selected.');actions([{label:'Electrical Guide',href:root+'learning-center/sauna-electrical-requirements/'}]);return;}
    if(/price|sale|special|saving|deal|discount|duck/.test(t)){add('We publish current Cal Sauna pricing, and MAAX pricing is being added. You can also request the current Duck Bucks special on a qualifying complete sauna.');actions([{label:'Get Duck Bucks',href:root+'specials/',gold:true},{label:'See MAAX',href:root+'maax-saunas/'}]);return;}
    if(/showroom|visit|location|monroeville|wexford/.test(t)){add('We have showrooms in Monroeville and Wexford.');actions([{label:'Showroom Details',href:root+'#showrooms',gold:true},{label:'Call 412-326-0361',href:'tel:+14123260361'}]);return;}
    if(/people|person|size|fit|room|space/.test(t)){add('Tell the Sauna Finder how many people will normally use it and where it will go. For MAAX, PRO 5 covers compact 1–2 person needs and PRO 10 covers 3–4 person cabins.');actions([{label:'Help Me Choose',href:root+'#finder',gold:true}]);return;}
    add('I can help with MAAX and Cal Saunas, sizing, electrical planning, showroom visits, or current Duck Bucks savings.');actions([{label:'Sauna Finder',href:root+'#finder'},{label:'Special Savings',href:root+'specials/',gold:true},{label:'Call 412-326-0361',href:'tel:+14123260361'}]);
  };
  const start=()=>{body.innerHTML='';if(page==='specials'){add('Hey — Bubbles here. I can help you claim the current Duck Bucks special.');actions([{label:'Get My Duck Bucks',href:'#questionnaire',gold:true}]);}else if(page==='maax'){add('Looking at MAAX SaunaWellness? I can help you compare the PRO 5 and PRO 10 infrared cabins by size, power and features.');actions([{label:'Compare MAAX Models',href:'#models',gold:true},{label:'Special Savings',href:'../specials/'}]);}else if(page==='cal'){add('Looking at Cal Saunas? I can help you compare the Solara sizes and the outdoor infrared model.');actions([{label:'Use Sauna Finder',href:'../#finder',gold:true},{label:'Special Savings',href:'../specials/'}]);}else if(page==='learning'){add('Doing your homework? Ask me about infrared vs. traditional, sizing, electrical needs, or current savings.');actions([{label:'Sauna Finder',href:root+'#finder',gold:true},{label:'Special Savings',href:root+'specials/'}]);}else{add('Hey — I’m Bubbles. I can help you narrow down the right sauna without turning this into homework.');actions([{label:'Help Me Choose',href:'#finder',gold:true},{label:'MAAX SaunaWellness',href:'maax-saunas/'},{label:'Duck Bucks',href:'specials/'}]);}};
  wrap.querySelector('#bb-launch').onclick=()=>{panel.classList.toggle('open');teaser.classList.remove('show');if(panel.classList.contains('open')&&!body.children.length)start()};wrap.querySelector('.bb-close').onclick=()=>panel.classList.remove('open');const send=()=>{const q=input.value.trim();if(!q)return;add(q,true);input.value='';answer(q)};wrap.querySelector('#bb-send').onclick=send;input.addEventListener('keydown',e=>{if(e.key==='Enter')send()});const nudge=txt=>{teaser.textContent=txt;teaser.classList.add('show')};setTimeout(()=>nudge(page==='specials'?'Want your Duck Bucks?':'Need help choosing?'),4500);
})();'''
(ROOT/'assets/bubbles.js').write_text(bubbles,encoding='utf-8')
print('rewrote assets/bubbles.js')

STYLE='''body{margin:0;font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;background:#fbf8f2;color:#172326;line-height:1.65}a{color:#76542d}.wrap{width:min(1000px,calc(100% - 36px));margin:auto}.hero{background:#172123;color:#fff;padding:70px 0}.hero h1{font:500 56px Georgia,serif;line-height:1.04;margin:10px 0 16px}.hero p{font-size:19px;color:#dce2e2;max-width:790px}.eyebrow{text-transform:uppercase;letter-spacing:.17em;font-size:11px;font-weight:800;color:#e0b67f}.section{padding:58px 0}.section.alt{background:#efe7db}.section h2{font:500 38px Georgia,serif;margin:0 0 15px}.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}.card{background:#fff;border:1px solid #ded5c8;padding:25px}.card h3{font:500 27px Georgia,serif;margin:0 0 8px}.price{font:700 25px Georgia,serif}.note{border-left:4px solid #c29358;background:#fff;padding:18px 20px;margin:20px 0}.cta{background:#0e1719;color:#fff;padding:48px 0}.btn{display:inline-block;background:#c29358;color:#111;text-decoration:none;padding:14px 19px;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.07em;margin:8px 8px 0 0}@media(max-width:700px){.hero h1{font-size:42px}.grid{grid-template-columns:1fr}}'''

def make_page(rel,title,desc,eyebrow,h1,lead,sections,buttons):
    depth=len(Path(rel).parents)-1
    root='../'*depth
    sec=''.join(f'<section class="section{" alt" if i%2 else ""}"><div class="wrap"><h2>{h}</h2>{body}</div></section>' for i,(h,body) in enumerate(sections))
    btns=''.join(f'<a class="btn" href="{href}">{label}</a>' for label,href in buttons)
    canonical='https://pittsburghsauna.com/'+str(Path(rel).parent).replace('\\','/')+'/'
    doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{canonical}"><style>{STYLE}</style></head><body><section class="hero"><div class="wrap"><div class="eyebrow">{eyebrow}</div><h1>{h1}</h1><p>{lead}</p></div></section>{sec}<section class="cta"><div class="wrap"><h2>Talk with Pittsburgh Sauna.</h2><p>Monroeville & Wexford · 412-326-0361</p>{btns}</div></section><script src="{root}assets/analytics.js" defer></script><script src="{root}assets/bubbles.js?v=20260902-1" defer></script></body></html>'''
    p=ROOT/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(doc,encoding='utf-8');print('rewrote',rel)

make_page('learning-center/2-person-sauna-pittsburgh/index.html','2 Person Sauna Pittsburgh | MAAX & Cal Infrared Options','Compare 2 person infrared saunas in Pittsburgh from MAAX SaunaWellness and Cal Saunas, including dimensions, electrical needs, pricing and local showroom guidance.','2 Person Sauna Pittsburgh','Two-person sauna choices that actually fit the room.','For most Pittsburgh homes, a two-person infrared sauna is one of the easiest ways to add a dedicated wellness space without giving up a huge footprint.',[
('Two strong places to start','<div class="grid"><div class="card"><h3>MAAX SaunaWellness PRO 5 · 2 Person</h3><p>Canadian Hemlock · 47&quot; W × 41&quot; D × 78&quot; H · 110V / 20A · 5 carbon heaters.</p><div class="price">Current dealer pricing being added</div></div><div class="card"><h3>Cal Saunas Solara-2</h3><p>Canadian Hemlock · 47&quot; W × 39&quot; D × 75&quot; H · 120V infrared.</p><div class="price">Current sale price: $3,495</div></div></div>'),
('What matters besides the seat count','<p>Measure the finished footprint, ceiling height, door swing, assembly space and the entire delivery route. A cabin that fits the room still has to make it through doors, stairs and turns.</p><div class="note"><b>Traditional heat?</b> We are updating our traditional sauna lineup. We will not steer you to an obsolete model just to fill the category.</div>')],[('Compare MAAX','../../maax-saunas/'),('Get Duck Bucks','../../specials/'),('Use Sauna Finder','../../#finder')])

make_page('learning-center/4-person-sauna-pittsburgh/index.html','4 Person Sauna Pittsburgh | MAAX PRO 10 & Cal Solara-4','Compare 4 person infrared sauna options in Pittsburgh including MAAX SaunaWellness PRO 10 and Cal Saunas Solara-4.','4 Person Sauna Pittsburgh','More room without jumping to a giant sauna.','A four-person cabin gives couples space to stretch out and makes shared sessions easier for families and guests.',[
('Current four-person infrared choices','<div class="grid"><div class="card"><h3>MAAX SaunaWellness PRO 10 · 4 Person</h3><p>Canadian Red Cedar · 70&quot; W × 47&quot; D × 81&quot; H · 220V / 20A · carbon plus full-spectrum infrared.</p><div class="price">Current dealer pricing being added</div></div><div class="card"><h3>Cal Saunas Solara-4</h3><p>Canadian Hemlock · 69&quot; W × 47&quot; D × 75&quot; H · 120V infrared.</p><div class="price">Current sale price: $4,095</div></div></div>'),
('Buy for normal use','<p>If two people will use the sauna most of the time, a 3–4 person cabin can be a smart comfort upgrade. If you specifically want stones, steam and classic high heat, ask us about the traditional category we are currently rebuilding.</p>')],[('Compare MAAX','../../maax-saunas/'),('Get Duck Bucks','../../specials/'),('Use Sauna Finder','../../#finder')])

make_page('learning-center/infrared-sauna-pittsburgh/index.html','Infrared Sauna Pittsburgh | MAAX & Cal Saunas','Shop and compare infrared saunas in Pittsburgh from MAAX SaunaWellness and Cal Saunas with local showroom guidance in Monroeville and Wexford.','Infrared Sauna Pittsburgh','Infrared sauna options with local Pittsburgh support.','Infrared is a strong fit for buyers who want radiant warmth, lower air temperatures and a routine that is easy to use several times a week.',[
('MAAX SaunaWellness','<p>MAAX gives us a premium infrared ladder from 1 to 4 people. PRO 5 uses Canadian Hemlock and compact 110V/20A configurations. PRO 10 steps up to Canadian Red Cedar, 220V/20A and broader-spectrum infrared.</p><a class="btn" href="../../maax-saunas/">Explore MAAX</a>'),
('Cal Saunas Solara','<p>Cal gives us 2-, 3- and 4-person indoor infrared cabins plus the Solara-Outdoor. Current published sale prices run from $3,495 for Solara-2 to $4,095 for Solara-4, with Solara-Outdoor at $3,990.</p><a class="btn" href="../../cal-saunas/">Explore Cal Saunas</a>')],[('Get Duck Bucks','../../specials/'),('Visit Showrooms','../../#showrooms')])

make_page('learning-center/full-spectrum-infrared/index.html','What Is Full-Spectrum Infrared? | Pittsburgh Sauna','Understand near, mid and far infrared sauna heat and how MAAX SaunaWellness PRO 5 and PRO 10 use different infrared systems.','Infrared Learning Center','What does full-spectrum infrared actually mean?','The phrase describes a heater system designed to cover a broader range of infrared wavelengths. It is useful, but it should never be the only reason you choose a sauna.',[
('MAAX gives us a useful real-world comparison','<div class="grid"><div class="card"><h3>PRO 5</h3><p>MAAX positions PRO 5 around far- and mid-infrared heat in a compact Canadian Hemlock cabin.</p></div><div class="card"><h3>PRO 10</h3><p>PRO 10 adds full-spectrum infrared elements alongside carbon heaters in a larger Canadian Red Cedar cabin.</p></div></div>'),
('Compare the entire cabin','<p>Heater placement, bench position, electrical requirements, materials, controls, warranty and how the sauna feels matter more than stacking up marketing buzzwords.</p>')],[('Explore MAAX','../../maax-saunas/'),('Infrared vs Traditional','../traditional-vs-infrared/')])

make_page('learning-center/home-sauna-pittsburgh/index.html','Home Sauna Pittsburgh | Local Buying Guide','A Pittsburgh home sauna guide covering MAAX and Cal infrared saunas, traditional vs infrared, sizing, electrical planning and local showrooms.','Home Sauna Pittsburgh','How to choose a home sauna in Pittsburgh.','Start with the experience you want, then match the sauna to your space, power and budget. That order is more useful than falling in love with a model first.',[
('Our current infrared lineup','<p><b>MAAX SaunaWellness:</b> premium 1–4 person indoor infrared cabins. <b>Cal Saunas:</b> 2–4 person indoor infrared plus an outdoor infrared model. We are also rebuilding our traditional sauna category after a manufacturer change.</p>'),
('Published pricing and special savings','<p>Current Cal infrared sale pricing starts at $3,495. MAAX dealer pricing is being added now. Qualifying complete-sauna purchases can also be eligible for our current Duck Bucks offer.</p>')],[('Use Sauna Finder','../../#finder'),('Compare MAAX','../../maax-saunas/'),('Get Duck Bucks','../../specials/')])

make_page('learning-center/indoor-vs-outdoor/index.html','Indoor vs Outdoor Sauna | Pittsburgh Sauna','Compare indoor and outdoor sauna placement, site preparation, electrical planning and current Pittsburgh sauna options.','Sauna Placement Guide','Indoor or outdoor: where should your sauna go?','Indoor wins on convenience. Outdoor wins when the sauna becomes part of the backyard. The best answer depends on the experience you want and the site you have.',[
('Indoor choices','<p>MAAX SaunaWellness is an indoor infrared line with 1–4 person options. Cal offers indoor Solara infrared cabins as well. Basements, home gyms, spare rooms and wellness rooms can all work when the exact model requirements are met.</p>'),
('Outdoor choices','<p>Cal Solara-Outdoor is our current published outdoor infrared option at a $3,990 sale price. For traditional outdoor projects, talk with us while we finalize the replacement traditional line.</p><div class="note"><b>Site prep:</b> use a stable, level base with appropriate drainage, access and electrical planning for the exact product. Do not attribute another manufacturer’s installation rules to MAAX.</div>')],[('See Cal Outdoor','../../cal-saunas/#outdoor'),('Use Sauna Finder','../../#finder')])

make_page('learning-center/which-sauna-brand/index.html','MAAX vs Cal Saunas Pittsburgh | Which Brand Fits You?','Compare MAAX SaunaWellness and Cal Saunas in Pittsburgh by size, electrical requirements, infrared features, outdoor options and pricing.','Brand Comparison','MAAX or Cal Saunas: which direction fits you?','Both are infrared lines, but they give us different price points, materials, electrical setups and product stories.',[
('Choose MAAX SaunaWellness if…','<p>You want a premium infrared line with 1–4 person choices, PRO 5 compact 110V models, or PRO 10 Red Cedar cabins with broader-spectrum infrared and wellness-focused features.</p>'),
('Choose Cal Saunas if…','<p>You want straightforward published sale pricing, 120V indoor Solara choices, or the current Solara-Outdoor infrared option.</p>'),
('Want traditional heat?','<p>We are actively rebuilding the traditional category after a manufacturer change. We would rather tell you that clearly than relabel an infrared product as something it is not.</p>')],[('Compare MAAX','../../maax-saunas/'),('Compare Cal','../../cal-saunas/'),('Get Duck Bucks','../../specials/')])

make_page('learning-center/best-sauna-price-pittsburgh/index.html','Best Sauna Price Pittsburgh | Current Deals & Duck Bucks','Compare current sauna pricing in Pittsburgh, including published Cal Sauna sale prices, MAAX pricing updates and Duck Bucks special savings.','Best Sauna Price Pittsburgh','The best sauna price is the best complete value.','Compare the complete cabin, required electrical work, included heating system, warranty, local support and current savings—not just the first number in an ad.',[
('What we publish today','<p>Cal Solara sale prices currently include Solara-2 at $3,495, Solara-3 at $3,795, Solara-4 at $4,095 and Solara-Outdoor at $3,990. MAAX dealer pricing is being added to the site.</p>'),
('Stack value, not fake discounts','<p>Our Duck Bucks offer can provide additional savings on qualifying complete-sauna purchases. Clearance opportunities may appear when inventory changes, but we will not advertise a clearance unit that does not exist.</p>')],[('Current Specials','../../specials/'),('Compare MAAX','../../maax-saunas/'),('Compare Cal','../../cal-saunas/')])

# Commercial-intent pages: preserve keywords but make claims current and accurate.
commercial={
 'sauna-sale-pittsburgh':('Sauna Sale Pittsburgh | Current Sauna Specials','Sauna sale Pittsburgh','Looking for a sauna sale in Pittsburgh? Start with current published pricing, then claim Duck Bucks for additional qualifying savings.'),
 'sauna-deals-pittsburgh':('Sauna Deals Pittsburgh | MAAX, Cal & Duck Bucks','Sauna deals Pittsburgh','The strongest sauna deal is one you can verify: real model pricing, current special savings and local support after the purchase.'),
 'sauna-clearance-pittsburgh':('Sauna Clearance Pittsburgh | Current Availability','Sauna clearance Pittsburgh','Clearance inventory changes. We use this page to connect Pittsburgh shoppers with any current closeout, floor-model or special-purchase opportunities without pretending inventory exists when it does not.'),
 'sauna-cost-pittsburgh':('Sauna Cost Pittsburgh | Prices & Planning','How much does a sauna cost in Pittsburgh?','Current Cal infrared sale pricing starts at $3,495. MAAX pricing is being added. Your complete project cost also depends on electrical work, delivery, site conditions and accessories.'),
 'sauna-installation-cost-pittsburgh':('Sauna Installation Cost Pittsburgh | Planning Guide','Sauna installation cost in Pittsburgh','Installation cost depends on the exact sauna, circuit, room or outdoor site, delivery route and whether site preparation is needed. We quote the product first, then plan the real installation around it.'),
 'traditional-sauna-pittsburgh':('Traditional Sauna Pittsburgh | Buying Guide','Traditional sauna Pittsburgh','Traditional sauna means high room heat, stones and optional steam. Our traditional product category is currently being updated after a manufacturer change; contact us for the current options rather than relying on an obsolete model list.'),
 'outdoor-sauna-pittsburgh':('Outdoor Sauna Pittsburgh | Backyard Sauna Guide','Outdoor sauna Pittsburgh','For outdoor infrared, Cal Solara-Outdoor is our current published option. For traditional outdoor sauna projects, we are updating the product line and can help plan the site while the final assortment is being completed.')
}
for slug,(title,h1,lead) in commercial.items():
    body='<p>We serve Western Pennsylvania from showrooms in Monroeville and Wexford. Current Cal pricing is published on the site; MAAX SaunaWellness pricing is being added, and Duck Bucks are available on qualifying complete-sauna purchases.</p><div class="note">Call 412-326-0361 if you want today’s inventory, current offer or a project-specific quote.</div>'
    make_page(f'learning-center/{slug}/index.html',title,lead,slug.replace('-',' ').title(),h1,lead,[('Current, verifiable information',body)],[('Get Duck Bucks','../../specials/'),('MAAX Saunas','../../maax-saunas/'),('Cal Saunas','../../cal-saunas/')])

# Sitemap should point to MAAX, never the retired product page.
p=ROOT/'sitemap.xml';s=p.read_text(encoding='utf-8').replace('https://pittsburghsauna.com/hekla-saunas/','https://pittsburghsauna.com/maax-saunas/');p.write_text(s,encoding='utf-8');print('patched sitemap.xml')

# Final customer-facing cleanup for malformed duplicate wording.
for p in ROOT.rglob('*.html'):
    if p.relative_to(ROOT).as_posix()=='hekla-saunas/index.html': continue
    s=p.read_text(encoding='utf-8').replace('MAAX Saunas Saunas','MAAX Saunas')
    p.write_text(s,encoding='utf-8')

# Audit retired brand references in customer-facing files; fail if found outside the intentional legacy redirect.
problems=[]
for p in list(ROOT.rglob('*.html'))+[ROOT/'assets/bubbles.js',ROOT/'sitemap.xml']:
    if not p.exists() or p.relative_to(ROOT).as_posix()=='hekla-saunas/index.html': continue
    txt=p.read_text(encoding='utf-8')
    if re.search(r'\bHekla\b',txt,re.I): problems.append(str(p.relative_to(ROOT)))
if problems:
    raise SystemExit('Retired-brand references remain in: '+', '.join(problems))
print('audit passed: no Hekla references in customer-facing pages')
