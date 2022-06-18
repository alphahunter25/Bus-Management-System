from random import randint
from rich.console import Console
from rich.table import Table
from rich import box
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
import json

console = Console()
# from main import console



data = {
    "accounts" : []

}


def intcheck(n):
    try:
        age = int(Prompt.ask(n))
        return age

    except:
        console.print(Text("PLEASE ENTER A NUMBER", style = "yellow bold"))
        return intcheck(n)

#accounts system
class Person:
    def __init__(self, name, age, cnic):
        self.name = name
        self.age = age
        self.cnic = cnic

    def editinfo(self, name, age, cnic):
        self.name = name
        self.age = age
        self.cnic = cnic
    
    def viewinfo(self):
        print(f"Name: {self.name}\nAge: {self.age}\nCNIC: {self.cnic}")


class Account(Person):
    def __init__(self, username, password, name, age, cnic, branch):
        self.username = username
        self.password = password
        self.branch =branch
        super().__init__(name, age, cnic)
        self.bookings = []

    def changeinfo(self, username, password, age, cnic):
        self.username = username
        self.password = password
        self.age = age
        self.cnic = cnic
    
    def userinfo(self):
        console.print(Text("\nAccount information : ", style = "green bold underline"))
        console.print(Text("Name : ", style = "green"), Text(self.name, style = "white"))
        console.print(Text("Age : ", style = "green"), Text(str(self.age), style = "white"))
        console.print(Text("CNIC : ", style = "green"), Text(str(self.cnic), style = "white"))


    def viewtickets(self):
        if len(self.bookings) >0:
            Menu = Table(title="Current Bookings:", box = box.DOUBLE_EDGE, width=55, show_lines = True)
            Menu.add_column("No.", style="yellow bold", justify="center", width = 5)
            Menu.add_column("Ticket", style="white italic")
            for i in range(len(self.bookings)):
                Menu.add_row(f"{i+1}", f"{self.bookings[i].display()}")

            console.print(Menu)

        else:
            console.print(Text("You do not currently have any bookings", style = "bold cyan"))

    def bookticket(self):
        if len(self.branch.routes) == 0:
            return "No buses currently available"
        def busselector(route, type):
            for bus in range(len(self.branch.buses)):
                if self.branch.buses[bus].route == route and self.branch.buses[bus].type == type:
                    return self.branch.buses[bus]


        Menu = Table(title="Please choose one of the following Tickets", box = box.DOUBLE_EDGE, width=55, show_lines = True)
        Menu.add_column("Key", style="yellow bold", justify="center", width = 5)
        Menu.add_column("Options", style="white italic")

        for i in range(len(self.branch.routes)):
            Menu.add_row(f"{i+1}", self.branch.routes[i].display())

        console.print(Menu)


        choice = intcheck("Enter your choice: ")
        if choice <= 0 or choice > len(self.branch.routes):
            return "Invalid choice"
        tier = Prompt.ask(f"Would you like to go on our Economy buses or our First Class buses? (Extra fee of {self.branch.buses[1].fare} on First Class)\nEnter E for Economy or F for First Class: ")
        if choice-1 < len(self.branch.routes) and (tier == "E" or tier == "e"):
            chosenbus = busselector(self.branch.routes[choice-1], "Economy")
            if chosenbus.availability == "booked":
                return "Sorry, this bus is fully booked."
            ticket = Ticket(self.branch.routes[choice-1], chosenbus)
            self.bookings.append(ticket)
            availableseat = 0
            for i in range(len(chosenbus.seats)):
                if chosenbus.seats[i].availability == "Available":
                    availableseat += i
                    break
            chosenbus.seats[availableseat].book(self.username)
            chosenbus.seatavailability()
            self.branch.revenue += self.branch.routes[choice-1].fare
            return f"Ticket booked successfully."
            

        elif choice-1 < len(self.branch.routes) and (tier == "F" or tier == "f"):
            chosenbus = busselector(self.branch.routes[choice-1], "First Class")
            if chosenbus.availability == "booked":
                return "Sorry, this bus is booked."
            ticket = Ticket(self.branch.routes[choice-1], chosenbus)
            availableseat = 0
            for i in range(len(chosenbus.seats)):
                if chosenbus.seats[i].availability == "Available":
                    availableseat += i
                    break
            chosenbus.seats[availableseat].book(self.username)
            chosenbus.seatavailability()
            self.bookings.append(ticket)
            self.branch.revenue += chosenbus.fare
            return f"Ticket booked successfully."

        else:
            return "Invalid choice."


    def cancelticket(self):
        for i in range(len(self.bookings)):
            print(f"{i+1} : {self.bookings[i].display()}")
        choice = int(input("Enter the number of the ticket you want to remove: "))
        if choice < len(self.bookings):
            for bus in self.branch.buses:
                if bus.license == self.bookings[choice-1].bus.license:
                    bus.seats.cancel(self.username)
                    bus.seatavailability()

            self.bookings.pop(choice-1)
            return f"Ticket cancelled successfully."

        print("Invalid choice.")
        return False

            



