# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(" ")
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
totalheight = 0
for height in student_heights :
	totalheight =+ height

number_students = 0
for student in student_heights :
	number_students =+ 1
print(totalheight / number_students)

#Write your code below this row 👇




