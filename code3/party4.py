class PartyAnimal:

   def __init__(self):
     self.x = 0
     print("PartyAnimal wird erstellt")

   def party(self) :
     self.x = self.x + 1
     print("Partys bisher:", self.x)

   def __del__(self):
     print("Zerstört nach", self.x, "Partys")

an = PartyAnimal()
an.party()
an.party()
an = 42
print("an speichert nun", an)
