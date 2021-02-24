names = []
marks = []
while True:
    print(" student no " + str(len(names)+1))
    student =input()
    print("marks scored "+ str(len(marks)+1))
    score =input()
    if student == '':
        break
    
    names = names + [student]
    marks = marks + [score]
 #   print(names)
#    print(marks)
print("marks list is: " )
for students in names:
    print(marks)
    print(str(students) +" has got "+ str(marks) +"marks")
