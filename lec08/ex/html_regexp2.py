import re


def read_html(file_path):
    with open(file_path, "r", encoding="utf8") as rfo:
        html = rfo.read()
    return html


if __name__ == "__main__":
    html = read_html("../data/index.html").replace("¥n", "")
    pattern = re.compile("<!--.*?-->")
    match_lst = pattern.findall(html)
    for match in match_lst:
        print(match)

    html = pattern.sub("", html)    # 削除

    # print(html)

    # with open("lec08/data/index2.html", "w", encoding="utf-8") as wfo:
    #     wfo.write(html+"\n")
