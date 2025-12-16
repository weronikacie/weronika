class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"Dom: {self.address}, {self.area} m2, "
            f"{self.rooms} pokoi, działka {self.plot} m2, cena {self.price}"
        )


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Mieszkanie: {self.address}, {self.area} m2, "
            f"{self.rooms} pokoi, piętro {self.floor}, cena {self.price}"
        )


house = House(120, 5, 800000, "Warszawa, Zielona 5", 500)
flat = Flat(60, 3, 450000, "Kraków, Długa 10", 3)

print(house)
print(flat)
