from main.controller import Controller
from main.menu import Menu


def main():
    player = Menu().player
    c = Controller(player)
    c.start()

if __name__ == "__main__":
    main()
