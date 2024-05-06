import time

import requests,json

url = "https://api.ez-captcha.com/createTask"

payload = json.dumps({
    "clientKey": "de15a6be209a4ab288e2008db87dfc16800359",
    "task": {
        "websiteURL": "https://store.steampowered.com/join",
        "websiteKey": "6LdIFr0ZAAAAAO3vz0O0OQrtAefzdJcWQM2TMYQH",
        "type": "ReCaptchaV2STaskProxyless",
        "s": "T1aQRQzokXvzd_liHgz5hj-Vz8lMFSQhb21WmlItZhblTnp2hiljJQKGY1whoQj04hBYjVGMW8RVApAoVzCtbbsu1ht8BF-6xcWeZbY8O5uXd7rRAihcq_mF065Q83JEvqI_TWOR2ZM1c7KjFgQv_f5bRWVYbVvYDBDFQiGXlhLP0Si1OCqmpFc2MvsNlNGZdYUhYkoKeOCXFxD8F_ujRCBB9wmcPd7QKeYuh2SyqGcHY_vicx2-s6UQkNbarVGD_0qodyuAU1BSOlSaAw"
    }
})
headers = {
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)


task = response.json().get("taskId")
print(task)
url = "https://api.ez-captcha.com/getTaskResult"

payload = json.dumps({
   "clientKey": "de15a6be209a4ab288e2008db87dfc16800359",
   "taskId": task
})
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}
time.sleep(10)
response = requests.request("POST", url, headers=headers, data=payload)
print(response.json())
print(response.json().get("solution").get("gRecaptchaResponse"))