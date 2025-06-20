class Farm:
    def __init__(self, farm_name: str):
        self.name = farm_name
        self.animals: dict[str, int] = {}

    def add_animal(self, animal_type: str, count: int = 1) -> None:
        """Ajoute `count` animaux de type `animal_type` à la ferme."""
        if count <= 0:
            raise ValueError("count doit être strictement positif")

        self.animals[animal_type] = self.animals.get(animal_type, 0) + count

    def get_info(self) -> str:
        """Retourne un rapport multi‑lignes du stock d’animaux."""
        title = f"{self.name}'s farm"

        max_len = max((len(a) for a in self.animals), default=0)
        lines = [f"{animal.ljust(max_len)} : {qty}"
                 for animal, qty in self.animals.items()]

        body = "\n".join(lines)
        return f"{title}\n\n{body}\n\n    E-I-E-I-0!"


    def get_animal_types(self) -> list[str]:
        """Retourne la liste triée des types d’animaux."""
        return sorted(self.animals)

    def get_short_info(self) -> str:
        """Retourne une phrase courte résumant la ferme et ses animaux."""
        animal_types = self.get_animal_types()
        if not animal_types:
            return f"{self.name}'s farm has no animals yet."

        parts: list[str] = []
        for animal in animal_types:
            qty = self.animals[animal]
            if qty > 1 and animal not in {"sheep", "fish"}:
                parts.append(animal + "s")
            else:
                parts.append(animal)

        if len(parts) > 2:
            listing = ", ".join(parts[:-1]) + " and " + parts[-1]
        elif len(parts) == 2:
            listing = " and ".join(parts)
        else:
            listing = parts[0]

        return f"{self.name}'s farm has {listing}."


if __name__ == "__main__":
    macdonald = Farm("McDonald")
    macdonald.add_animal('cow', 5)
    macdonald.add_animal('sheep')
    macdonald.add_animal('sheep')
    macdonald.add_animal('goat', 12)

    print(macdonald.get_info())
    print(macdonald.get_short_info())
