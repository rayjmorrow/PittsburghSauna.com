(()=>{
  const GA_MEASUREMENT_ID=''; // Add GA4 Measurement ID, e.g. G-XXXXXXXXXX
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
      if(href==='#showrooms'||href.includes('#showrooms')) track('showroom_click',{link_url:href});
    }
    const choice=e.target.closest('.choice');
    if(choice) track('sauna_finder_answer',{answer:choice.textContent.trim()});
  });

  document.addEventListener('submit',e=>{
    if(e.target && e.target.id==='savingsForm'){
      track('generate_lead',{form_name:'Special Savings'});
    }
  },true);
})();
