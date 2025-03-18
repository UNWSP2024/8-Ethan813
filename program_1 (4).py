# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):

    nameList = personsName.strip().split()
    for string in nameList:
        personsInitials = ''.join([name[0].upper() for name in nameList])
    #    Add your logic here

    return personsInitials

personsName = input('Enter the users first, middle, and last name')

initials = (initials_generator(personsName))

print(initials)
#ethan collins 3/17/2025 initials generator