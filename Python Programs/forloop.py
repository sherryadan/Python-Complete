#for loop 
#for loop is used to iterate over a sequence (list, string, tuple, dictionary, set, etc.)

name = "Adan"

for i in name:
    print(i, end=" ")

    if(i == "b"):
        print("Here is something very special!")
    
    else:
        print("")

colors = ["red", "green", "blue"]

for color in colors:
    print(color)
# indentation matters a lot here.
    for i in color:
        print(i)
