from colors import COLORS
import copy, pygame, random


def draw_text(window, message, x, y, color):

    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render(message, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    window.blit(text, textRect)
    pygame.display.flip()


class Matrix:

    def __init__(self, size_x, size_y):

        self.__size_x = size_x
        self.__size_y = size_y
        self.__matrix = [[0 for i in range(size_x)] for y in range(size_y)]

    def get(self):
        
        return self.__matrix

    def draw(self, window):

        for y in range(self.__size_y):
            for x in range(self.__size_x):
                
                pygame.draw.rect(window, COLORS[self.__matrix[y][x]], pygame.Rect(250 * x, 250 * y, 250, 250))

                if self.__matrix[y][x] != 0:
                    draw_text(window, str(2 ** self.__matrix[y][x]), 250 * x + 125, 250 * y + 125, (255, 255, 255))

        pygame.display.flip()

    def __transpose(self):

        self.__matrix = list(map(list, zip(*self.__matrix)))

    def __mirror(self):

        self.__matrix = [line[::-1] for line in self.__matrix]

    def add_number(self, count):

        positions = list()

        for y in range(self.__size_y):
            for x in range(self.__size_x):
                if self.__matrix[y][x] == 0:
                    positions.append((x, y))

        for i in range(count):
            x, y = positions[random.randint(0, len(positions) - 1)]                
            self.__matrix[y][x] = [1, 1, 1, 1, 2][random.randint(0, 4)]

    def move_left(self):

        for y in range(self.__size_y):
            for x in range(1, self.__size_x):

                if self.__matrix[y][x] == 0:
                    continue

                for i in range(x, 0, -1):

                    # [2, 0, 2, 0] -> [2, 2, 0, 0]
                    if self.__matrix[y][i - 1] == 0:
                        self.__matrix[y][i - 1] = self.__matrix[y][i]
                        self.__matrix[y][i] = 0

                    # [2, 2, 0, 0] -> [3, 0, 0, 0]
                    if self.__matrix[y][i - 1] == self.__matrix[y][i]:
                        self.__matrix[y][i - 1] = self.__matrix[y][i] + 1
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

    def is_full(self):

        for line in self.__matrix:

            if 0 in line:
                return False

        matrix_copy = copy.deepcopy(self.__matrix)

        self.move_left()
        self.move_up()
        self.move_right()
        self.move_down()

        if self.__matrix == matrix_copy:
            return True

        self.__matrix = copy.deepcopy(matrix_copy)
        return False