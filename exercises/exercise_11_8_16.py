# create a dictionary from info
def dict(listoflist):
    """ list[list] -> dict """
    namelist = []
    gradelist = []
    final_dict = {}

    for l in listoflist:
        student_grades = []
        for i in range(len(l)):
            if l[i].isdigit():
                student_grades.append(int(l[i]))
            else:
                namelist.append(l[i])
        gradelist.append(student_grades)

    for i in range(len(namelist)):
        final_dict[namelist[i]] = gradelist[i]
    return final_dict


student_list = []
# get number of students, their names, and their grades
student_num = int(input("How many students? "))
for i in range(student_num):
    student = input(
        "Please enter a student name and grades, separated by spaces.\n").split(
            ' ')
    student_list.append(student)
# dictionary of lists
student_dict = dict(student_list)
# find and print class average
grade_sum = 0
full_len = 0
highest_grade = 0
highest_name = []
for key in student_dict:
    full_len += len(student_dict[key])
    for i in range(len(student_dict[key])):
        grade_sum += student_dict[key][i]
        if student_dict[key][i] > highest_grade:
            highest_grade = student_dict[key][i]
            highest_name.append(key)
class_average = grade_sum / full_len
print("Class Average: ", class_average)
# print highest grade
print("Highest Grade: ", highest_name[-1], highest_grade)
