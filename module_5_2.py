class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors

h1 = House()
print(f'h1.numberOfFloors = {h1.numberOfFloors}')
h1.setNewNumberOfFloors(5)
print(f'h1.numberOfFloors = {h1.numberOfFloors}')
