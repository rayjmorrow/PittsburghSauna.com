from pathlib import Path
import re

specials = Path('specials/index.html')
if not specials.exists():
    raise SystemExit('specials/index.html not found')

s = specials.read_text()

# Rename navigation everywhere to "Special Savings".
for p in Path('.').rglob('index.html'):
    try:
        text = p.read_text()
    except Exception:
        continue
    text = re.sub(r'>(Specials)<', '>Special Savings<', text)
    p.write_text(text)

s = specials.read_text()

# Remove the visible voucher preview and any Duck Bucks reveal from the landing experience.
hero = '''<section class="hero"><div class="wrap"><div class="hero-copy"><div class="eyebrow">Exclusive Offer · Just For You</div><h1>SPECIAL SAVINGS</h1><h2>Tell us a little about yourself.</h2><p>Answer a few quick questions and we’ll email you a personalized certificate with a special offer, good for 18 days from the date it’s sent.</p><div class="hero-points"><span>🔒 Exclusive invitation only</span><span>✉ Emailed to you</span><span>▣ Expires in 18 days</span></div><a class="btn" href="#questionnaire">Get My Special Offer →</a></div></div></section>'''
s = re.sub(r'<section class="hero">.*?</section><section class="strip">', hero + '<section class="strip">', s, count=1, flags=re.S)

# Strip teaser language that reveals the certificate type/value before submission.
s = s.replace('Hot Tub Factory Outlet VIP Savings', 'Special Savings')
s = s.replace('Duck Bucks savings certificate', 'personalized savings certificate')
s = s.replace('Duck Bucks certificate', 'savings certificate')
s = s.replace('Duck Bucks have no cash value and are valid only on qualifying purchases. One Duck Bucks offer per purchase. ', '')
s = s.replace('Final voucher terms control.', 'Final offer terms control.')
s = s.replace('VIP Savings Questionnaire', 'Special Savings Questionnaire')
s = s.replace('Your savings are personal.', 'Your offer is personal.')
s = s.replace('We personalize your voucher', 'We personalize your offer')

# Hide internal implementation/CRM status from customers.
s = re.sub(r'<div class="mini-status">.*?</div>', '', s, flags=re.S)

# Make the visual treatment match the approved premium direction: dark sauna hero, gold accents, cream form.
overrides = '''<style id="special-savings-refine">
.links .special{color:#e0a83d!important;font-weight:900!important}
.hero{background:linear-gradient(90deg,rgba(0,0,0,.92) 0%,rgba(0,0,0,.82) 38%,rgba(0,0,0,.28) 70%),url('https://www.spa-whirlpoolshop.de/cdn/shop/files/traditionelle-finnish-sauna-hekla-210x-indoor-fur-5-personen-hochwertiger-fur-garten-terrasse-new-wave-spa-wellness-1361462.jpg?v=1766056163&width=1600') center/cover!important;padding:76px 0 82px!important;text-align:left!important;min-height:520px;display:flex;align-items:center}.hero .wrap{display:block!important}.hero-copy{max-width:690px}.hero h1{font-family:Inter,system-ui,sans-serif!important;font-size:72px!important;font-weight:900!important;letter-spacing:.02em!important;color:#f0c276!important;margin:8px 0 10px!important}.hero h2{font-family:Inter,system-ui,sans-serif!important;font-size:28px!important;text-transform:uppercase;letter-spacing:.03em;margin:0 0 18px!important}.hero p{font-size:20px!important;line-height:1.65!important;margin:0 0 22px!important;max-width:650px!important}.hero-points{display:flex;gap:28px;flex-wrap:wrap;margin:24px 0 28px;color:#f0c276;font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:.04em}.hero-points span{display:inline-flex;align-items:center;gap:7px}.section{background:#fbf8f2!important}.head{text-align:center!important;margin-left:auto!important;margin-right:auto!important}.form-shell{grid-template-columns:1fr!important;max-width:1040px;margin:auto}.side-card{display:none!important}.form-card{background:#fffaf2!important;border-color:#ded5c8!important;box-shadow:0 12px 36px rgba(24,34,35,.08)!important}.submit-row .btn{background:#c58a22!important;border-color:#c58a22!important;color:#fff!important;font-size:14px!important;min-height:56px!important}.strip{background:#f3eee6!important}.fineprint{background:#f3eee6!important}.how{background:#fffaf2!important;color:#162326!important}.howitem{border-color:#ded5c8!important;background:#fff!important}.howitem p{color:#596164!important}.num{background:#c58a22!important;color:#fff!important}@media(max-width:650px){.hero h1{font-size:46px!important}.hero h2{font-size:22px!important}.hero p{font-size:17px!important}.hero-points{gap:14px;display:grid}}
</style>'''
s = s.replace('</head>', overrides + '</head>')

specials.write_text(s)
