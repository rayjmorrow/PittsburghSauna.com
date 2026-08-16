from pathlib import Path

files = [Path('index.html'), Path('hekla-saunas/index.html'), Path('cal-saunas/index.html')]
for p in files:
    if not p.exists():
        continue
    s = p.read_text()
    if p.as_posix() == 'index.html':
        s = s.replace('href="#cal">Cal Saunas</a>', 'href="cal-saunas/">Cal Saunas</a>')
        s = s.replace('href="#learn">Learning Center</a>', 'href="learning-center/">Learning Center</a>')
        s = s.replace('<a class="btn alt" href="#finder">Explore Cal Saunas →</a>', '<a class="btn alt" href="cal-saunas/">Explore Cal Saunas →</a>')
    else:
        s = s.replace('href="../#cal">Cal Saunas</a>', 'href="../cal-saunas/">Cal Saunas</a>')
        s = s.replace('href="../#learn">Learning Center</a>', 'href="../learning-center/">Learning Center</a>')
        s = s.replace('href="../#hekla">Hekla</a>', 'href="../hekla-saunas/">Hekla</a>')
    p.write_text(s)
