from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

PRO5='https://pushpedalpull.com/cdn/shop/files/SWPRO52Predlight.webp?v=1775238349'
PRO5_LARGE='https://pushpedalpull.com/cdn/shop/files/SW4predlightcopy2_1024x1024_1_1812308b-9833-4c1e-a3eb-8b38ed99ac8e.webp?v=1775238392'
PRO10='https://wellness-mexico.com.mx/wp-content/uploads/2025/09/SaunaWellness_PRO_10_4P_RED_Front_copy_2.png'

# Homepage
p=ROOT/'index.html'; s=p.read_text(encoding='utf-8')
s=s.replace("url('assets/hero-sauna.svg') center/cover", f"url('{PRO10}') 78% center/contain no-repeat,linear-gradient(90deg,#0e1719,#172123)")
s=s.replace(".traditional{background-image:url('assets/traditional-sauna.svg');background-color:#6d4b32}", ".traditional{background-image:url('assets/site-images/Solara-Outdoor-product-img-2-a97e1336a8.webp');background-color:#6d4b32}")
s=s.replace(".infrared{background-image:url('assets/infrared-sauna.svg');background-color:#5b3832}", f".infrared{{background-image:url('{PRO5}');background-color:#5b3832;background-size:cover;background-position:center}}")
s=s.replace(".outdoor{background-image:url('assets/outdoor-sauna.svg');background-color:#394b3d}", ".outdoor{background-image:url('assets/site-images/Solara-Outdoor-product-img-2-a97e1336a8.webp');background-color:#394b3d;background-size:cover;background-position:center}")
s=s.replace(".maax{background-image:url('assets/infrared-sauna.svg');background-color:#24383b}", f".maax{{background-image:url('{PRO10}');background-color:#24383b;background-size:cover;background-position:center}}")
p.write_text(s,encoding='utf-8')
print('updated index.html')

# MAAX page: real product photography + outdoor section
p=ROOT/'maax-saunas/index.html'; s=p.read_text(encoding='utf-8')
s=s.replace(".hero{background:linear-gradient(110deg,#101a1d 0%,#172629 60%,#314246 100%);color:#fff;min-height:560px;display:flex;align-items:center}", f".hero{{background:linear-gradient(90deg,rgba(14,23,25,.97),rgba(14,23,25,.80) 48%,rgba(14,23,25,.16)),url('{PRO10}') 82% center/contain no-repeat,#172123;color:#fff;min-height:600px;display:flex;align-items:center}}")
s=s.replace(".hero-art{display:grid;place-items:center;padding:30px}.hero-art img{width:min(360px,100%);filter:invert(1);opacity:.9}", ".hero-art{min-height:420px}.hero-art img{display:none}")
s=s.replace('<div class="hero-art"><img src="../assets/infrared-sauna.svg" alt="Infrared sauna illustration"></div>','<div class="hero-art" aria-hidden="true"></div>')
s=s.replace('.model{background:#fff;border:1px solid var(--line);padding:28px}', '.model{background:#fff;border:1px solid var(--line);overflow:hidden}.model-photo{height:270px;background:#eee center/contain no-repeat}.model-body{padding:28px}')
repls={
'<article class="model"><div class="meta">SaunaWellness PRO 5 · 1 Person</div>':f'<article class="model"><div class="model-photo" style="background-image:url(\'{PRO5_LARGE}\')"></div><div class="model-body"><div class="meta">SaunaWellness PRO 5 · 1 Person</div>',
'<article class="model"><div class="meta">SaunaWellness PRO 5 · 2 Person</div>':f'</div></article><article class="model"><div class="model-photo" style="background-image:url(\'{PRO5}\')"></div><div class="model-body"><div class="meta">SaunaWellness PRO 5 · 2 Person</div>',
'<article class="model"><div class="meta">SaunaWellness PRO 10 · 3 Person</div>':f'</div></article><article class="model"><div class="model-photo" style="background-image:url(\'{PRO10}\')"></div><div class="model-body"><div class="meta">SaunaWellness PRO 10 · 3 Person</div>',
'<article class="model"><div class="meta">SaunaWellness PRO 10 · 4 Person</div>':f'</div></article><article class="model"><div class="model-photo" style="background-image:url(\'{PRO10}\')"></div><div class="model-body"><div class="meta">SaunaWellness PRO 10 · 4 Person</div>'
}
for a,b in repls.items(): s=s.replace(a,b)
# close last model-body if needed
s=s.replace('<b>Indoor use</b></div></article></div><div class="note">','<b>Indoor use</b></div></div></article></div><div class="note">',1)
# add outdoor section before features
marker='<section class="section features">'
outdoor='''<section class="section" id="outdoor"><div class="wrap"><div class="eyebrow">MAAX SX Outdoor Series</div><h2>MAAX goes outside, too.</h2><p class="sub">The MAAX SX Outdoor Series extends the lineup into weather-ready backyard installations, with 2-, 4- and 6-person options, full-spectrum infrared, Canadian Red Cedar interiors, Himalayan salt features and outdoor-rated construction.</p><div class="models"><article class="model"><div class="model-photo" style="background-image:url('../assets/site-images/Solara-Outdoor-product-img-2-a97e1336a8.webp');background-size:cover"></div><div class="model-body"><div class="meta">SX Outdoor Series</div><h3>Backyard wellness.</h3><p>Outdoor MAAX models are designed specifically for exterior installation. We’ll confirm the exact SX model, electrical requirements, site preparation and current availability before you order.</p><div class="specs"><b>Sizes:</b> 2, 4 and 6 person options<br><b>Category:</b> Outdoor full-spectrum infrared<br><b>Planning:</b> 220V power and a suitable prepared site</div></div></article><article class="model"><div class="model-photo" style="background-image:url('''+PRO10+''')"></div><div class="model-body"><div class="meta">Indoor + Outdoor MAAX</div><h3>One brand. More ways to use it.</h3><p>MAAX now gives Pittsburgh Sauna a much broader story: compact indoor infrared, premium cedar full-spectrum models and dedicated outdoor sauna options.</p><div class="specs"><b>Ask us about:</b> SR, SL / SaunaWellness and SX Outdoor availability.</div></div></article></div></div></section>'''
s=s.replace(marker,outdoor+marker)
p.write_text(s,encoding='utf-8')
print('updated maax-saunas/index.html')

# Specials hero
p=ROOT/'specials/index.html'; s=p.read_text(encoding='utf-8')
s=s.replace("url('../assets/infrared-sauna.svg') center/cover", f"url('{PRO10}') 82% center/contain no-repeat,#111")
p.write_text(s,encoding='utf-8')
print('updated specials/index.html')
