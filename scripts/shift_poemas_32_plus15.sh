#!/usr/bin/env bash
set -euo pipefail

# This script updates files in _poemas:
# - For every file named with a Roman numeral (e.g. XXXII.md) convert to integer.
# - If the integer >= 32, add 15, produce a new Roman numeral.
# - Update front-matter title: and permalink: to use the new Roman numeral.
# - Backup original file to filename.bak and rename the file to NEWROMAN.md

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
POEM_DIR="$ROOT_DIR/_poemas"

if [ ! -d "$POEM_DIR" ]; then
  echo "_poemas directory not found at $POEM_DIR" >&2
  exit 1
fi

export POEM_DIR

python3 - <<'PY'
import os, re, sys
from pathlib import Path

poem_dir = Path(os.environ['POEM_DIR'])

# roman->int and int->roman helpers
vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
syms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

def roman_to_int(s):
    s = s.upper()
    i = 0
    n = 0
    mapping = dict(zip(syms, vals))
    # greedy parse
    for sym,val in zip(syms, vals):
        while s[i:i+len(sym)] == sym:
            n += val
            i += len(sym)
            if i >= len(s): break
    # Fallback: more robust parser
    # Use left-to-right
    total = 0
    prev = 0
    for ch in s[::-1]:
        v = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(ch,0)
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total


def int_to_roman(num):
    res = ''
    n = num
    for v,sym in zip(vals, syms):
        while n >= v:
            res += sym
            n -= v
    return res

# Match roman filename (only letters I,V,X,L,C,D,M and optional other chars?)
roman_re = re.compile(r"^([IVXLCDM]+)\.md$", re.I)

changed = []
for p in sorted(poem_dir.iterdir()):
    if not p.is_file():
        continue
    m = roman_re.match(p.name)
    if not m:
        continue
    roman = m.group(1).upper()
    num = roman_to_int(roman)
    if num >= 32:
        newnum = num + 15
        newroman = int_to_roman(newnum)
        newname = f"{newroman}.md"
        target = p.with_name(newname)
        if target.exists():
            print(f"Target exists, skipping {p.name} -> {newname}", file=sys.stderr)
            continue
        text = p.read_text(encoding='utf-8')
        orig_text = text
        # Update title: line starting with title:
        text = re.sub(r'^(title:\s*)(["\"]?)([IVXLCDM]+)(["\"]?)', lambda mm: mm.group(1)+mm.group(2)+newroman+mm.group(4), text, flags=re.M)
        # Update permalink: /poemas/XXXII/ -> newroman
        text = re.sub(r'^(permalink:\s*)(["\']?)/poemas/[A-Za-z0-9_\-]+/(["\']?)', lambda mm: mm.group(1)+mm.group(2)+f"/poemas/{newroman}/"+mm.group(3), text, flags=re.M)
    # Backup into the backups directory inside POEM_DIR
    bak_dir = Path(os.environ['POEM_DIR']) / 'backups'
    bak_dir.mkdir(parents=True, exist_ok=True)
    bak = bak_dir / (p.name + '.bak')
    p.rename(bak)
    target.write_text(text, encoding='utf-8')
        changed.append((p.name, newname))
        print(f"Renamed {p.name} -> {newname}")

if not changed:
    print('No files changed')
else:
    print('Changed files:')
    for a,b in changed:
        print('  ', a, '->', b)

PY

echo "Done."
