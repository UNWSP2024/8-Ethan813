# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
courses = {}
number_of_courses = int(input('how many courses will you enter? '))
for number in range(number_of_courses):
    new_key = input('please enter a course ID ')
    new_name = input('please enter a course name that fits with the ID ')
    courses[new_key] = [new_name]

key_search = input('please enter a subject to search ')
for subject in courses:
    if key_search in subject:
        print(courses[subject])
# ethan collins 3/18/2025 course dictionary