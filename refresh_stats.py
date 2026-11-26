#!/usr/bin/env python3
"""Atualiza estrelas, último commit e licença de cada repo em data/repos.json via GitHub API (gh CLI)."""
import json, subprocess, time, sys
P = 'data/repos.json'
d = json.load(open(P))
repos = d['repos']
for i in range(0, len(repos), 6):
    chunk = repos[i:i+6]
    q = ' '.join(f"repo:{r['repo']}" for r in chunk)
    out = subprocess.run(['gh','api','-X','GET','search/repositories','-f',f'q={q}','-f','per_page=10',
        '--jq','.items[]|[.full_name,.stargazers_count,.pushed_at[0:10],(.license.spdx_id//"none"),.archived]|@tsv'],
        capture_output=True, text=True).stdout
    got = {l.split('\t')[0].lower(): l.split('\t') for l in out.splitlines() if l}
    for r in chunk:
        v = got.get(r['repo'].lower())
        if not v: print('não encontrado:', r['repo'], file=sys.stderr); continue
        r['stars'], r['pushed'], r['license'] = int(v[1]), v[2], v[3]
        if v[4] == 'true': r['note'] = 'ARQUIVADO pelo mantenedor. ' + r.get('note','')
    time.sleep(2.5)
import datetime; d['generated'] = datetime.date.today().isoformat()
json.dump(d, open(P,'w'), ensure_ascii=False, indent=1)
print('ok', len(repos))
