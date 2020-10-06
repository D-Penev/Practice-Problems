
class Trainer():
    def __init__(self,name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return 'This pokemon is already caught'

        self.pokemon.append(pokemon)
        return  f'Caught {pokemon.pokemon_details()}'
    def release_pokemon(self, pokemon_name):
        corr_len = len(list(filter(lambda x: x.name == pokemon_name, self.pokemon)))
        if corr_len == 0:
            return 'Pokemon is not caught'
        else:
            for i in range(0, len(self.pokemon)):
                if self.pokemon[i].name == pokemon_name:
                    self.pokemon.remove(self.pokemon[i])
                    break

    def trainer_data(self):
        trainer = f'Pokemon Trainer {self.name}'
        trainer += f'Pokemon couunt {len(self.pokemon)}'
        for i in range(0, len(self.pokemon)):
            trainer += f'- {self.pokemon[i].pokemon_details()}\n'
        return trainer

