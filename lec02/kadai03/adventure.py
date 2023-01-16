from pokemon import *
import sys

if __name__ == "__main__":
    file_path = sys.argv[1] # "lec02/data/poke_names.txt"
    zukan = Zukan(file_path)
    poke_name = sys.argv[2]
    mon = Monster(poke_name)
    print(zukan.search_monster(mon))
 