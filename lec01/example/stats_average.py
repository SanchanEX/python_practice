def read_stats(file_path):
    stats = []
    with open(file_path, "r") as rfo:
        for row in rfo:
            row = row.rstrip()
            stats.append([int(col) for col in row.split(" ")])
    return stats


def calc_average(lst):
    return sum(lst) / len(lst)


if __name__ == "__main__":
    stats = read_stats("../data/base_stats.txt")
    for col_idx in range(6):
        avg = calc_average([stat[col_idx] for stat in stats])
        print(col_idx+1, f"{avg:.2f}")
