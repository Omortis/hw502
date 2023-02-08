import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


# Question 5 on OOP
# Question 5: Part A

# Let's make a new class called House that where you have to provide
# the following attributes in the __init__ function:

#     address,
#     style, (see this list for inspiration)
#     yearBuilt
#     numUnits(are there rental units in the property?)
#     numFloors(how many floors does it have?)

# You should also include the attributes and provide methods to change
# the values of ( or just check!)

# doorsLocked
# windowsClosed

class House:

    def __init__(self, address, style,
                 yearBuilt, numUnits, numFloors):
        self.address = address
        self.style = style
        self.yearBuilt = yearBuilt
        self.numUnits = numUnits
        self.numFloors = numFloors
        self.doorsLocked = False
        self.windowsClosed = False
        self.coffeeMakerOn = False

    def Lock(self):
        self.doorsLocked = True

    def Unlock(self):
        self.doorsLocked = False

    def IsLocked(self):
        return "The door is locked" if self.doorsLocked == True else "The door is not locked."

    def OpenWindows(self):
        self.windowsClosed = False

    def CloseWindows(self):
        self.windowsClosed = True

    def AreWindowsUp(self):
        return "The windows are closed." if self.windowsClosed == True else "The windows are not closed."

    def TurnCoffeeOn(self):
        self.coffeeMakerOn = True

    def TurnCoffeeOff(self):
        self.coffeeMakerOn = False

    def IsCoffeeOn(self):
        return "The coffee is on." if self.coffeeMakerOn == True \
            else "Someone make some coffee!!!"


myHouse = House("1313 Mockingbird Lane", "Craftsman", "1943", "2", "3")

print(myHouse.address)
print(myHouse.style)
print(myHouse.yearBuilt)
print(myHouse.numUnits)
print(myHouse.numFloors)

print(myHouse.IsLocked())
myHouse.Lock()
print(myHouse.IsLocked())
myHouse.Unlock()
print(myHouse.IsLocked())

print(myHouse.AreWindowsUp())
myHouse.CloseWindows()
print(myHouse.AreWindowsUp())
myHouse.OpenWindows()
print(myHouse.AreWindowsUp())

print(myHouse.IsCoffeeOn())
myHouse.TurnCoffeeOn()
print(myHouse.IsCoffeeOn())
myHouse.TurnCoffeeOff()
print(myHouse.IsCoffeeOn())
