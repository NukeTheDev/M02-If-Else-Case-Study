import os

# Author Name: Charles Phillips
# Program name: College Student Class Ranking
# This program accepts a student's last name and first name,
# and then prints out where that student ranks in their class based on their GPA.


exitString = 'ZZZ'  # Customizable string to exit the program


def student_info():
    while True:
        last_name = input("Enter student's last name (or ZZZ to quit): ")
        if last_name == 'ZZZ':
            break
        elif not last_name.isalpha():
            os.system('cls')
            print("Error: Last name can only contain letters.")
            continue
        first_name = input("Enter student's first name: ")
        if not first_name.isalpha():
            os.system('cls')
            print("Error: First name can only contain letters.")
            continue
        while True:
            try:
                gpa = float(input("Enter student's GPA: "))
                if gpa < 0 or gpa > 4:
                    raise ValueError
                break
            except ValueError:
                os.system('cls')
                print("Invalid input. GPA must be a float between 0 and 4.")
        if gpa >= 3.5:
            print(f"{first_name}, {last_name} made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name}, {last_name} made the Honor Roll!")
        else:
            print(f"{first_name}, {last_name} did not qualify for Dean's List or Honor Roll.")
    exit()


student_info()
