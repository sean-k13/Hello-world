# CS1210: QotD1
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) you have not shared it with anyone else.
#
# ToDo: Change the word "hawkid" between the two double quote marks to
# match your own hawkid. Your hawkid is the "login identifier" (not
# your email address) that you use to login to all University
# services.
#
def signed():
    return(["swkingston"])

######################################################################
# Specification: tripCost(distance, mpg, cpg) returns the cost in
# dollars associated with taking a trip of distance miles in a car
# that gets mpg miles per gallon (guaranteed to be > 0) when gasoline
# costs cpg dollars per gallon.
#
# ToDo: Remove the line that says "pass" and replace it with your own
# code. Do not alter the function signature.
#
def tripCost(distance, mpg, cpg):
    cost = distance / mpg * cpg
    return cost
print(tripCost(15, 5, 3))

