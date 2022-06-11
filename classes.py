from random import randint


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
    def __init__(self, username, password, name, age, cnic):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.cnic = cnic
        self.bookings = []

    def changeinfo(self, username, password):
        self.username = username
        self.password = password
    
    def userinfo(self):
        print(f"_User_ : {self.username}\n_Name_ : {self.name}\n_Age_ : {self.age}\n_CNIC_ : {self.cnic}")

    def viewtickets(self):
        print(f"_User_ : {self.username}\n_Current Bookings_:{self.bookings} ")

    def bookticket(self, ticket):
        self.bookings.append(ticket)

    def cancelticket(self, ticket):
        self.bookings.remove(ticket)


#branch/bus system
class Branch:
    def __init__(self, location):
        self.code = randint(10000, 99999)
        self.location = location
        self.routes = []
        self.buses = []
        self.revenue = 0

    def branchinfo(self):
        print(f"Branch Code - {self.code}\nBranch Location - {self.location}\nBranch Routes - {self.routes}\nBranch Buses - {self.buses}\nBranch Revenue - {self.revenue}")

    def viewroutes(self):
        print(f"Current Routes:\n{self.routes}")


class Seat:
    def __init__(self):
        self.availability = "Available"

    def book(self, account):
        self.bookedby = account  

class Bus:
    def __init__(self, route):
        self.license = randint(1000, 9999)
        self.route = route
        self.numseats = 24
        self.seats = []
        for i in range(self.numseats):
            self.seats.append(Seat())
        self.availablility = "Available"


    def seatinfo(self, num):
        print(f"Status of seat {num}: {self.seats[num-1].availability}")

    def availability(self):
        status = 0
        for i in self.seats:
            if i.availability == "Available":
                status += 1

        if status == 24:
            self.status = "full"
        else:
            self.status = f"{24-status} seats available"
        
        return self.status

    
    def businfo(self):
        print(f"License Plate - {self.license}\nBus Route - {self.route}\nBus Number of Seats - {self.numseats}\nAvailablility - {self.availablility()}")


class Economy(Bus):
    def __init__(self, route):
        super().__init__(route)
        self.type = "Economy"

    def businfo(self):
        print(f"Tier - {self.type}")
        super().businfo()


class FirstClass(Bus):
    def __init__(self, route, fare):
        super().__init__(route)
        self.fare = fare
        self.type = "First Class"

    def setfare(self, fare):
        self.fare = fare
        print(f"The fare is now {self.fare}")

    def businfo(self):
        print(f"Tier - {self.type}")
        super().businfo()



    
    
        














