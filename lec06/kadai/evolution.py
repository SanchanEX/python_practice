class EvolvList(list):
    def __init__(self, tit):
        super().__init__()
        self.tit = tit

    def evolution(self, d=0):
        ind = '　'*d
        print(ind+self.tit)

        for i in self:
            if isinstance(i, EvolvList):
                i.evolution(d + 1)
            else:
                print(ind + '　' + i)


if __name__ == "__main__":
    tane = EvolvList("フシギダネ")
    kusa = EvolvList("フシギソウ")
    hana = EvolvList("フシギバナ")
    tane.append(kusa)
    kusa.append(hana)
    hana.append("フシギスギ")
    tane.evolution()
    print(tane)

    nazo = EvolvList("ナゾノクサ")
    kusai = EvolvList("クサイハナ")
    nazo.append(kusai)
    kusai.append("ラフレシア")
    kusai.append("キレイハナ")
    nazo.evolution()
    print(nazo)

    eevee = EvolvList("イーブイ")
    eevee.append("シャワーズ")
    eevee.append("サンダース")
    eevee.append("ブースター")
    eevee.append("エーフィ")
    eevee.append("ブラッキー")
    eevee.append("リーフィア")
    eevee.append("グレイシア")
    eevee.append("ニンフィア")
    eevee.evolution()
    print(eevee)
