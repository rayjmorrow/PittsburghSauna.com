(()=>{
  const path=location.pathname.replace(/\/+$/,'')||'/';
  const seo={
    '/':{title:'Saunas Pittsburgh PA | Traditional, Infrared & Outdoor Saunas',description:'Shop premium traditional, infrared and outdoor saunas in Pittsburgh, PA. Compare Hekla and Cal Saunas, prices, local showroom options and expert guidance from Pittsburgh Sauna.',canonical:'https://pittsburghsauna.com/'},
    '/hekla-saunas':{title:'Hekla Saunas Pittsburgh | Traditional, Infrared & Outdoor',description:'Shop Hekla traditional, infrared and outdoor saunas in Pittsburgh. Compare models, pricing and heater options from Pittsburgh Sauna.',canonical:'https://pittsburghsauna.com/hekla-saunas/'},
    '/cal-saunas':{title:'Cal Saunas Pittsburgh | Infrared & Traditional Home Saunas',description:'Explore Cal Saunas in Pittsburgh with current models, pricing and local showroom guidance from Pittsburgh Sauna by Hot Tub Factory Outlet.',canonical:'https://pittsburghsauna.com/cal-saunas/'},
    '/learning-center':{title:'Sauna Buying Guide Pittsburgh | Pittsburgh Sauna Learning Center',description:'Learn how to choose a home sauna in Pittsburgh. Compare traditional vs infrared, indoor vs outdoor, sauna sizing, heaters and planning considerations.',canonical:'https://pittsburghsauna.com/learning-center/'},
    '/specials':{title:'Sauna Specials Pittsburgh | Current Pittsburgh Sauna Savings',description:'Request current special savings on qualifying saunas and outdoor products from Pittsburgh Sauna and Hot Tub Factory Outlet.',canonical:'https://pittsburghsauna.com/specials/'},
    '/monroeville-saunas':{title:'Saunas in Monroeville, PA | Pittsburgh Sauna',description:'Shop traditional, infrared and outdoor saunas near Monroeville, PA with local showroom guidance from Pittsburgh Sauna.',canonical:'https://pittsburghsauna.com/monroeville-saunas/'},
    '/wexford-saunas':{title:'Saunas in Wexford, PA | Pittsburgh Sauna',description:'Shop traditional, infrared and outdoor saunas near Wexford, PA with local showroom guidance from Pittsburgh Sauna.',canonical:'https://pittsburghsauna.com/wexford-saunas/'}
  };
  const meta=seo[path];
  if(meta){
    document.title=meta.title;
    let d=document.querySelector('meta[name="description"]');
    if(!d){d=document.createElement('meta');d.name='description';document.head.appendChild(d)}
    d.content=meta.description;
    let c=document.querySelector('link[rel="canonical"]');
    if(!c){c=document.createElement('link');c.rel='canonical';document.head.appendChild(c)}
    c.href=meta.canonical;
  }

  if(path==='/'&&!document.querySelector('#pgh-sauna-schema')){
    const schema=document.createElement('script');schema.type='application/ld+json';schema.id='pgh-sauna-schema';schema.textContent=JSON.stringify({
      '@context':'https://schema.org','@type':'Organization','name':'Pittsburgh Sauna','alternateName':'Hot Tub Factory Outlet - Pittsburgh Sauna','url':'https://pittsburghsauna.com/','telephone':'+1-412-326-0361','email':'sales@hottubfactoryoutlet.com','areaServed':['Pittsburgh','Monroeville','Wexford','Allegheny County','Western Pennsylvania'],'brand':[{'@type':'Brand','name':'Hekla'},{'@type':'Brand','name':'Cal Saunas'}],
      'department':[
        {'@type':'Store','name':'Pittsburgh Sauna at Hot Tub Factory Outlet - Monroeville','telephone':'+1-412-326-0361','address':{'@type':'PostalAddress','streetAddress':'4680 Old William Penn Hwy','addressLocality':'Monroeville','addressRegion':'PA','postalCode':'15146','addressCountry':'US'}},
        {'@type':'Store','name':'Pittsburgh Sauna at Hot Tub Factory Outlet - Wexford','telephone':'+1-412-326-0361','address':{'@type':'PostalAddress','streetAddress':'10269 Perry Hwy','addressLocality':'Wexford','addressRegion':'PA','postalCode':'15090','addressCountry':'US'}}
      ]
    });document.head.appendChild(schema);
  }

  const GA_MEASUREMENT_ID='G-S9NT6DN10R';
  if(!GA_MEASUREMENT_ID) return;
  window.dataLayer=window.dataLayer||[];
  window.gtag=window.gtag||function(){dataLayer.push(arguments)};
  const s=document.createElement('script');
  s.async=true;
  s.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(GA_MEASUREMENT_ID);
  document.head.appendChild(s);
  gtag('js',new Date());
  gtag('config',GA_MEASUREMENT_ID,{send_page_view:true});

  const track=(name,params={})=>gtag('event',name,params);
  document.addEventListener('click',e=>{
    const a=e.target.closest('a');
    if(a){
      const href=(a.getAttribute('href')||'').trim();
      if(href.startsWith('tel:')) track('click_to_call',{link_url:href});
      if(href.startsWith('mailto:')) track('click_email',{link_url:href});
      if(href.includes('specials')) track('special_savings_click',{link_url:href});
      if(href==='#finder'||href.includes('#finder')) track('sauna_finder_open',{link_url:href});
      if(href==='#showrooms'||href.includes('#showrooms')||href.includes('monroeville-saunas')||href.includes('wexford-saunas')) track('showroom_click',{link_url:href});
    }
    const choice=e.target.closest('.choice');
    if(choice) track('sauna_finder_answer',{answer:choice.textContent.trim()});
  });
  document.addEventListener('submit',e=>{
    if(e.target && e.target.id==='savingsForm') track('generate_lead',{form_name:'Special Savings'});
  },true);
})();
