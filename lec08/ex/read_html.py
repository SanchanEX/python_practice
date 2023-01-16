from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://www.teu.ac.jp/"

    with urlopen(url) as res:
        for row in res:
            row = row.decode().rstrip()  # 改行文字削除
            if row == "":   # 空行だったら
                continue
            print(row)
