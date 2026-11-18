"""Find the fastest and longest subtitle cues without uploading the subtitle file."""
import re
from pathlib import Path
from serve import page
INTERVAL=5
STAMP=r"(\d{1,3}):(\d{2}):(\d{2})[,.](\d{3})"
def stamp(parts):
    h,m,s,ms=map(int,parts);return h*3600+m*60+s+ms/1000
def cues(path):
    rows=[]
    text=Path(path).expanduser().read_text(encoding="utf-8-sig").replace("\r","")
    for block in re.split(r"\n\s*\n",text.strip()):
        lines=block.splitlines();j=next((i for i,line in enumerate(lines) if "-->" in line),None)
        if j is None:continue
        match=re.search(STAMP+r"\s*-->\s*"+STAMP,lines[j])
        if not match:continue
        start,end=stamp(match.groups()[:4]),stamp(match.groups()[4:])
        phrase=re.sub("<[^>]+>",""," ".join(lines[j+1:])).strip()
        if end>start and phrase:rows.append((start,end,phrase))
    return rows
def snapshot(o,m):
    data=cues(o["file"])
    if not data:raise ValueError("No valid timed SRT cues")
    limit=float(o.get("max_cps",20));ranked=sorted(data,key=lambda r:len(r[2])/(r[1]-r[0]),reverse=True)
    over=[r for r in ranked if len(r[2])/(r[1]-r[0])>limit]
    pages=[page("FAST CAPTIONS",len(over),f"Over {limit:g} chars/sec",f"Of {len(data)} timed cues")]
    for a,b,phrase in ranked[:15]:
        minute,sec=divmod(int(a),60)
        pages.append(page("AT "+f"{minute:02}:{sec:02}",f"{len(phrase)/(b-a):.1f}c/s",phrase[:26],f"{len(phrase)} chars / {b-a:.2f}s"))
    a,b,phrase=max(data,key=lambda r:len(r[2]));pages.append(page("LONGEST CUE",len(phrase),f"At {a:.2f} s",phrase[:26]))
    return dict(state="SRT timing review",key=str(len(over)),pages=pages)
