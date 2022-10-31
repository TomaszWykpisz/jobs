from pracuj import Pracuj
from indeed import Indeed
from olx import Olx


class Controller():

    def __init__(self):

        self.option = None
        self.Pracuj = Pracuj()
        self.Indeed = Indeed()
        self.Olx = Olx()
        self.show_options()
        self.input_option()


    def choose_option(self):
        
        if self.option == 1: self.Pracuj.get_data_from_website()
        elif self.option == 2: self.Indeed.get_data_from_website()
        elif self.option == 3: self.Olx.get_data_from_website()
        elif self.option == 4: pass
        elif self.option == 5: self.Pracuj.show_data()
        elif self.option == 6: self.Indeed.show_data()
        elif self.option == 7: self.Olx.show_data()
        elif self.option == 8: pass
        elif self.option == 9: exit()

        self.show_options()
        self.input_option()


    def show_options(self):

        print("Choose your option")
        print("1. Get data from pracuj")
        print("2. Get data from indeed")
        print("3. Get data from olx")
        print("4. Get data from everywhere")
        print("5. Show data from pracuj")
        print("6. Show data from indeed")
        print("7. Show data from olx")
        print("8. Show data from everywhere")
        print("9. Exit")


    def input_option(self):
        
        self.option = input("Your option: ")
        if self.validate_input():
            self.choose_option()


    def validate_input(self):

        try:
            self.option = int(self.option)
        except:
            self.wrong_input()
            return False
        
        if self.option < 1 or self.option > 9:
            self.wrong_input()
            return False 
        
        return True


    def wrong_input(self):
        print("Wrong input")
        self.input_option()
        