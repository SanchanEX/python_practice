from urllib.request import urlopen
from pprint import pprint

if __name__ == "__main__":
    url = "https://www.teu.ac.jp/"
    print(url)
    res = urlopen(url)
    pprint(res.getheaders())
    print(res.status)

    html = res.read()
    # print(type(html))
    html = html.decode()
    # print(type(html))
    # print(html)
