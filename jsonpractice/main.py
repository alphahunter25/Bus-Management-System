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

cat1 = cat("jojo", 12, "brown")
cat2 = cat("jeff", 14, "black")
cat3 = cat("jo", 11, "purple")

with open("dataobj.json", "r") as objson:
    obj = json.load(objson)
    obj["cats"].append(cat1.__dict__)
    obj["cats"].append(cat2.__dict__)
    obj["cats"].append(cat3.__dict__)
    

os.remove("dataobj.json")

with open("dataobj.json", "w") as objson:
    objson.write(json.dumps(obj, indent=2))

