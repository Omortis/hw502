import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Question 1 (worth 2 Bytecoins)¶

# Let's make a new class called House that where you have to provide the following
# attributes in the __init__ function:

#     address,
#     style, (see this list for inspiration)
#     yearBuilt
#     numUnits(are there rental units in the property?)
#     numFloors(how many floors does it have?)
#     marketValue

# You should also include the following attributes AND provide methods to change
# the values of

# doorsLocked
# windowsClosed


class House:
    def __init__(self, address, style, yearBuilt, numUnits, numFloors, marketValue):
        self.address = address
        self.style = style
        self.yearBuilt = yearBuilt
        self.numUnits = numUnits
        self.numFloors = numFloors
        self.marketValue = marketValue
        self._doorsLocked = False  # protected
        self._windowsClosed = True  # protected

    def __str__(self):
        output = self.address + ", "
        output += self.style + ", "
        output += str(self.yearBuilt) + ", "
        output += str(self.numUnits) + " units, "
        output += str(self.numFloors) + " floors, "
        output += '${:9,.2f}'.format(self.marketValue)
        return output

    # Added for Question 2.
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

print()
home2 = House("22 Acacia Avenue", "Townhouse", "1825", 1, 4, 250000)
print(home2)
print("\n" + home.address + " < " + home2.address + ": ", home < home2)
assert (home < home2) == True

# Question 3 (worth 2 Bytecoins)

# Create a subclass of the House class called LakeHouse that inherits
# the attributes from the House class, but also includes the following attributes:

#     * 'numUnits' should be overriden to always have only 1 unit
#     * 'boatStatus', whose values can be docked or not docked
#     * 'isRented', whose values are TRUE or FALSE depending on whether the
#       vacation house is rented or not. Make sure you write methods for modifying these values!


class LakeHouse(House):
    def __init__(self, address, style, yearBuilt, numFloors, marketValue):
        House.__init__(self, address, style, yearBuilt,
                       1, numFloors, marketValue)
        self.boatStatus = False
        self.isRented = False

    def __str__(self):
        output = self.address + ", "
        output += self.style + ", "
        output += str(self.yearBuilt) + ", "
        output += str(self.numFloors) + " floors, "
        output += '${:9,.2f}'.format(self.marketValue) + ", "
        output += ("rented, " if self.isRented == True else "not rented, ")
        output += ("boat docked" if self.boatStatus ==
                   True else "boat not docked")
        return output

    def isLakeHouseRented(self):
        return self.isRented

    def rent(self):
        self.isRented = True

    def vacate(self):
        self.isRented = False

    def isBoatDocked(self):
        return self.boatStatus

    def dockBoat(self):
        self.boatStatus = True

    def sailAway(self):
        self.boatStatus = False


lakeHouse = LakeHouse("565 North Clinton Drive", "Ranch", "1948", 2, 175000)
print()
print(lakeHouse)

print("default")
print("Are the doors locked?   ", lakeHouse.areDoorsLocked())
print("Are the windows closed? ", lakeHouse.areWindowsClosed())
assert lakeHouse.areDoorsLocked() == False
assert lakeHouse.areWindowsClosed() == True
print("\nlockDoors(), openWindows()")
lakeHouse.lockDoors()
lakeHouse.openWindows()
print("Are the doors locked?   ", lakeHouse.areDoorsLocked())
print("Are the windows closed? ", lakeHouse.areWindowsClosed())
assert lakeHouse.areDoorsLocked() == True
assert lakeHouse.areWindowsClosed() == False
print("\nunlockDoors(), closeWindows()")
lakeHouse.unlockDoors()
lakeHouse.closeWindows()
print("Are the doors locked?   ", lakeHouse.areDoorsLocked())
print("Are the windows closed? ", lakeHouse.areWindowsClosed())
assert lakeHouse.areDoorsLocked() == False
assert lakeHouse.areWindowsClosed() == True

print("\nLakeHouse specific")
print("Is it rented?           ", lakeHouse.isLakeHouseRented())
print("Is there a boat docked? ", lakeHouse.isBoatDocked())
assert lakeHouse.isLakeHouseRented() == False
assert lakeHouse.isBoatDocked() == False
print("\nrent and dock a boat.")
lakeHouse.rent()
lakeHouse.dockBoat()
print("Is it rented?           ", lakeHouse.isLakeHouseRented())
print("Is there a boat docked? ", lakeHouse.isBoatDocked())
assert lakeHouse.isLakeHouseRented() == True
assert lakeHouse.isBoatDocked() == True
print("\nvacate and sail away")
lakeHouse.vacate()
lakeHouse.sailAway()
print("Is it rented?           ", lakeHouse.isLakeHouseRented())
print("Is there a boat docked? ", lakeHouse.isBoatDocked())
assert lakeHouse.isLakeHouseRented() == False
assert lakeHouse.isBoatDocked() == False
