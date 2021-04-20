import csv

'''
This is a script we wrote to generate our initial emails to professors
'''


emailText = open("email.txt","r").read()
coursesText = open("profs.csv")
coursesParsed = csv.reader(coursesText)

for row in coursesParsed:
    fullName = row[1][:-4]
    lastName = fullName[fullName.rfind(' '):][1:]
    courseName = row[2].title()
    
    
    if(row[0] == 'Inclusive'):
        numCourses = '28'
    else:
        numCourses = 'four'


    print(emailText % ("Professor "+ lastName,courseName,numCourses,row[0].lower(),row[0].lower()))
    print(";")

