__author__ = 'Bertrand'
from menu import Menu
from enigma_machine_mono import EnigmaMachine

enigma_menu = Menu()
my_machine = EnigmaMachine()


def process_choix(choix):
    if choix == 1:
        str = enigma_menu.get_message()
        encoded = my_machine.code(str)
        enigma_menu.display_result_message(encoded)
    elif choix == 2:
        str = enigma_menu.get_message()
        decoded = my_machine.decode(str)
        enigma_menu.display_result_message(decoded)
    elif choix == 3:
        exit()

while True:
    choix = enigma_menu.show()
    process_choix(choix)





