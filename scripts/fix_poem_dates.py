#!/usr/bin/env python3

import re
from datetime import date, timedelta
from pathlib import Path

POEM_DIR = Path(__file__).resolve().parents[1] / "_poemas"

DATE_RE = re.compile(r"^date:\s*['\"]?(?P<date>[^'\"\n]+)['\"]?\s*$", re.IGNORECASE)
ROMAN_RE = re.compile(r'^[IVXLCDM]+$')

def extract_date(text):
    if not text.startswith('---'):
        return None
    fm = text.split('---')[1].strip().splitlines()
    for line in fm:
        m = DATE_RE.match(line.strip())
        if m:
            return m.group('date').strip()
    return None

def parse_or_default_date(s, fallback_year):
    try:
        parts = s.split('-')
        if len(parts) == 3:
            y, m, d = map(int, parts)
            return date(y, m, d)
        if len(parts) == 1:
            return date(fallback_year, 1, 1)
    except:
        pass
    return date(fallback_year, 1, 1)

def set_date_in_front_matter(text, new_date):
    if not text.startswith('---'):
        return text
    parts = text.split('---')
    fm = parts[1].splitlines()
    new_fm = []
    replaced = False
    for line in fm:
        if line.strip().lower().startswith('date:'):
            new_fm.append(f"date: {new_date}")
            replaced = True
        else:
            new_fm.append(line)
    if not replaced:
        new_fm.append(f"date: {new_date}")
    return "---\n" + "\n".join(new_fm) + "\n---" + parts[2]

def roman_value(s):
    values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        v = values[ch]
        if v < prev:
            total -= v
        else:
            total += v
        prev = v
    return total

def main():
    poems = []
    for md in POEM_DIR.glob('*.md'):
        stem = md.stem
        if stem == 'CII' or ROMAN_RE.fullmatch(stem):
            poems.append((roman_value(stem), md))
    poems.sort(key=lambda x: x[0])

    # map of year -> set of used dates
    used = {}

    for _, md in poems:
        text = md.read_text(encoding='utf8')
        raw_date = extract_date(text)
        if not raw_date:
            # fallback year from file mtime
            y = md.stat().st_mtime
            fallback = date.fromtimestamp(y).year
            d = date(fallback, 1, 1)
        else:
            try:
                y = int(raw_date.split('-')[0])
            except:
                y = date.fromtimestamp(md.stat().st_mtime).year

            d = parse_or_default_date(raw_date, y)

        # ensure year key exists
        if y not in used:
            used[y] = set()

        new_day = d
        while new_day in used[y]:
            new_day += timedelta(days=1)

        used[y].add(new_day)

        new_iso = new_day.isoformat()
        updated = set_date_in_front_matter(text, new_iso)
        md.write_text(updated, encoding='utf8')

        print(f"{md.name} -> {new_iso}")

if __name__ == "__main__":
    main()
