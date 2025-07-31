#Define the local and Global variables with the same name and print both variables and understand the scope of the variables 
x = 10  
def scope():
    x = 20  
    print("Local x:", x)
scope()
print("Global x:", x)