import requests
from bs4 import BeautifulSoup
from utils import *

path_urls = "urls.txt"
path_proxies = "proxies.txt"

urls = File_Interact(path_urls)
urls = urls.read_file_list()

proxies = File_Interact(path_proxies)
proxies = proxies.read_file_list()

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'cookie':''
}

# 1. Check link đã hiển thị trên Google.Com chưa
def test_checkindex():
    biendem = 0
    for url in urls:
        try:
            html_page = requests.get(f"https://www.google.com/search?q=site:{url}", headers=headers)
            soup = BeautifulSoup (html_page.content, 'html.parser')
            result = soup.find("div", id="rso")
            biendem += 1
            if result :
                print(f"{biendem} --- {url} --- Url này đã được indexed\n")
            else:
                print(f"{biendem} --- {url} --- Url này chưa được indexed\n")
        except BaseException as e:
            print("Loi: ", e)

if __name__ == "__main__":
    test_checkindex()
