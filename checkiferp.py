import requests
import re
import time

inappropriate_keywords = ['defaults', 'owned', 'bio', 'studio', 'icebunny', 'snowbunny', 'bull', 'bio in following', 'studio only', 'wallets', 'wallet', 'bulls', 'dice', 'dizzy', '💿', 'donate to add', 'follow to add']

bundle_id = 154461070616457
accessory_id = 104554419958896
favorite_game_id = 18432220092
group_ids = [126992943, 226283782, 16772560, 1094217708, 35216426, 557719733, 1029384]

inappropriate_users = []
output_log_file = "output_log.txt"
inappropriate_users_file = "inappropriate_users.txt"

API_KEY = "studio api key needed to check group members and api, generate at https://create.roblox.com/dashboard/credentials?activeTab=ApiKeysTab"
ROBLOSECURITY = "roblosecurity goes here to properly check friends idk if its needed"

headers_cookie = {'Cookie': f'.ROBLOSECURITY={ROBLOSECURITY}'}
headers_cloud  = {"x-api-key": API_KEY}

def fetch(url, use_cookie=True, retries=5, delay=5):
    headers = headers_cookie if use_cookie else headers_cloud
    for _ in range(retries):
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                return r
        except:
            pass
        time.sleep(delay)
    return None

def log(msg):
    with open(output_log_file, 'a', encoding='utf-8') as f:
        f.write(msg + '\n')
    print(msg)

def check_profile(uid):
    r = fetch(f"https://users.roblox.com/v1/users/{uid}")
    if not r: return
    d = r.json()
    name = d.get('name', '')
    desc = d.get('description', '')
    if any(w.lower() in name.lower() for w in inappropriate_keywords):
        log(f"Bad username: {name} ({uid})")
    if any(w.lower() in desc.lower() for w in inappropriate_keywords):
        log(f"Bad desc: {name} ({uid})")

def check_avatar(uid):
    r = fetch(f"https://avatar.roblox.com/v1/users/{uid}/avatar")
    if not r: return
    d = r.json()
    if bundle_id in d.get('bundleIds', []):
        log(f"Bundle match: {uid}")
        inappropriate_users.append(uid)
    if accessory_id in d.get('assetIds', []):
        log(f"Accessory match: {uid}")
        inappropriate_users.append(uid)

def check_favorite(uid):
    r = fetch(f"https://games.roblox.com/v2/users/{uid}/favorite/games")
    if not r: return
    ids = [g['id'] for g in r.json().get('data', [])]
    if favorite_game_id in ids:
        log(f"Favorite match: {uid}")
        inappropriate_users.append(uid)

def check_groups(uid):
    url = f"https://groups.roblox.com/v1/users/{uid}/groups/roles"
    r = fetch(url, use_cookie=False)
    if not r or r.status_code != 200:
        return
    data = r.json().get('data', [])
    for gid in group_ids:
        if any(g['group']['id'] == gid for g in data):
            log(f"Group match {gid}: {uid}")
            inappropriate_users.append(uid)

def get_uid(link):
    m = re.search(r'/users/(\d+)', link)
    return m.group(1) if m else None

def read_links(path):
    with open(path, encoding='utf-8') as f:
        return [l.strip() for l in f if l.strip()]

def save_bad():
    with open(inappropriate_users_file, 'w', encoding='utf-8') as f:
        for uid in inappropriate_users:
            f.write(f"https://roblox.com/users/{uid}\n")

links = read_links(r'path to user id files go here example: C:\Users\person\Downloads')

for link in links:
    uid = get_uid(link)
    if uid:
        print(f"Checking {uid}")
        check_profile(uid)
        check_avatar(uid)
        check_favorite(uid)
        check_groups(uid)

save_bad()
log(f"Total: {len(inappropriate_users)}")