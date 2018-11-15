__author__ = 'Bertrand'
from menu import Menu
from enigma_machine_mono import EnigmaMachine


def process_choix(pMenu, pMachine):
    if choix == 0:
            msg = pMenu.get_initial_pos()
            res = pMachine.setup(msg)
    if choix == 1:
            msg = pMenu.get_message()
            res = pMachine.code(msg)
            pMenu.display_result_message(res)
    elif choix == 2:
            msg = pMenu.get_message()
            msg = pMachine.decode(msg)
            pMenu.display_result_message(msg)
    elif choix == 3:
        exit()

enigma_menu = Menu
my_machine = EnigmaMachine

while True:
    choix = enigma_menu.show()
    process_choix(enigma_menu,my_machine)





