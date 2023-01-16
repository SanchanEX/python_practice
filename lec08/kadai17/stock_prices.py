from dataclasses import dataclass
import sys
import re


@dataclass
class StockPrice:
    date: str           # 日付
    hajimene: float     # 始値
    takane: float       # 高値
    yasune: float       # 安値
    owarine: float      # 終値
    dekidaka: int       # 出来高
    owarine2: float     # 調整後終値


def read_html(file_path):
    with open(file_path, "r", encoding="utf8") as rfo:
        html = rfo.read()
    return html


class StockPrices(list):
    def append(self, value):
        if not isinstance(value, StockPrice):
            raise ValueError('StockPriceオブジェクト以外は追加できません')
        super().append(value)


if __name__ == "__main__":
    file_path = sys.argv[1]
    html = read_html(file_path)
    date_pattern = re.compile(
        '([1,2][0-9][0-9][0-9]年)([1-9]月|1[0-2]月)([1-9]日|1[0-9]日|2[0-9]日|3[0-1]日)'
    )
    hajimene_pattern = re.compile(
        '"openPrice".{1}"(.{3}|.{3}..{1})"'
    )
    takane_pattern = re.compile(
        '"highPrice".{1}"(.{3}|.{3}..{1})"'
    )
    yasune_pattern = re.compile(
        '"lowPrice".{1}"(.{3}|.{3}..{1})"'
    )
    owarine_pattern = re.compile(
        '"closePrice".{1}"(.{3}|.{3}..{1})"'
    )
    dekidaka_pattern = re.compile(
        '"volume".{1}"(.{10})"'
    )
    owarine2_pattern = re.compile(
        '"adjustedClosePrice".{1}"(.{3}|.{3}..{1})"'
    )

    date_lst = date_pattern.findall(html)
    hajimene_lst = hajimene_pattern.findall(html)
    takane_lst = takane_pattern.findall(html)
    yasune_lst = yasune_pattern.findall(html)
    owarine_lst = owarine_pattern.findall(html)
    dekidaka_lst = dekidaka_pattern.findall(html)
    owarine2_lst = owarine2_pattern.findall(html)

    # print(date_lst)
    # print(hajimene_lst)
    # print(takane_lst)
    # print(yasune_lst)
    # print(owarine_lst)
    # print(dekidaka_lst)

    # i = 0

    sp_lst = StockPrices()

    for date, h, t, y, o, deki, o2 in zip(date_lst, hajimene_lst, takane_lst, yasune_lst, owarine_lst, dekidaka_lst, owarine2_lst):
        date = ''.join(date)
        sp_lst.append(StockPrice(date, h, t, y, o, deki, o2))
        # i += 1
        # print(i)

    # for dl in date_lst:
    #     d = ''.join(dl)
    #     # StockPrice(d)
    # for hl in hajimene_lst:
    #     print(hl)

    ### これより下を変更しないこと ###
    try:
        sp_lst.append(243)
    except Exception as e:
        print(e)

    print(f"{len(sp_lst)}日間の株価データ：")
    for sp in sp_lst:
        print(sp)
