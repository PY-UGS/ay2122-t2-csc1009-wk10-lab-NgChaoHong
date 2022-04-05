def modulefunc(mod):
    if (mod == "CSC1006"):
        print("Mathematics 2")
    elif(mod == "CSC1007"):
        print("Operating Systems")
    elif(mod == "CSC1008"):
        print("Data Structure and Algorithms")
    elif(mod == "CSC1009"):
        print("Object Oriented Programming")
    elif(mod == 'CSC1010'):
        print("Computer Networks")
    else:
        print("Unknown module")

module_code = str(input("enter module code: "))
modulefunc(module_code)