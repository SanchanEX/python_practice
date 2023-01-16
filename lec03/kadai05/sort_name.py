import sys


def read_file(file_path):
    names = []
    with open(file_path, "r", encoding='utf-8')as rfo:
        for row in rfo:
            nam = row.rstrip().split()[1]
            names.append(nam)
    return names


def write_file(wfile, sort_list):
    with open(wfile, 'w', encoding='utf-8')as wf:
        for row in sort_list:
            wf.writelines(row)


def keisan(name):
    num = 0
    m = 5
    li = list(name)
    for i in li:
        i = ord(i)
        n = int(i) ** m
        m -= 1
        num += n
    return num


if __name__ == '__main__':
    l = []
    dic = {}
    lis = read_file(sys.argv[1])
    for i in lis:
        d = keisan(i)
        dic[i] = d
    sort = sorted(dic.items(), key=lambda t: t[1])
    for i in sort:
        l.append(i[0]+'\n')
    write_file(sys.argv[2], l)