#branch/bus system
class Branch:
    def __init__(self, location, fare):
        self.code = randint(10000, 99999)
        self.location = location
        self.routes = []
        self.firstfare = fare
        for i in self.routes:
            self.buses.append(Economy(i))
            self.buses.append(FirstClass(i, self.firstfare))
        self.buses = []
        self.revenue = 0

    def branchinfo(self):
        print(f"Branch Code - {self.code}\nBranch Location - {self.location}\nBranch Routes - {self.routes}\nBranch Buses - {self.buses}\nBranch Revenue - {self.revenue}")

    def changefare(self, fare):
        for i in self.routes:
            if type(i) == FirstClass:
                i.fare = fare 

        self.firstfare = fare     


    def viewroutes(self):
        print(f"Current Routes:\n{self.routes}")


class Seat:
    def __init__(self, avail = "Available"):
        self.availability = avail

    def book(self, account):
        self.bookedby = account
        self.availability = "Booked"  

    def cancel(self):
        self.bookedby = None
        self.availability = "Available"

class Bus:
    def __init__(self, route):
        self.license = randint(10000, 99999)
        self.route = route
        self.numseats = 24
        self.seats = []

        for i in range(self.numseats):
            self.seats.append(Seat())
        self.availability = "Available"


    def seatinfo(self, num):
        print(f"Seat {num} is : {self.seats[num-1].availability}")

    def seatavailability(self):
        status = 0
        for i in self.seats:
            if i.availability == "Booked":
                status += 1

        if status == 24:
            self.status = "full"
        else:
            self.status = f"{24-status} seats available"
        
        return self.status

    
    def businfo(self):
        print(f"License Plate - {self.license}\nBus Route - {self.route}\nBus Number of Seats - {self.numseats}\nAvailablility - {self.seatavailability()}")


class Economy(Bus):
    def __init__(self, route):
        super().__init__(route)
        self.type = "Economy"

    def businfo(self):
        print(f"Tier - {self.type}")
        super().businfo()


class FirstClass(Bus):
    def __init__(self, route, fare = 1000):
        super().__init__(route)
        self.fare = fare
        self.type = "First Class"

    def setfare(self, fare):
        self.fare = fare
        print(f"The fare is now {self.fare}")

    def businfo(self):
        print(f"Tier - {self.type}")
        super().businfo()


#route management
class Route:
    def __init__(self, start, destination, fee, departure):
        self.start = start
        self.destination = destination
        self.fare = fee
        self.departure = departure
    
    def display(self):
        return f"{self.start} to {self.destination}\nFee: {self.fare}\nDeparture: {self.departure}"




#tickets
class Ticket:
    def __init__(self, route, bus):
        self.route = route
        self.bus = bus

    


    def display(self):
        return f"{self.route.display()}\nTier: {self.bus.type}\nLicense Plate: {self.bus.license}"



#admin
class Admin:

    def viewrevenue(self, branch):
        print(f"{branch.location} has made ${branch.revenue}")

    def addroute(self,branch, start, des, fee, dep):
        branch.routes.append(Route(start, des, fee, dep))
        temp = Economy(branch.routes[-1])
        branch.buses.append(temp)
        temp = FirstClass(branch.routes[-1])
        branch.buses.append(temp)




    
    
        














