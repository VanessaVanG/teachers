'''This challenge has several steps so take your time, read the instructions carefully, and feel free to experiment in Workspaces or on your own computer.
For this first task, create a function named num_teachers that takes a single argument, which will be a dictionary of Treehouse teachers and their courses.
The num_teachers function should return an integer for how many teachers are in the dict.'''
# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.
def num_teachers(teach_dict):
    #return how many teachers are in the dictionary
    return len(teach_dict)

'''Create a new function named num_courses that will receive the same dictionary as its only argument.
The function should return the total number of courses for all of the teachers.'''
def num_courses(teach_dict):
    #initialize count
    course_num = 0
    #iterate through each key ie teacher in the dictionary
    for teacher in teach_dict:
        #iterate through each item in the value (ie course) lists
        for course in teach_dict[teacher]:
            #increment course_num
            course_num += 1
    return course_num

'''For this step, make another new function named courses that will, again, take the dictionary of teachers and courses.
courses, though, should return a single list of all of the available courses in the dictionary. No teachers, just course names!'''
def courses(teach_dict):
    #make a list
    class_list = []
    #Iterate through each key ie teacher in the dictionary
    for teacher in teach_dict:
        #Iterate through each item in the value (ie course) lists
        for course in teach_dict[teacher]:
            #add each to the list
            class_list.append(course)
    return class_list

'''Create a function named most_courses that takes our good ol' teacher dictionary.
most_courses should return the name of the teacher with the most courses. You might need to hold onto some sort of max count variable.'''
   
def most_courses(teach_dict):
    #make a variable for most
    most = 0
    #iterate through the the dictionary items
    for teacher,courses in teach_dict.items():
        #compare the length of the courses to the most variable
        if len(courses) > most:
            #most becomes the largest length so far
            most = len(courses)
            #the key(i.e. teacher) becomes name
            name = teacher
    return name        

'''In this last challenge, I want you to create a function named stats and it'll take our teacher dictionary as its only argument.
stats should return a list of lists where the first item in each inner list is the teacher's name and the second item is the number of courses that teacher has. For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]'''

def stats(teach_dict):
    #make a list of lists list
    list_of_lists = []
    #iterate through the items in the dictionary
    for teacher,courses in teach_dict.items():
        #make a list with the teacher and the # of courses
        single_list = [teacher, len(courses)]
        #add that list to lol list
        list_of_lists.append(single_list)
    return list_of_lists