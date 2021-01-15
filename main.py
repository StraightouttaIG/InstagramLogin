import requests
import uuid


def get_pre_login_cookie():
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get("https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup/", headers=headers)
    cookie = response.cookies["csrftoken"]
    if response.status_code == 200:
        login(cookie)
    else:
        print(response.text)


def login(cookie):
    username = input("Username: ")
    password = input("Password: ")
    headers = {"User-Agent": "Mozilla/5.0 Instagram 170.2.0.30.474 Android", "Cookie": f"csrftoken={cookie}"}
    payload = {"username": username, "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:0:{password}",
               "device_id": uuid.uuid4()}
    response = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=headers, data=payload)
    if response.status_code == 200:
        print(f"Account Cookie: {response.cookies.get_dict()}")
    elif response.status_code == 429:
        print("Rate limited")
    else:
        print(response.text)


if __name__ == '__main__':
    get_pre_login_cookie()

