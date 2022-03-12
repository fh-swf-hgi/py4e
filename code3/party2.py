class PartyAnimal:

    def party(self):
        try:
            self.x = self.x + 1
        except AttributeError:
            self.x = 1
        print("Partys bisher:", self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)
