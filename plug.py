import requests
from bs4 import BeautifulSoup

def parse(plugin_name):
    URL = f'https://wordpress.org/plugins/{plugin_name}'
    try:
        page = requests.get(URL)
    except requests.exceptions.RequestException:
        return "Network Error!"

    soup = BeautifulSoup(page.content, "html.parser")

    try:
        div_contents = soup.find("div", class_="widget plugin-meta")
        li_contents = div_contents.find_all("li")
    except AttributeError:
        return "Not Exist!"

    for item in li_contents:
        if "Active installations" in item.text:
            ad = item.find("strong")
            return ad.text

def main():
    try:
        with open("plugins.txt", "r") as file:
            plugin_names = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("plugins.txt file not found!")
        return

    for plugin_name in plugin_names:
        result = parse(plugin_name)
        print(f"{plugin_name}: {result}")

if __name__ == "__main__":
    main()
