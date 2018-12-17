__author__ = 'Bertrand'


class Menu():
    def get_message(self):
        msg = ''
        while msg  == '':
            msg = input("veuillez saisir un message : ")
        return msg

    def display_result_message(self, msg):
        print(" message après traitement : ")
        print(msg + '\n')

    def show(self):
        print("Que voulez vous faire ?")
        print("1 : coder un message")
        print("2 : décoder un message")
        print("3 : quitter")

        choix = 4
        valid_choices = [1,2,3]
        while (choix not in valid_choices):
            choix = int(input())
            if choix not in valid_choices:
                print("mauvais choix, réessayez")
        return choix








