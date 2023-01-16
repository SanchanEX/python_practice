from bs4 import BeautifulSoup
import sys
import re


if __name__ == "__main__":
    path = sys.argv[1]
    soup = BeautifulSoup(open(path, encoding="utf-8"), "html.parser")
    ph = soup.find("table", cellspacing=0)
    phh = ph.find_next_sibling("table")
    pattern = re.compile(
        "<tr><td>(\d+:\d+)</td><td>(\d+:\d+)</td><td>(\d+:\d+)</td><td></td></tr>")
    d = pattern.findall(str(phh))
    for i, time in enumerate(d, 1):
        time = list(time)
        print(i, time)
