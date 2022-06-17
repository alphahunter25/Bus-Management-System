import json 
import os

# with open("data.json", "r") as data:

#     datas = json.load(data)
#     datas["cats"].append("Mimi")
#     datas["cats"].append("jo")
#     datas["cats"].append("jojo")

#     with open("databackup.json", "w") as backup:
#         backup.write(json.dumps(datas, indent=2))


# os.remove("data.json")

# with open("data.json", "w") as data:
#     data.write(json.dumps(datas, indent=2))

#shit works till here....for now


class cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def view(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Color: {self.color}")

cat1 = cat("jojo", 12, "brown")
cat2 = cat("jeff", 14, "black")
cat3 = cat("jo", 11, "purple")

# with open("dataobj.json", "r") as objson:
#     obj = json.load(objson)
#     obj["cats"].append(cat1.__dict__)
#     obj["cats"].append(cat2.__dict__)
#     obj["cats"].append(cat3.__dict__)
    

# os.remove("dataobj.json")

# with open("dataobj.json", "w") as objson:
#     objson.write(json.dumps(obj, indent=2))

# catlist = [cat1, cat2, cat3]
# catdict = {"cats": []}

# for cat in catlist:
#     catdict["cats"].append(cat.__dict__)

# with open("objtest.json", "w") as file:
#     file.write(json.dumps(catdict, indent=2))

outcat = []
with open("objtest.json", "r") as file:
    obj = json.load(file)
    for i in obj["cats"]:
        tempcat = cat(i["name"], i["age"], i["color"])
        outcat.append(tempcat)

for i in outcat:
    i.view()











