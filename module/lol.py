# import game
# import shop
# from functions.game import show_info as game_show_info, play_game 
# from functions.shop import show_info as shop_show_info, buy_item
import functions, friends
from functions.shop import show_info as shop_show_info, buy_item 
def turn_on():
    print('= Turn on game=')

    while True:
        choice = input('What would you like to do?\n' 
        '1: Go to Shop\n'
        '2: Play Game\n'
        '3: send_message\n'
        '0: Exit\n' 
        'Input: '
        )

        if choice == '0':
            break
        elif choice == '1':
            shop_show_info()
            buy_item()
        elif choice == '2':
            functions.game.show_info()
            functions.game.play_game()
        elif choice == '3':
            friends.chat.send_message()
        else:
            print('Choice not exist')
        print('-----------------------')

    print('= Trun off game =')

if __name__ == '__main__':
    turn_on()
