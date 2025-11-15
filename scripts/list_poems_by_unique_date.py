#!/usr/bin/env python3
"""
List all poem files from I.md to CII.md in _poemas/, extract their normalized date (using fix_poem_dates.py logic), and output the filenames in ascending date order, ensuring no repeated dates.
"""
import re
from datetime import datetime
from pathlib import Path

POEM_DIR = Path(__file__).resolve().parents[1] / "_poemas"
DATE_RE = re.compile(r"^date:\s*['\"]?(?P<date>[^'\"\n]+)['\"]?\s*$", re.IGNORECASE)

files = []
for md in sorted(POEM_DIR.glob('*.md')):
    name = md.stem
    if re.match(r'^[IVXLCDM]+$', name) or name == 'CII':
        text = md.read_text(encoding='utf-8')
        date = None
        if text.startswith('---'):
            parts = text.split('---')
            if len(parts) >= 3:
                fm = parts[1].strip('\n')
                for line in fm.splitlines():
                    m = DATE_RE.match(line)
                    if m:
                        raw = m.group('date').strip()
                        try:
                            if re.match(r'^\d{4}-\d{2}-\d{2}$', raw):
                                date = raw
                            elif re.match(r'^\d{4}$', raw):
                                date = raw + '-01-01'
                            else:
                                parsed = datetime.fromisoformat(raw)
                                date = parsed.date().isoformat()
                        except Exception:
                            pass
        if not date:
            date = datetime.fromtimestamp(md.stat().st_mtime).date().isoformat()
        files.append((date, md.name))

# Remove repeated dates, keep only the first file for each date
seen = set()
unique_files = []
for date, fname in files:
    if date not in seen:
        unique_files.append((date, fname))
        seen.add(date)

# Sort by date, then filename
unique_files.sort()

for date, fname in unique_files:
    print(f"{fname}\t{date}")
