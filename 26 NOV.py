import random
import os

class Ceritaku:
    def __init__(self):
        Mie = ["Mie hompimpa", "Mie suit ", "Mie Gacoan"]
        randomMie = random.choice(Mie)

        tempatmakan = ["Sukabangun", "Celentang"]
        randomTempatmakan = random.choice(tempatmakan)

        gorengan = ["Udang keju", "Udang rambutan", "Siomay", "Pangsit goreng"]
        randomGorengan = random.choice(gorengan)

        minuman = ["Es Teh", "Air mineral", "Jus jeruk", "Es dawet", "Tea tarik"]
        randomMinuman = random.choice(minuman)
        os.system("cls")
        print(f"saya makan mie gacoan, mie di antarkan ke meja, saya makan mie {randomMie} dan {randomGorengan} saya minum {randomMinuman} dan saya makan mie gacoannya di {randomTempatmakan}")
def main():
    run = Ceritaku()

if __name__ == "__main__":
    main()