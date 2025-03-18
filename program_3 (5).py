# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random
correct = 0
incorrect = 0
countries = {'United States':'washington d.c.','New Zealand':'wellington','Mexico':'mexico city','Canada':'ottawa','South Africa':'cape town','Japan':'tokyo','Norway':'oslo','Sweden':'stockholm','Iceland':'reykjavik','Germany':'berlin'}
while correct < 10:
    key = random.choice(list(countries.keys()))
    capital = countries[key]
    print('what is the capital of',key,'?')
    answer = input()
    if answer == capital:
        correct += 1
    else:
        incorrect += 1
print('you got', correct,'questions right', ' you got', incorrect, 'questions wrong')
#ethan collins 3/17/2025 quiz of the capitals from countries I have been to or want to go.


