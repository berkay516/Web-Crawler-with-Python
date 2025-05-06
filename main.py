import requests
from bs4 import BeautifulSoup

links = []

def get(urls):
    try:
        soup = BeautifulSoup(requests.get(urls).text, 'html.parser')
        return soup
    except:
        return None

def find(urls):
    soup = get(urls)
    if soup is None:
        return
    
    for a in soup.find_all("a"):
        hrf = a.get("href")
        if hrf and hrf.startswith(("http://", "https://")) and hrf not in links:
            links.append(hrf)
            print(hrf)
            find(hrf)

if __name__=="__main__":
    user=input("enter link to crawling: ")
    find(user)






