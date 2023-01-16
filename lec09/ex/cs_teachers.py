from bs4 import BeautifulSoup


class Teacher:
    def __init__(self, name, url, pos, field):
        self.name = name
        self.url = url
        self.pos = pos
        self.field = field

    def __repr__(self):
        return f"{self.name} (URL：{self.url}／職位：{self.pos}／専門分野：{self.field})"


if __name__ == "__main__":
    file_path = "../data/teachers.html"  # sys.argv[1]
    soup = BeautifulSoup(open(file_path, encoding="utf-8"), "html.parser")
    a_tag = soup.find("a", class_="csdep_linkbutton")
    href = a_tag["href"]
    li_tag = a_tag.find("li", class_="csdep_topprof_right")
    h2_tag = li_tag.h2
    h4_tag = li_tag.h4
    p_tag = li_tag.p
    oono = Teacher(h2_tag.string, "https://www.teu.ac.jp"+href,
                   h4_tag.string.replace("　", ""), p_tag.string)
    print("1", oono)
