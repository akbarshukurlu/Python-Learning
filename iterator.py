print("""
************************************************
                Cubes of Numbers
************************************************
""")
class Cube():

    def __init__(self, max = 0):

        self.max = max
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self.count <= self.max):
            result = self.count ** 3

            self.count += 1

            return result
        else:
            self.count = 0
            raise StopIteration


cube = Cube(int(input("Your Conut:")))


iterator = iter(cube)

for i in cube:
    print(i)



