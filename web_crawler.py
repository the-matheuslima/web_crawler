import requests
import sys
from bs4 import BeautifulSoup

TO_CRAWL = []
CRAWLED =  set()


def get_links(html):
    links = []   
    try: 
        soup = BeautifulSoup(html, "html.parser")
        tags_a = soup.find_all("a", href=True)
        for tag in tags_a:
            link = tag['href']
            if link.startswith("http"):
                links.append(link)                
        return links
    except:
        pass

def crawl():
    while 1:
        if TO_CRAWL:
            url = TO_CRAWL.pop()
            response = requests.get(url)
            html = response.text
            if html:
                links = get_links(html)
                if links:
                    for link in links:
                        if link not in CRAWLED and link not in TO_CRAWL:
                            TO_CRAWL.append(link)

                print("Crawling {}".format(url))

                CRAWLED.add(url)
            else:
                CRAWLED.add(url)
        else:
            print("Done")
            break
        
if __name__ == "__main__":
    url = sys.argv[1]
    TO_CRAWL.append(url)
    crawl()