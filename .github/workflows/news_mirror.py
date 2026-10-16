# -*- coding: utf-8 -*-
"""Wild Rift news mirror: official news (__NEXT_DATA__) + YouTube playlist RSS -> news-cache.json"""
import urllib.request, json, re, datetime, sys

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=timeout)

# 1. Official news
official = []
try:
    html = fetch('https://wildrift.leagueoflegends.com/en-gb/news/').read().decode('utf-8', 'replace')
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if m:
        nd = json.loads(m.group(1))
        items = nd['props']['pageProps']['page']['blades'][2]['items']
        for it in items:
            title = str(it.get('title') or '')
            if not title:
                continue
            cat = str((it.get('category') or {}).get('title') or '')
            desc = it.get('description') or ''
            if isinstance(desc, dict):
                desc = desc.get('body') or ''
            desc = str(desc)[:200]
            pub = str(it.get('publishedAt') or '')[:10]
            act = it.get('action') or {}
            url = ''
            if act.get('type') == 'weblink':
                url = (act.get('payload') or {}).get('url') or ''
            elif act.get('type') == 'url':
                url = act.get('value') or act.get('href') or ''
            if url and url.startswith('/'):
                url = 'https://wildrift.leagueoflegends.com' + url
            img = ''
            try:
                img = it['imageMedia'].get('url') or ''
            except Exception:
                pass
            if url:
                official.append({'title': title, 'url': url, 'category': cat, 'published': pub, 'image': img, 'description': desc})
    print('official:', len(official), flush=True)
except Exception as e:
    print('official ERR:', repr(e), flush=True)

# 2. YouTube playlist RSS
youtube = []
try:
    xml = fetch('https://www.youtube.com/feeds/videos.xml?playlist_id=PLuiVQJJnpdDF4azH7o0oWi80VtymwOHKs').read().decode('utf-8', 'replace')
    entries = re.findall(r'<entry>(.*?)</entry>', xml, re.S)
    for en in entries:
        mt = re.search(r'<title>([^<]*)</title>', en)
        mv = re.search(r'<yt:videoId>([^<]+)</yt:videoId>', en)
        mp = re.search(r'<published>([^<]+)</published>', en)
        if mt and mv:
            vid = mv.group(1)
            youtube.append({'title': mt.group(1), 'videoId': vid, 'url': 'https://www.youtube.com/watch?v=' + vid,
                            'published': (mp.group(1)[:10] if mp else ''), 'thumbnail': 'https://i.ytimg.com/vi/' + vid + '/hqdefault.jpg'})
    print('youtube:', len(youtube), flush=True)
except Exception as e:
    print('youtube ERR:', repr(e), flush=True)

out = {'fetched_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), 'official': official, 'youtube': youtube}
with open('news-cache.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print('written news-cache.json len:', len(json.dumps(out, ensure_ascii=False)), flush=True)
