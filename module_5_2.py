class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'numberOfFloors = {self.numberOfFloors}')

h1 = House()
print(f'h1.numberOfFloors = {h1.numberOfFloors}')
h1.setNewNumberOfFloors(5)
print(f'h1.numberOfFloors = {h1.numberOfFloors}')
