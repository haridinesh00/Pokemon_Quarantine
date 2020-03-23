class Trainer:

    def __init__(self):
        self.Name = ''
        self.party_pokemon = []
        self.items = []

    def addPokemon(self,pokemon):
        self.party_pokemon.append(pokemon)

    def addItem(self,newItem):
        self.items.append(newItem)

    def useItem(self, usedItem):
        self.items.remove(usedItem)

    def bag(self):
        for i in set(self.items):
            print(i, " : ", self.items.count(i))
