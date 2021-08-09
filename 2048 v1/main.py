import os, random


class Matrix:

    def __init__(self, size_x, size_y):

        self.__matrix = [[0 for i in range(size_x)] for y in range(size_y)]
        self.__size_x = size_x
        self.__size_y = size_y

    def print(self):

        for line in self.__matrix:
            for value in line:
                print(" " * (4 - len(str(value))) + str(value), end = "   ")
            print()

    def __transpose(self):

        self.__matrix = list(map(list, zip(*self.__matrix)))

    def __mirror(self):

        self.__matrix = [line[::-1] for line in self.__matrix]

    def add_number(self, count):

        for i in range(count):

            while True:

                x = random.randint(0, 3)
                y = random.randint(0, 3)
                
                if self.__matrix[y][x] == 0:
                    self.__matrix[y][x] = [2, 2, 2, 4][random.randint(0, 3)]
                    break

    def move_left(self):

        for y in range(self.__size_y):
            for x in range(1, self.__size_x):
                for i in range(x, 0, -1):

                    if self.__matrix[y][i - 1] == 0 and self.__matrix[y][i] != 0:
                        self.__matrix[y][i - 1] = self.__matrix[y][i]
                        self.__matrix[y][i] = 0

                    if self.__matrix[y][i - 1] == 0 and self.__matrix[y][i] == 0:
                        break

                    if self.__matrix[y][i - 1] == self.__matrix[y][i]:
                        self.__matrix[y][i - 1] = self.__matrix[y][i] * 2 
                        self.__matrix[y][i] = 0
                        break

    def move_right(self):

        self.__mirror()
        self.move_left()
        self.__mirror()

    def move_up(self):

        self.__transpose()
        self.move_left()
        self.__transpose()

    def move_down(self):

        self.__transpose()
        self.__mirror()
        self.move_left()
        self.__mirror()
        self.__transpose()

    def full(self):

        for line in self.__matrix:
            if 0 in line:
                return False

        return True


matrix = Matrix(4, 4)
matrix.add_number(2)


while not matrix.full():
    
    os.system("cls")
    matrix.print()
    direction = input("Direction = ")

    if direction == "gauche":
        matrix.move_left()

    if direction == "haut":
        matrix.move_up()

    if direction == "droite":
        matrix.move_right()

    if direction == "bas":
        matrix.move_down()

    matrix.add_number(1)


print("Game Over !")