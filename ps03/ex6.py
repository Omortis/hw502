import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


class House(object):
    def __init__(self, address, style, yearBuilt, numUnits, numFloors, marketValue):
        self.address = address
        self.style = style
        self.yearBuilt = yearBuilt
        self.numUnits = numUnits
        self.numFloors = numFloors
        self.marketValue = marketValue
        self._doorsLocked = False  # protected
        self._windowsClosed = True  # protected
        self._coffeeMakerOn = False  # protected

    def __str__(self):
        output = self.address + ", "
        output += self.style + ", "
        output += str(self.yearBuilt) + ", "
        output += str(self.numUnits) + " units, "
        output += str(self.numFloors) + " floors, "
        output += '${:9,.2f}'.format(self.marketValue)
        return output

    # Added for Question 2, below
    def __lt__(self, other):
        return self.marketValue < other.marketValue

    def areDoorsLocked(self):
        return self._doorsLocked

    def lockDoors(self):
        self._doorsLocked = True

    def unlockDoors(self):
        self._doorsLocked = False

    def areWindowsClosed(self):
        return self._windowsClosed

    def closeWindows(self):
        self._windowsClosed = True

    def openWindows(self):
        self._windowsClosed = False

    # Added for 6b.
    def turnCoffeeOn(self):
        self._coffeeMakerOn = True

    def turnCoffeeOff(self):
        self._coffeeMakerOn = False

    def isCoffeeOn(self):
        return self._coffeeMakerOn


home = House("1313 Mockingbird Lane", "Colonial", "1929", 1, 3, 125000)
print(home)
print("default")
print("Are the doors locked?   ", home.areDoorsLocked())
print("Are the windows closed? ", home.areWindowsClosed())
assert home.areDoorsLocked() == False
assert home.areWindowsClosed() == True

print("\nlockDoors(), openWindows()")
home.lockDoors()
home.openWindows()
print("Are the doors locked?   ", home.areDoorsLocked())
print("Are the windows closed? ", home.areWindowsClosed())
assert home.areDoorsLocked() == True
assert home.areWindowsClosed() == False

print("\nunlockDoors(), closeWindows()")
home.unlockDoors()
home.closeWindows()
print("Are the doors locked?   ", home.areDoorsLocked())
print("Are the windows closed? ", home.areWindowsClosed())
assert home.areDoorsLocked() == False
assert home.areWindowsClosed() == True

# Added for 6b.
print("\nisCoffeeOn()")
print("Is there coffee on?   ", home.isCoffeeOn())
print("Someone make some coffee!!!")
assert home.isCoffeeOn() == False
home.turnCoffeeOn()
print("Is there coffee on?   ", home.isCoffeeOn())
assert home.isCoffeeOn() == True
