class Circle:
    def __init__(self, rayon = 1.0):
        self.rayon = rayon
    def perimetre(self):
        return 2 * 3.14 * self.rayon
    def surface(self):
        return 3.14 * (self.rayon ** 2)
    def definition(self) -> None:
        print(
            "Un cercle est l'ensemble des points "
            "situés à égale distance (le rayon) d'un point fixe appelé centre."
        )

perim = Circle()
surf = Circle()
print("-------------resultat du rayon par défaut-------------")
print(f"Le périmètre du cercle est : {(perim.perimetre())}")
print(f"La surface du cercle est : {(surf.surface())}")


perim = Circle(5)
surf = Circle(10)
print("-------------resultat du rayon reel-------------")
print(f"Le périmètre du cercle est : {(perim.perimetre())}")
print(f"La surface du cercle est : {(surf.surface())}")


print("-------------definition du cercle-------------")
definition = Circle()
definition.definition()

