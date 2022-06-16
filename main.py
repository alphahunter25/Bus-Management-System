from classes import *
from rich.console import Console
from rich.table import Table
from rich import box
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
import os
import time

os.system("cls")
console = Console()

lahoreBranch = Branch("Lahore", 5000)


accounts = []
def clashcheck(user):
    for i in accounts:
        if i.username == user:
            return True

# useAd = Prompt.ask("Please enter your choice ")

# if useAd == "1":
# #     print("so far so good")
# mainchecker = False

# if

class Menu:
    def exiter(self):
        console.print(Text("Thank you for using the Bus Management System.", style = "bold red"))
        exit()

    def intro(self):
        panel = Panel(Text("Welcome to the Bus Management System." , justify="center", style = "bold cyan"))
        console.print(panel)

        useAdMenu = Table(title="Would you like to run this program as:", box = box.DOUBLE_EDGE, width=40)
        useAdMenu.add_column("Key", style="yellow bold", justify="center", width = 1)
        useAdMenu.add_column("Options", style="white italic")
        useAdMenu.add_row("1", "A User")
        useAdMenu.add_row("2", "An Admin")

        console.print(useAdMenu)
        useadPrompt = Prompt.ask("\nPlease choose one of the options or press Q to quit ")
        if useadPrompt == "1" or useadPrompt == "2":
            return useadPrompt
        elif useadPrompt == "Q":
            self.exiter()
        else:
            console.print(Text("Please enter a valid option", style = "bold red"))
            return self.intro()

    def admin(self):
        os.system("cls")
        panel = Panel(Text("Running the program as an Admin" , justify="center", style = "bold cyan"))
        console.print(panel)


        Menu = Table(title="Please choose one of the following commands", box = box.DOUBLE_EDGE, width=55)
        Menu.add_column("Key", style="yellow bold", justify="center", width = 5)
        Menu.add_column("Options", style="white italic")
        Menu.add_row("1", "Change the fare of the First Class buses")
        Menu.add_row("2", "View branch revenue")
        Menu.add_row("3", "Add another route to this branch")  
        Menu.add_row("4", "Clear the screen")
        Menu.add_row("5", "Go back to the main menu")                

        console.print(Menu)

        looper = True
        while looper:
            adPrompt = Prompt.ask("\nPlease choose one of the options or press Q to quit ")

            if adPrompt == "1":
                if len(lahoreBranch.routes) != 0:
                    def intcheck():
                        try:
                            newFare = int(Prompt.ask("Please enter the new fare "))
                            return newFare

                        except:
                            console.print(Text("PLEASE ENTER A NUMBER", style = "yellow bold"))
                            intcheck()

                    newFare = intcheck()

                    lahoreBranch.changefare(newFare)

                else:
                    console.print(Text("No bus currently added . . . use command number 3 to add a route first ", style = "yellow"))

            elif adPrompt == "2":
                revenuecalc = lahoreBranch.revenue 
                console.print(Text(f"This branch has made Rs{revenuecalc} since it was made.", style = "bold underline medium_spring_green"))

            elif adPrompt == "3":
                start = Prompt.ask("\nPlease enter the starting point of the new route ")
                end = Prompt.ask("Please enter the destination of the new route ")
                def intcheck():
                    try:
                        newFare = int(Prompt.ask("Please enter the fare "))
                        return newFare

                    except:
                        console.print(Text("PLEASE ENTER A NUMBER", style = "yellow bold"))
                        intcheck()

                fare = intcheck()
                time = Prompt.ask("Please enter the departure time of the new route ")

                newRoute = Route(start, end, fare, time)
                lahoreBranch.routes.append(newRoute)
                lahoreBranch.buses.append(Economy(newRoute))
                if len(lahoreBranch.routes) == 1:
                    lahoreBranch.buses.append(FirstClass(newRoute))
                    
                else:
                    lahoreBranch.buses.append(FirstClass(newRoute, lahoreBranch.buses[-2].fare))

                console.print(Text(f"Route succesfully added", style = "bold underline medium_spring_green"))

            elif adPrompt == "Q" or adPrompt == "q":
                self.exiter()

            elif adPrompt == "4":
                return self.admin()

            elif adPrompt == "5":
                looper = False
                return False


            else:
                console.print(Text("Please enter a valid option", style = "bold red"))

    def user(self):
        os.system("cls")

        panel = Panel(Text("Running the program as a User" , justify="center", style = "bold cyan"))
        console.print(panel)


        Menu = Table(title="Please choose one of the following commands", box = box.DOUBLE_EDGE, width=55)
        Menu.add_column("Key", style="yellow bold", justify="center", width = 5)
        Menu.add_column("Options", style="white italic")
        Menu.add_row("1", "Log in ")
        Menu.add_row("2", "Create a new account")

        console.print(Menu)

        adPrompt = Prompt.ask("Please choose one of the options or press Q to quit ")

        if adPrompt == "2":
            username = Prompt.ask("\nEnter your new username ")
            password = Prompt.ask("Enter your password ")
            name = Prompt.ask("Enter your full name ")
            age = Prompt.ask("Enter your age ")
            cnic = Prompt.ask("Enter your CNIC Number ")

            while clashcheck(username) == True:
                username = Prompt.ask("\nUsername already exists. Please enter a new username ")

            tempaccount = Account(username, password, name, age , cnic, lahoreBranch)
            accounts.append(tempaccount)
        
            return 1


        elif adPrompt == "1":
            def userpasscheck():
                username = Prompt.ask("\nEnter your username or press 'm' to go back to the main menu if you don't have an account ")
                if username == "m" or username == "M":
                    return "m"
                password = Prompt.ask("Enter your password ")



                for i in range(len(accounts)):
                    if username == accounts[i].username and password == accounts[i].password:
                        return i

                else:
                    console.print(Text("Username or password is incorrect", style = "bold red underline"))
                    return userpasscheck()

            return userpasscheck()


        
    def usersuccess(self, userout):
        def menu():
            os.system("cls")
            
            panel = Panel(Text(f"Logged in successfully as {userout.username}" , justify="center", style = "bold cyan"))
            console.print(panel)

            Menu = Table(title="Please choose one of the following commands", box = box.DOUBLE_EDGE, width=55)
            Menu.add_column("Key", style="yellow bold", justify="center", width = 5)
            Menu.add_column("Options", style="white italic")
            Menu.add_row("1", "Book a ticket ")
            Menu.add_row("2", "View booked tickets ")
            Menu.add_row("3", "View your profile information ")
            Menu.add_row("4", "Change your profile information")
            Menu.add_row("5", "Clear the screen")
            Menu.add_row("6", "Go back to the main menu")

            console.print(Menu)

        menu()

        adPrompt = Prompt.ask("\nPlease choose one of the options or press Q to quit ")

        if adPrompt == "1":
            console.print(Text(f"{userout.bookticket()}", style = "bold cyan"))

        elif adPrompt == "2":
            userout.viewtickets()

        elif adPrompt == "3":
            console.print(Text(f"{userout.viewprofile()}", style = "bold cyan"))

        elif adPrompt == "4":
            sure = Prompt.ask("Are you sure you want to change your username and password? (Y/N) ")
            if sure == "Y" or sure == "y":
                newname = Prompt.ask("Enter your new username ")
                newpassword = Prompt.ask("Enter your new password ")
                userout.changeinfo(newname, newpassword)
                console.print(Text(f"Your profile information has been changed", style = "bold cyan"))
                menu()

            elif sure == "N" or sure == "n":
                menu()

        elif adPrompt == "5":
            menu()

        elif adPrompt == "6":
            return False

        elif adPrompt == "Q" or adPrompt == "q":
            self.exiter()
        
        











def main():
    # mainer = False
    menuinit = Menu()
    os.system("cls")
    introout = menuinit.intro()
    os.system("cls")
    if introout == "2":
        menuout = menuinit.admin()
        if menuout == False:
            # mainer = True
            os.system("cls")
            main()

    elif introout == "1":
        menuout = menuinit.user()
        if menuout == 1:
            console.print(Text("ACCOUNT CREATED SUCCESSFULLY . . . please wait", style = "bold cyan underline"))
            time.sleep(3)
            main()
            # userout = menuinit.user()
            # if type(userout) == Account:
            #     menuinit.usersuccess(userout)

            # else:
            #     console.print(type(userout))
            #     console.print("pain")
        elif type(menuout) ==  int:
            os.system("cls")
            menuinit.usersuccess(accounts[menuout])

        elif menuout == "m":
            main()
        else:
            console.print(Text("UNKNOWN ERROR . . . PLEASE RESTART", style = "bold red underline"))
            time.sleep(3)
            exit()

# main()
    # if introout == "2":
    #     os.system("cls")
    #     while mainchecker == False:
    #         menuinit.admin()



main()







    
















