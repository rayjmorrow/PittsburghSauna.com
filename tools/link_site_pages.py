from pathlib import Path

files = [
    Path('index.html'),
    Path('hekla-saunas/index.html'),
    Path('cal-saunas/index.html'),
    Path('learning-center/index.html'),
]

for p in files:
    if not p.exists():
        continue

    s = p.read_text()
    is_home = p.as_posix() == 'index.html'

    if is_home:
        s = s.replace('href="#cal">Cal Saunas</a>', 'href="cal-saunas/">Cal Saunas</a>')
        s = s.replace('href="#learn">Learning Center</a>', 'href="learning-center/">Learning Center</a>')
        s = s.replace('<a class="btn alt" href="#finder">Explore Cal Saunas →</a>', '<a class="btn alt" href="cal-saunas/">Explore Cal Saunas →</a>')
        showroom = '<a href="#showrooms">Showrooms</a>'
        specials = '<a href="specials/">Specials</a>'
    else:
        s = s.replace('href="../#cal">Cal Saunas</a>', 'href="../cal-saunas/">Cal Saunas</a>')
        s = s.replace('href="../#learn">Learning Center</a>', 'href="../learning-center/">Learning Center</a>')
        s = s.replace('href="../#hekla">Hekla</a>', 'href="../hekla-saunas/">Hekla</a>')
        showroom = '<a href="../#showrooms">Showrooms</a>'
        specials = '<a href="../specials/">Specials</a>'

    if specials not in s:
        if showroom in s:
            s = s.replace(showroom, showroom + specials, 1)
        else:
            s = s.replace('</nav><div class="navright">', showroom + specials + '</nav><div class="navright">', 1)

    p.write_text(s)
