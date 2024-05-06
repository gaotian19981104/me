import json
try:
    with open('config.json', 'r') as f:
       config = json.loads(f.read())
except FileNotFoundError:
    with open('config.json', 'w') as f:
        default_config = {
            'proxy': 'PROXIES_FILE_OR_PROXY_HERE',
            'proxy_type': 'http',
            'threads': 0,
            'capmonster': 'API_KEY_HERE',
            'save_file': "accounts.txt",
            'emails_file': 'emails.txt'
        }
        f.write(json.dumps(default_config, indent=4))
        config = default_config