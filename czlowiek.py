class Czlowiek():
    def __init__(self,imie):
        print("Wywoluje sie konstruktor")
        self.imie=imie
    #cialo klasy
    gatunek="human"
    def podskocz(self):
          print('podskoczylem!')
    def __del__(self):
        print("Do widzenia, babcia Gienia")

class Dziecko(Czlowiek):
    def bawimy_sie(self):
        print('juhuuuu!')


#teraz tworzymy obiekt (instrukcje klasy)
marcin=Czlowiek('marcin')
#odwolanie do Metody
marcin.podskocz()
#odwolanie do atrybutu
print(marcin.imie)
basia=Czlowiek('Basia')
print(basia.imie)

barcin=Dziecko("barcin")
barcin.podskocz()
barcin.bawimy_sie()
