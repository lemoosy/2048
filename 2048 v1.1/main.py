from matrix import Matrix, draw_text
import copy, pygame, time


pygame.init()
window = pygame.display.set_mode((1000, 1000))
matrix = Matrix(4, 4)
matrix.add_number(2)
matrix.draw(window)


while not matrix.is_full():

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            matrix_copy = copy.deepcopy(matrix.get())

            if event.key == pygame.K_LEFT:
                matrix.move_left()
                
            elif event.key == pygame.K_UP:
                matrix.move_up()

            elif event.key == pygame.K_RIGHT:
                matrix.move_right()

            elif event.key == pygame.K_DOWN:
                matrix.move_down()

            else:
                continue

            if matrix.get() != matrix_copy:
                matrix.add_number(1)
                
            matrix.draw(window)


draw_text(window, "Game Over !", 500, 500, (231, 76, 60))
time.sleep(3)