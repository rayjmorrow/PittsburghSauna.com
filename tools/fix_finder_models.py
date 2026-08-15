from pathlib import Path
import re

p = Path('index.html')
s = p.read_text()

# Add result styling if it is not already present.
s = s.replace(
    '.result{display:none;background:#f8f3eb;border:1px solid #dfd3c2;padding:24px;margin-top:18px}.result.show{display:block}',
    '.result{display:none;background:#f8f3eb;border:1px solid #dfd3c2;padding:30px;margin-top:18px}.result.show{display:block}.result h3{font-size:32px;margin:4px 0 10px}.result-kicker{font-size:11px;text-transform:uppercase;letter-spacing:.18em;font-weight:800;color:#8a6338}.result-grid{display:grid;grid-template-columns:1fr;gap:12px;margin:20px 0}.result-box{background:#fff;border:1px solid #ded5c8;padding:17px}.result-box b{display:block;font-size:12px;letter-spacing:.07em;text-transform:uppercase;margin-bottom:5px}.result-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}.restart{background:none;border:0;padding:0;color:#76542d;font-weight:800;font-size:11px;letter-spacing:.08em;text-transform:uppercase;cursor:pointer}'
)

new_script = r'''<script>
const quiz=[
 {key:'location',title:'Where will your sauna go?',help:'Start with the space. This immediately narrows the best sauna styles for your home.',options:[['indoors','Indoors'],['outdoors','Outdoors'],['either','Either could work'],['unsure','I need help deciding']]},
 {key:'heat',title:'What sauna experience sounds best?',help:'There is no wrong answer. Choose the experience you picture yourself using most often.',options:[['traditional','Traditional high heat & steam'],['infrared','Gentler infrared warmth'],['compare','I want to compare both'],['unsure','Not sure — help me choose']]},
 {key:'seating',title:'How many people should it comfortably seat?',help:'Think about normal use, not just the biggest gathering you might have.',options:[['1-2','1–2 people'],['3-4','3–4 people'],['5plus','5+ people'],['unsure','I am not sure yet']]},
 {key:'priority',title:'What matters most to you?',help:'This helps us understand which features and construction details deserve the most attention.',options:[['traditional','Deep heat & the traditional sauna experience'],['daily','Everyday wellness & convenience'],['design','Design & appearance'],['outdoor','Creating an outdoor retreat']]},
 {key:'space',title:'How would you describe the space you have?',help:'Exact measurements can come later. For now, give us the closest description.',options:[['compact','Compact — I want to use space efficiently'],['medium','Medium — room for a typical 2–4 person sauna'],['large','Large — I have flexibility'],['measure','I need help measuring / planning the space']]}
];
let current=0,answers={};
const steps=document.getElementById('steps'),qbox=document.getElementById('qbox'),result=document.getElementById('result');
const labels=['Location','Sauna Style','Seating','Priorities','Available Space'];
function draw(){
 result.className='result';result.innerHTML='';qbox.style.display='block';
 steps.innerHTML=quiz.map((q,i)=>`<div class="step ${i===current?'active':''}"><i>${i+1}</i>${labels[i]}</div>`).join('');
 const q=quiz[current];
 qbox.innerHTML=`<div class="eyebrow">Question ${current+1} of 5</div><h3>${q.title}</h3><div class="small">${q.help}</div><div class="choices">${q.options.map(([v,l])=>`<button class="choice ${answers[q.key]===v?'selected':''}" data-v="${v}">${l}</button>`).join('')}</div><div class="quizfoot"><div class="small">Choose the answer that is closest for you.</div><div>${current?'<button class="btn alt" style="color:#1b2628;border-color:#b98a51;margin-right:8px" id="back">Back</button>':''}<button class="btn" id="next">${current===4?'See My Sauna Matches →':'Next Question →'}</button></div></div>`;
 document.querySelectorAll('.choice').forEach(b=>b.onclick=()=>{answers[q.key]=b.dataset.v;draw()});
 if(current)document.getElementById('back').onclick=()=>{current--;draw()};
 document.getElementById('next').onclick=()=>{if(!answers[q.key])return alert('Choose the option that is closest for you.');if(current<4){current++;draw()}else showResult()};
}
function saunaMatches(){
 const a=answers,models=[];
 const add=(name,brand,type,fit)=>{if(!models.some(m=>m.name===name))models.push({name,brand,type,fit})};
 const outdoor=a.location==='outdoors'||a.priority==='outdoor';
 const small=a.seating==='1-2'||a.space==='compact';
 const large=a.seating==='5plus'||a.space==='large';
 const wantsTrad=a.heat==='traditional'||a.priority==='traditional';
 const wantsIR=a.heat==='infrared'||a.priority==='daily';
 const undecided=a.heat==='compare'||a.heat==='unsure'||(!wantsTrad&&!wantsIR);
 if(outdoor){
   add('Hekla Outdoor Cabin','Hekla','Traditional Outdoor','Best fit for a dedicated backyard retreat and outdoor installation.');
   if(large) add('Hekla Larger Outdoor Cabin','Hekla','Traditional Outdoor','A better starting point when you want more seating and have room to build around it.');
   if(undecided||wantsIR) add('Hekla Infrared Sauna','Hekla','Infrared','Worth comparing if everyday convenience matters and you are still deciding on the final installation.');
 } else {
   if(wantsTrad){
     add(small?'Hekla Traditional 210X':'Hekla Traditional Sauna','Hekla','Traditional','Strong match for classic high heat, stones and the Finnish-style sauna experience.');
     if(!small) add('Hekla Larger Traditional Model','Hekla','Traditional','A stronger direction when seating capacity matters more than keeping the footprint compact.');
   }
   if(wantsIR){
     add('Hekla Infrared Sauna','Hekla','Infrared','Strong match for frequent use, gentler operating temperatures and everyday wellness.');
     add('Cal Saunas Infrared Model','Cal Saunas','Infrared','A second infrared option to compare for layout, finish, heater placement and comfort.');
   }
   if(undecided){
     add(small?'Hekla Traditional 210X':'Hekla Traditional Sauna','Hekla','Traditional','Gives you a traditional high-heat benchmark based on your seating and space answers.');
     add('Hekla Infrared Sauna','Hekla','Infrared','Gives you an infrared benchmark for easier everyday use.');
     add('Cal Saunas Infrared Model','Cal Saunas','Infrared','Adds a second brand and layout to the comparison instead of forcing an early heat-style decision.');
   }
 }
 if(models.length<3){
   add('Cal Saunas Infrared Model','Cal Saunas','Infrared','Useful comparison model for comfort, finish and day-to-day usability.');
   add('Hekla Traditional Sauna','Hekla','Traditional','Useful traditional comparison even if heat style is not fully decided.');
   add('Hekla Infrared Sauna','Hekla','Infrared','Useful infrared comparison based on your other answers.');
 }
 return models.slice(0,3);
}
function showResult(){
 const matches=saunaMatches();
 const seatLabel=answers.seating==='1-2'?'1–2 people':answers.seating==='3-4'?'3–4 people':answers.seating==='5plus'?'5+ people':'Seating still to be finalized';
 const spaceLabel=answers.space==='compact'?'Compact footprint':answers.space==='medium'?'Typical residential space':answers.space==='large'?'Flexible / larger space':'We should help measure the space';
 qbox.style.display='none';
 steps.innerHTML=labels.map(l=>`<div class="step"><i>✓</i>${l}</div>`).join('');
 result.className='result show';
 result.innerHTML=`<div class="result-kicker">Your Top Sauna Matches</div><h3>Here are the three models we’d start with.</h3><p>You do not have to know whether you want traditional or infrared yet. We used all five answers to build a practical shortlist.</p><div class="result-grid">${matches.map((m,i)=>`<div class="result-box"><b>#${i+1} — ${m.brand}</b><strong style="font-size:18px">${m.name}</strong><div class="small" style="margin:5px 0 8px">${m.type}</div>${m.fit}</div>`).join('')}</div><div class="result-box"><b>Your starting requirements</b>${seatLabel} · ${spaceLabel}</div><p style="margin-top:20px"><b>Next step:</b> We’ll confirm exact models, dimensions, electrical requirements and installation details with you before you buy.</p><div class="result-actions"><a class="btn" href="#showrooms">Visit a Showroom →</a><a class="btn alt" style="color:#1b2628;border-color:#b98a51" href="tel:+14123260361">Call 412-326-0361</a><a class="btn alt" style="color:#1b2628;border-color:#b98a51" href="mailto:sales@hottubfactoryoutlet.com?subject=My%20Sauna%20Finder%20Matches">Email Us</a></div><div style="margin-top:20px"><button class="restart" id="restart">↻ Start the Sauna Finder Again</button></div>`;
 document.getElementById('restart').onclick=()=>{current=0;answers={};draw();document.getElementById('finder').scrollIntoView({behavior:'smooth'})};
 result.scrollIntoView({behavior:'smooth',block:'center'});
}
draw();
</script>'''

s, n = re.subn(r'<script>.*?</script>', new_script, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not replace Finder script')
p.write_text(s)
