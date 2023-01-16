class Monster:
    def __init__(self, title):
        self.name = title

    def __call__(self):
        print(f"僕の名前は{self.name}です")


if __name__ == "__main__":
    fushi = Monster("フシギダネ")
    fushi()
    pika = Monster("ピカチュウ")
    pika()
