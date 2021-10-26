class PartyAnimal:

    def party(self):
        try:
            self.x = self.x + 1
        except AttributeError:
            self.x = 1
        print("Partys bisher:",self.x)

an = PartyAnimal()
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.party))
