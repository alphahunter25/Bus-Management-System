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


class Menu:
    def exiter(self):
        console.print(Text("Thank you for using the Bus Management System.", style = "bold red"))
        time.sleep(3)
        exit()

    def intcheck(self, n):
        try:
            age = int(Prompt.ask(n))
            return age

        except:
            console.print(Text("PLEASE ENTER A NUMBER", style = "yellow bold"))
            return self.intcheck(n)

    def intro(self):
        os.system("cls")        
        panel = Panel(Text("Welcome to the Bus Management System." , justify="center", style = "bold cyan"))
        console.print(panel)

        useAdMenu = Table(title="Would you like to run this program as:", box = box.DOUBLE_EDGE, width=40)
        useAdMenu.add_column("Key", style="yellow bold", justify="center", width = 1)
        useAdMenu.add_column("Options", style="white italic")
        useAdMenu.add_row("1", "A User")
        useAdMenu.add_row("2", "An Admin")

        console.print(useAdMenu)

        looper = True
        while looper:
            useadPrompt = Prompt.ask("\nPlease choose one of the options or press Q to quit ")
            if useadPrompt == "1" or useadPrompt == "2":
                looper = False
                return useadPrompt
            elif useadPrompt == "Q" or useadPrompt == "q":
                self.exiter()
            else:
                console.print(Text("Please enter a valid option", style = "bold red"))


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
                    newFare = self.intcheck("Please enter the new fare ")
                    lahoreBranch.changefare(newFare)

                else:
                    console.print(Text("No bus currently added . . . use command number 3 to add a route first ", style = "yellow"))

            elif adPrompt == "2":
                revenuecalc = lahoreBranch.revenue 
                console.print(Text(f"This branch has made Rs{revenuecalc} since it was made.", style = "bold underline medium_spring_green"))

            elif adPrompt == "3":
                start = Prompt.ask("\nPlease enter the starting point of the new route ")
                end = Prompt.ask("Please enter the destination of the new route ")
                fare = self.intcheck("Please enter the fare ")
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
        looper = True
        os.system("cls")

        panel = Panel(Text("Running the program as a User" , justify="center", style = "bold cyan"))
        console.print(panel)


        Menu = Table(title="Please choose one of the following commands", box = box.DOUBLE_EDGE, width=55)
        Menu.add_column("Key", style="yellow bold", justify="center", width = 5)
        Menu.add_column("Options", style="white italic")
        Menu.add_row("1", "Log in ")
        Menu.add_row("2", "Create a new account")
        Menu.add_row("3", "Clear screen ")
        console.print(Menu)

        while looper:
            adPrompt = Prompt.ask("Please choose one of the options or press Q to quit ")

            if adPrompt == "2":
                username = Prompt.ask("\nEnter your new username ")
                while username == "m" or username == "M":
                    username = Prompt.ask("\nPlease choose another username as 'm' is already an assigned key ") 
                password = Prompt.ask("Enter your password ")
                name = Prompt.ask("Enter your full name ")



                age = self.intcheck("Enter your age ")       
                cnic = self.intcheck("Enter your cnic number ")

                while clashcheck(username) == True:
                    username = Prompt.ask("\nUsername already exists. Please enter a new username ")

                tempaccount = Account(username, password, name, age , cnic, lahoreBranch)
                accounts.append(tempaccount)

                console.print(Text("ACCOUNT CREATED SUCCESSFULLY\n\n", style = "bold cyan underline"))



            elif adPrompt == "1":
                def userpasscheck():
                    username = Prompt.ask("\nEnter your username ")

                    password = Prompt.ask("Enter your password ")



                    for i in range(len(accounts)):
                        if username == accounts[i].username and password == accounts[i].password:
                            return i

                    else:
                        console.print(Text("Username or password is incorrect\n ", style = "bold red underline"))


                a = userpasscheck()
                if type(a) == int:
                    looper = False
                    return a



            elif adPrompt == "3":
                return self.user()

            elif adPrompt == "Q" or adPrompt == "q":
                self.exiter()

            

            else:
                console.print(Text("INVALID OPTION\n", style = "bold red underline"))


             


        
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
        looper = True
        while looper:
            adPrompt = Prompt.ask("\nPlease choose one of the options or press Q to quit ")

            if adPrompt == "1":
                console.print(Text(userout.bookticket(), style = "bold cyan"))

            elif adPrompt == "2":
                userout.viewtickets()

            elif adPrompt == "3":
                console.print(Text(userout.userinfo(), style = "cyan"))

            elif adPrompt == "4":
                sure = Prompt.ask("Are you sure you want to change your username and password? (Y/N) ")
                if sure == "Y" or sure == "y":
                    newname = Prompt.ask("Enter your new username ")
                    newpassword = Prompt.ask("Enter your new password ")
                    userout.changeinfo(newname, newpassword)
                    console.print(Text(f"Your profile information has been changed and will be applied on your next login ", style = "bold cyan"))


                elif sure == "N" or sure == "n":
                    pass

            elif adPrompt == "5":
                menu()

            elif adPrompt == "6":
                return False

            elif adPrompt == "Q" or adPrompt == "q":
                self.exiter()
            













def main():
    # user / admin selection
    menuinit = Menu()
    
    introout = menuinit.intro()
    
    os.system("cls")
    if introout == "2": #choosing admin
        menuout = menuinit.admin() 
        if menuout == False:

            os.system("cls")
            main()


    elif introout == "1": #choosing user
        menuout = menuinit.user()
        if type(menuout) ==  int:#checking if signin was successful
           
            os.system("cls")
            usermenu = menuinit.usersuccess(accounts[menuout]) #user menu
            if usermenu == False: 
                main()

        else:
            console.print(Text("UNKNOWN ERROR . . . PLEASE RESTART", style = "bold red underline"))
            time.sleep(3)
            exit()



main()







    
















