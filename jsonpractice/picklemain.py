import pickle

class seat:
    def __init__(self):
        self.availability = "Available"

    def book(self):
        self.availability = "Booked"

class bus:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels
        self.seats = []
        for i in range(wheels):
            self.seats.append(seat())

    def seatinfo(self):
        for i in range(len(self.seats)):
            print(f"Seat {i+1} is : {self.seats[i].availability}")


a = bus("bus1", 4)

abc = pickle.dumps(data)
with open("data.pickle", "wb") as f:
    f.write(abc)

with open("data.pickle", "rb") as f:
    datas = pickle.load(f)
    print(datas["branch"].routes[0].display())