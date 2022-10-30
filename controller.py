class Controller():

    def validate_input(self, option):

        try:
            option = int(option)
        except:
            return False
        if option < 1 or option > 9: return False 
        return True

    def choose_option(self, option):

        if not self.validate_input(option): 
            option = input("Please choose correct option: ")
            self.choose_option(option)
        
        if option == 1: pass
        elif option == 2: pass
        elif option == 3: pass
        elif option == 4: pass
        elif option == 5: pass
        elif option == 6: pass
        elif option == 7: pass
        elif option == 8: pass
        elif option == 9: exit()

        