from resources.account import Account
from utils.logger import Logger
from itertools import cycle
import random, threading, json, os
count = 0
class Main():
    print("hello")
    def __init__(self) -> None:
        try:
            with open('config.json',encoding='utf-8') as f:
                self.config = json.loads(f.read())
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
                self.config = default_config

    def main(self):
        emails = cycle(open(self.config['emails_file']).read().splitlines())
        while True:
            global count
            try:
                count += 1
                email = next(emails)
                account_mail = email.split(":")[0]
                account_pass = email.split(":")[1]
                if os.path.exists(self.config['proxy']):
                    proxy = random.choice(open(self.config['proxy']).read().splitlines())
                else:
                    proxy = self.config['proxy']
                username, password = Account(proxy, account_mail, account_pass).create_account()
                with open(self.config['save_file'], 'a+') as f:
                    f.write(f"{username}:{password}\n")
                    Logger("Generated account", f"{username}:{password} [{count}]").log_default()
            except Exception as e:
                Logger(f'Failed to generate account [{count}]', e).log_error()

if __name__ == '__main__':
    INSTANCE =  Main()
    INSTANCE.main()
    # 这行代码是一个条件表达式，用于确定要启动多少个线程。让我解释一下它的逻辑：
    # inp = int(input("[!] 你想开启多少个线程: ")) if INSTANCE.config['threads'] == 0 else INSTANCE.config[
    #     'threads']
    # # 日志
    # Logger('线程', f"开启 {inp} 个线程").log_default()
    # for _ in range(int(inp)):
    #     threading.Thread(target=INSTANCE.main).start()