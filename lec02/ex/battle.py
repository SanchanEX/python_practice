from pikachu import *
from random import randint

if __name__ == "__main__":
    wild_pikas = [WildPikachu(randint(1,100)) for i in range(5)]
    pika = TamePikachu("光宙", "サトシ", 32)
    for wp in wild_pikas:
        print(pika, "vs", wp)
        if pika > wp:
            print(pika, "の勝利！")
        else:
            print(pika, "の敗北...")
    
