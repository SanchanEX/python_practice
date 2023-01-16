import sys
import re


def read_html(file_path):
    with open(file_path, "r", encoding="utf8") as rfo:
        html = rfo.read()
    return html


if __name__ == "__main__":
    file_path = sys.argv[1]
    html = read_html(file_path)
    detail_pattern = re.compile(
        '<a href="(/info/lab/teacher/cs/index.html.*?)".*?>'
    )
    name_pattern = re.compile(
        '<h2>(.*?)</h2>'
    )
    position_pattern = re.compile(
        '<h4>(教授.*?)|(准教授.*?)|(実験助手).*?|(講師).*?|(助教).*?</h4>'
    )

    detail_lst = detail_pattern.findall(html)
    name_lst = name_pattern.findall(html)
    position_lst = position_pattern.findall(html)
    print(position_lst)
    print(len(position_lst))

    # match_lst.append(("hoge/fuga/:piyopiyo-1.html", "ほげほげ", "教授", "プログラミング"))
    # print(f"リストの長さ：{len(match_lst)}")
    # for i, match in enumerate(match_lst, 1):
    #     try:
    #         name = match[1]
    #         url  = "https://www.teu.ac.jp"+match[0]
    #         pos  = match[2].split()[0]
    #         field= match[3]
    #         t = Teacher(name, url, pos, field)
    #         print(i, t)
    #     except Exception as e:
    #         print(i, e)
