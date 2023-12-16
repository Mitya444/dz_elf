from abc import ABC, abstractmethod

class Elf(ABC):

    def __init__(self, name, mus_instrument, favorite_song):
        self.name = name
        self.mus_instrument = mus_instrument
        self.favorite_song = favorite_song

    def play_song(self):
        print(f"Elf {self.name} playing {self.favorite_song} on {self.mus_instrument}")

    @abstractmethod
    def fight(self):
        pass


class ElfRanger(Elf):

    def __init__(self, name, mus_instrument, favorite_song, bow: dict):
        super().__init__(name, mus_instrument, favorite_song)
        self.damage = bow["damage"]
        self.bow = bow["name"]

    def fight(self):
        print(f"Elf {self.name} kills his opponent with {self.bow}")


class ElfMage(Elf):

    def __init__(self, name, mus_instrument, favorite_song, spell: str):
        super().__init__(name, mus_instrument, favorite_song)
        self.spell = spell

    def fight(self):
        print(f"Elf {self.name} casts {self.spell} at the enemy")

    def cast_spell(self):
        print(f"Elf {self.name} is casting {self.spell}")


class ElfWarrior(Elf):

    def __init__(self, name, mus_instrument, favorite_song, weapon: str):
        super().__init__(name, mus_instrument, favorite_song)
        self.weapon = weapon

    def fight(self):
        print(f"Elf {self.name} strikes with {self.weapon}")

    def charge(self):
        print(f"Elf {self.name} is charging into battle with {self.weapon}")


bob = ElfRanger("Bob", "lute", "Bad Romance", {"name": "M249", "damage": 999})
bob.play_song()
bob.fight()

gandalf = ElfMage("Gandalf", "staff", "The Misty Mountains Cold", "Fireball")
gandalf.play_song()
gandalf.fight()
gandalf.cast_spell()

aragorn = ElfWarrior("Aragorn", "sword", "May It Be", "Andúril")
aragorn.play_song()
aragorn.fight()
aragorn.charge()