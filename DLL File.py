from bs4 import BeautifulSoup
import requests
# -----------------------------------
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'})
# -----------------------------------
dllfile = str(input("What DLL file do you need?\n"))
dllfile = dllfile.replace(".dll", "")
url = r"https://www.dll-files.com/" + dllfile + r"dll.html"
#url = r"https://example.org"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
urlcodes = soup.find_all("a")
print(urlcodes)
print(len(urlcodes))