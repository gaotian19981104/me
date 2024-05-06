import requests, json


class Solver():
    def __init__(self, data_s) -> None:
        self.data_s = data_s
        # try:
        #     with open('config.json', 'r') as f:
        #         self.api_key = self.config['capmonster']
        #         print(self.api_key)
        # except Exception as e:
        #     self.api_key = 'wtf'

    def ob_task_id(self):
        url = "https://api.ez-captcha.com/createTask"

        payload = json.dumps({
            "clientKey": "de15a6be209a4ab288e2008db87dfc16800359",
            "task": {
                "websiteURL": "https://store.steampowered.com/join",
                "websiteKey": "6LdIFr0ZAAAAAO3vz0O0OQrtAefzdJcWQM2TMYQH",
                "type": "ReCaptchaV2STaskProxyless",
                "s": self.data_s
            }
        })
        headers = {
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()


    def solve_captcha(self):
        task = self.ob_task_id().get("taskId")
        while True:
            captchaData = requests.post(f"https://api.ez-captcha.com/getTaskResult", json={
                "clientKey":  "de15a6be209a4ab288e2008db87dfc16800359",
                "taskId": task
            }, timeout=30).json()
            if "processing" in captchaData:
                pass
            else:
                try:
                    print(captchaData.get("solution").get("gRecaptchaResponse"))
                    return captchaData.get("solution").get("gRecaptchaResponse")
                except Exception:
                    # print("Failed.")
                    continue
