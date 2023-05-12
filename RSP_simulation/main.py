from game import Game
from logo import logo, interface

object_num = None
game_state = True
default_bg = False

# print the ASCII logo
print(logo + '\n')

while game_state:
    # print the interface menu
    print(interface)

    # get the input
    ans = input("Enter the number: ")

    match ans:
        case '1':
            if object_num is None:
                game = Game()
            else:
                game = Game(object_num=object_num)

            if default_bg:
                game.set_default_bgpic()

            # start simulation
            game.start()

        case '2':
            try:
                object_num = int(input('Enter the objects number: '))
                if 1 > object_num or object_num > 30:
                    object_num = None
                    raise RuntimeError
            except:
                print("You should enter the integer number between 1 and 30 ")

        case '3':
            default_bg = True
            print('Background image was set to default')

        case '4':
            game_state = False
            print("Goodbye!")

        case _:
            print("Enter a number between 1 and 4.")
