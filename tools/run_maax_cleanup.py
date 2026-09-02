from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'specials/index.html'
s=p.read_text(encoding='utf-8')
s=re.sub(r"url\('https://[^']*hekla[^']*'\)","url('../assets/infrared-sauna.svg')",s,flags=re.I)
s=s.replace('https://rayjmorrow.github.io/PittsburghSauna.com/specials/voucher/','https://pittsburghsauna.com/specials/voucher/')
s=s.replace('https://rayjmorrow.github.io/PittsburghSauna.com/specials/','https://pittsburghsauna.com/specials/')
p.write_text(s,encoding='utf-8')
print('patched specials/index.html')
code=(ROOT/'tools/cleanup_maax_migration.py').read_text(encoding='utf-8')
exec(compile(code,str(ROOT/'tools/cleanup_maax_migration.py'),'exec'))
