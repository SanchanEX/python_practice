from bs4 import BeautifulSoup
from dataclasses import dataclass
from pprint import pprint


@dataclass
class StockPrice:
    date: str
    hajimene: float
    takane: float
    yasune: float
    owarine: float
    dekidaka: int
    owarine2: float


if __name__ == "__main__":
    file_path = "../data/ufj.html"  # sys.argv[1]
    soup = BeautifulSoup(open(file_path, encoding="utf-8"), "html.parser")
    #print(soup,              type(soup))
    #print(soup.title,        type(soup.title))
    #print(soup.title.string, type(soup.title.string))
    # pprint(soup.title.__dict__)
    #table_tag = soup.table
    table_tag = soup.find("table", class_="tjCjeiMn _1aNPcH77")
    tr_tags = table_tag.find_all("tr")  # tableの子孫の中からtrを抽出
    for tr_tag in tr_tags:
        td_tags = tr_tag.find_all("td")  # tableの子孫の中からtdを抽出
        if len(td_tags) == 0:
            continue
        th_tag = tr_tag.th              # 日付文字列はthで囲まれている
        date = th_tag.string
        prices = [date]
        for td_tag in td_tags:
            prices.append(td_tag.string)
        sp = StockPrice(*prices)
        print(sp)
