#match case 

x = int(input("Enter a number: "))

match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
    case 5:
        print("x is 5")
    case _:
        print("x is something else")