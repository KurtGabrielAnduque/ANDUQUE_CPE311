#Student Enrollment Problem
""" You are given a set of N courses.
    Courses will be defined as (code, units).
    Select the maximum set of courses a student can hve.
    Maximum units allowed is based on input with a max of 24
    default of 18. """
from DATASCI.scratch import enrolledClasses


#creating constructor for object
class Lecture:

    def __init__(self, code, units):
        self.code = code #course code
        self.units = units #units

    def getUnits(self):
        return self.units

    def __str__(self): #return the string representation
        return self.code + ': <' + str(self.units) + ' units >'


def buildSched(codes, units): #function for building the sched from the given list
    schedule = [] #create a empty list that will lecture(object)
    for i in range(len(units)): # loop through indices of every list
        schedule.append(Lecture(codes[i],units[i])) # Creation of Lecture(object) and append to schedule list

    return schedule #return the list of Lecture(objects)

def greedy(classes, MaxUnits, keyFunction): # perform greedy algorithm without exceeding the limits
    # classes: Lecture(objects)
    # MaxUnits: given constrain by the units or the maximum allowed units
    # Keyfunction : sorting criteria
    classesCopy = sorted(classes, key = keyFunction, reverse= False) #Sort based on keyfunction  (ascending order)
    result = []

    totalUnits = 0.0 #monitor the total units
    #perform forloop from classcopy
    for i in range(len(classes)):
        if (totalUnits + classesCopy[i].getUnits()) <= MaxUnits: #condition that will check if the total and new units is exceeding the maximum units
            result.append(classesCopy[i]) #if not exceeding append the object to result
            totalUnits += classesCopy[i].getUnits() #update the total units for next loop


    return (result, totalUnits)

# function for testing greedy algorithm and print result
def testGreedy(classes, constraint, keyFunction):
    taken, val = greedy(classes,constraint,keyFunction)
    print('Total units of classes taken = ', val)
    for item in taken:
        print('', item)

# function for running the greedy aglorithm
def testGreedys(Classcodes, MaxUnits = None):
    if MaxUnits is None:
        MaxUnits = 18 # this execute if the user didnt enter constraint, it will automatically set to 18 units
    MaxUnits = min(24, max(0, MaxUnits)) #set to maximum 24 units if the user try to input above 24

    print('Use greedy by value to allocate', MaxUnits, 'units')
    testGreedy(Classcodes, MaxUnits, Lecture.getUnits)

# list of coursecode with corresponding units
courseCode = ['CPE 021','CPE 013','CPE 015A','CPE 021A', 'CPE 302','CPE 311','GEC 002', 'MATH 020', 'PE 004']
units = [2,4,3,1,3,3,3,3,2]
# building the schedule
enrolledClasses = buildSched(courseCode, units)

# executing greedy aglorithm

while True:
    try:
        user = int(input('Enter the number of units you want to enroll: '))
        testGreedys(enrolledClasses,user)
        break

    except ValueError:
        print('invalid input pls input numbers')






