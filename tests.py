
def intcheck(n):
    try:
        age = int(input(n))
        
        return age

    except:
        print("PLEASE ENTER A NUMBER")
        
        return intcheck(n)

a = 192

b = intcheck(f"Enter your age:, prev age {a}")
print(b)