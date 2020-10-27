myUniqueList = []
myLeftovers = []

def addToList(newItem):
    if newItem in myUniqueList:
        addToLeftovers(newItem)
        return False
    else:
        myUniqueList.append(newItem)
        return True

def addToLeftovers(newItem):
    myLeftovers.append(newItem)

# Testing the addToList function
print(myUniqueList)
print(addToList("pizza")) # Returns True
print(myUniqueList)

print(myLeftovers)
# adding a repeated value
print(addToList("pizza")) # Returns False
print(myUniqueList)
print(myLeftovers)
# adding a new element
print(addToList("burguer")) # Returns True
print(myUniqueList)
print(addToList("burguer")) # Returns False
print(myUniqueList)
print(myLeftovers)
# adding a new element
print(addToList("pasta")) # Returns True
print(myUniqueList)
print(myLeftovers)
