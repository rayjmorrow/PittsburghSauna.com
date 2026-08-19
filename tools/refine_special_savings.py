from pathlib import Path
import re

CAMPAIGN_END = "September 6, 2026"

specials = Path('specials/index.html')
if not specials.exists():
    raise SystemExit('specials/index.html not found')

# Rename navigation everywhere to "Special Savings".
for p in Path('.').rglob('index.html'):
    try:
        text = p.read_text()
    except Exception:
        continue
    text = re.sub(r'>Specials<', '>Special Savings<', text)
    p.write_text(text)

s = specials.read_text()

# Fixed-date campaign hero. We reveal the deadline, but not the offer amount or voucher type.
hero = f'''<section class="hero"><div class="wrap"><div class="hero-copy"><div class="eyebrow">Limited-Time Pittsburgh Sauna Offer</div><h1>SPECIAL SAVINGS</h1><h2>Our current sale ends {CAMPAIGN_END}.</h2><p>Answer a few quick questions and we’ll email you a personalized certificate with the special savings available for your project.</p><div class="hero-points"><span>🔒 Exclusive savings</span><span>✉ Personalized for you</span><span>★ Sale ends {CAMPAIGN_END}</span></div><a class="btn" href="#questionnaire">Get My Special Offer →</a></div></div></section>'''
s = re.sub(r'<section class="hero">.*?</section><section class="strip">', hero + '<section class="strip">', s, count=1, flags=re.S)

# Keep the actual offer private until the questionnaire is submitted.
s = s.replace('Hot Tub Factory Outlet VIP Savings', 'Special Savings')
s = s.replace('Duck Bucks savings certificate', 'personalized savings certificate')
s = s.replace('Duck Bucks certificate', 'savings certificate')
s = s.replace('VIP Savings Questionnaire', 'Special Savings Questionnaire')
s = s.replace('Your savings are personal.', 'Your offer is personal.')
s = s.replace('We personalize your voucher', 'We personalize your offer')
s = s.replace('Your certificate will be issued in your name and will expire 18 days after the date it is emailed to you.', f'Your personalized certificate will show the current sale end date: {CAMPAIGN_END}.')
s = s.replace('Each certificate expires 18 days after it is emailed.', f'The current special savings event ends {CAMPAIGN_END}.')
s = s.replace('The expiration date will be 18 days from the email date.', f'Your certificate will be valid through {CAMPAIGN_END}.')
s = s.replace('Your certificate is emailed to you and remains valid for 18 days from the send date.', f'Your certificate is emailed directly to you and is valid through {CAMPAIGN_END}.')
s = s.replace('Your certificate will include its own valid-through date.', f'Your certificate will be valid through {CAMPAIGN_END}.')
s = s.replace('Your certificate will include its valid-through date.', f'Your certificate will be valid through {CAMPAIGN_END}.')
s = s.replace('Your certificate is emailed directly to you with its valid-through date printed on it.', f'Your certificate is emailed directly to you with “Valid Through {CAMPAIGN_END}” printed on it.')
s = s.replace('Use it within 18 days', f'Use it by {CAMPAIGN_END}')
s = s.replace('Expires in 18 days', f'Ends {CAMPAIGN_END}')
s = s.replace('Valid-through date included', f'Ends {CAMPAIGN_END}')
s = re.sub(r'18 days[^<.]*[.]?', '', s, flags=re.I)
s = s.replace('Duck Bucks have no cash value and are valid only on qualifying purchases. One Duck Bucks offer per purchase. ', '')
s = s.replace('Final voucher terms control.', 'Final offer terms control.')

# Make the public explanatory strip describe a real campaign deadline, not a rolling expiration.
s = re.sub(r'<div class="stripitem"><b>TIME-SENSITIVE</b><span>.*?</span></div>', f'<div class="stripitem"><b>LIMITED-TIME SALE</b><span>Current special savings end {CAMPAIGN_END}.</span></div>', s, flags=re.S)

# Hide internal implementation/CRM status from customers.
s = re.sub(r'<div class="mini-status">.*?</div>', '', s, flags=re.S)

# Premium visual treatment matching the approved direction.
if 'id="special-savings-refine"' not in s:
    overrides = '''<style id="special-savings-refine">
.links .special{color:#e0a83d!important;font-weight:900!important}
.hero{background:linear-gradient(90deg,rgba(0,0,0,.92) 0%,rgba(0,0,0,.82) 38%,rgba(0,0,0,.28) 70%),url('https://www.spa-whirlpoolshop.de/cdn/shop/files/traditionelle-finnish-sauna-hekla-210x-indoor-fur-5-personen-hochwertiger-fur-garten-terrasse-new-wave-spa-wellness-1361462.jpg?v=1766056163&width=1600') center/cover!important;padding:76px 0 82px!important;text-align:left!important;min-height:520px;display:flex;align-items:center}.hero .wrap{display:block!important}.hero-copy{max-width:690px}.hero h1{font-family:Inter,system-ui,sans-serif!important;font-size:72px!important;font-weight:900!important;letter-spacing:.02em!important;color:#f0c276!important;margin:8px 0 10px!important}.hero h2{font-family:Inter,system-ui,sans-serif!important;font-size:28px!important;text-transform:uppercase;letter-spacing:.03em;margin:0 0 18px!important}.hero p{font-size:20px!important;line-height:1.65!important;margin:0 0 22px!important;max-width:650px!important}.hero-points{display:flex;gap:28px;flex-wrap:wrap;margin:24px 0 28px;color:#f0c276;font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:.04em}.hero-points span{display:inline-flex;align-items:center;gap:7px}.section{background:#fbf8f2!important}.head{text-align:center!important;margin-left:auto!important;margin-right:auto!important}.form-shell{grid-template-columns:1fr!important;max-width:1040px;margin:auto}.side-card{display:none!important}.form-card{background:#fffaf2!important;border-color:#ded5c8!important;box-shadow:0 12px 36px rgba(24,34,35,.08)!important}.submit-row .btn{background:#c58a22!important;border-color:#c58a22!important;color:#fff!important;font-size:14px!important;min-height:56px!important}.strip{background:#f3eee6!important}.fineprint{background:#f3eee6!important}.how{background:#fffaf2!important;color:#162326!important}.howitem{border-color:#ded5c8!important;background:#fff!important}.howitem p{color:#596164!important}.num{background:#c58a22!important;color:#fff!important}@media(max-width:650px){.hero h1{font-size:46px!important}.hero h2{font-size:22px!important}.hero p{font-size:17px!important}.hero-points{gap:14px;display:grid}}
</style>'''
    s = s.replace('</head>', overrides + '</head>')

specials.write_text(s)
