# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Areli Diaz, 05/18/26, Created Script
#               05/19/26  Modified Script
# ------------------------------------------------------------------------------------------ #

# Import the json module
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''  # Stores the first name of a student entered by the user.
student_last_name: str = ''  # Stores the last name of a student entered by the user.
course_name: str = ''  # Stores the name of a course entered by the user.
file = None #
menu_choice: str = ''  # Stores choice made by the user
student_data: dict = {}  # one row of student data saved as a dictionary
students: list = []  # a table of student data

# When the program starts, read the file data into a list of lists of dictionaries
try:
    file = open(FILE_NAME, "r") # Extract the data from the file
    students = json.load(file)
    file.close()
except FileNotFoundError as err: # Gives a file not found error incase the file doesn't exist
    print('File not found, please create file and try again\n')
    print("---Error Details---")
    print(err, err.__doc__, type(err), sep='\n') # Prints more technical detail on the errors
except Exception as err: # This covers any other errors that might happen
    print('Non-specific error found.\n')
    print("---Error Details---")
    print(err, err.__doc__, type(err), sep='\n')
finally:
    if file is not None and not file.closed: # Checks if file has content and is closed, if not then it closes the file
        print('File not closed, closing now')
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("Please choice menu choice 1,2,3 or 4: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha(): # Checks to see that the user only used letters
                raise ValueError("Please only use letters when entering student's first name")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha(): # Checks to see that the user only used letters
                raise ValueError("Please only use letters when entering student's last name")

            course_name = input("Please enter the name of the course: ") # no alpha check since course names have #s
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as err: # If the user uses numbers or special characters, an error message will show
            print("---Error Details---")
            print(err, err.__doc__, type(err), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        print('Students currently registered (First Name, Last Name, Course Name): ')
        for student in students:
            print(f"{student["FirstName"]}, {student["LastName"]}, {student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2) # saves the new student information into the json file
            file.close()
        except TypeError as err: # Goes through all the possible errors a user might find
            print('Please make sure that data is in valid JSON format')
            print("---Error Details---")
            print(err, err.__doc__, type(err), sep='\n')
        except Exception as err:
            print('Non-specific error found.\n')
            print("---Error Details---")
            print(err, err.__doc__, type(err), sep='\n')
        finally: # Makes sure the file closes even if there was no error
            if file is not None and not file.closed:
                print('File not closed, closing now')
                file.close()

        print("The following data was saved to the file!")
        for student in students:
            print(f"{student["FirstName"]}, {student["LastName"]}, {student["CourseName"]}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # breaks out of the loop

    else:
        print("Invalid menu choice. Please only choose options 1, 2, 3, or 4")

print("Program Ended")
