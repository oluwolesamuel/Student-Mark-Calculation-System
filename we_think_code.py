## firstly, read the files and store them as dictionary value pairs


exam_file = open ('Exam_results.txt','r')     ## line opens the text file and sets it to read only mode

exam_marks = {}               # name of dictionary to store studentname and exam mark values pairs
            

for line in exam_file.readlines():        ## since each row represents student name and score, we simply read line by line

    line=line.strip()                ## removes whitespaces after each pai of values

    (key, val) = line.split('-')     ## indicates that the studentnames and marks are seperated by '-' symbol
    
    exam_marks[key]= int(val)             ## splits the values in the txt files into key and value pairs

##we can also decide the datatype to store as value by indicating it (can be float, int, string, etc)
exam_file.close()


#we basically repeat same process for the group_project and daily exercises files

group_file = open ('group_project.txt', 'r')

project_marks = {}

for line in group_file.readlines():
    
    line = line.strip()

    (key, val) = line.split('-')
    
    project_marks[key] = int(val)

group_file.close()

exercises_file = open ('Daily_exercises.txt', 'r')

exercise_marks = {}

for line in exercises_file.readlines():
    
    line = line.strip()

    (key, val) = line.split('-')
    
    exercise_marks[key] = int(val)

exercises_file.close()

user_name = str(input("Enter username: "))      # prompts the user to enter student name/number

exam_mark = exam_marks[user_name]               # retrieves the mark that corresponds to student's username

project_score = project_marks[user_name]

exercise_score = exercise_marks[user_name]

Final_results = ((exam_mark/100)*60)+project_score+((exercise_score/30)*20)

Average = (Final_results/100)*10

print("Exam mark is ", (exam_mark/100)*60, " out of 60")

print("Group project mark is", project_score, " out of 20")

print("Daily exercise mark is", (exercise_score/30)*20, " out of 20")

print(Final_results)

print(Average)

##### Conditional statement to determine if student has passed or failed
if (Final_results>=80 and Final_results<90):    
    print ("Normal Pass")    
elif(Final_results>=90):
    print ("First Class Pass")
else:
    print ("Fail")






