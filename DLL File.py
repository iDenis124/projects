from bs4 import BeautifulSoup
import requests
# -----------------------------------
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/70.0'})
# -----------------------------------
dllfile = str(input("What DLL file do you need?\n"))
dllfile = dllfile.replace(".dll", "")
url = r"https://www.dll-files.com/" + dllfile + r"dll.html"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')