import re


def read_html(file_path):
    with open(file_path, "r", encoding="utf8") as rfo:
        html = rfo.read()
    return html


if __name__ == "__main__":
    html = read_html("../data/index.html")
    pattern = re.compile('<a href="(http.*?)".*?>(.*?)</a>')    # aタグのみ抽出
    match_lst = pattern.findall(html)
    for match in match_lst:
        print(match)
