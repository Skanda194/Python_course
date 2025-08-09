# School Management System
from abc import ABC
import os
import json

# Industry -- OOPS 

# Student , Teacher , Principal
# Details -- Marks , Subject teacher 

# Teacher -- Class , Subjects , Grade a student 

# Principal -- Add remove teacher , Student ,Subject -- Drawing , Assign subject to a teacher , Class assigment
class User(ABC):
    def __init__(self,username, password, name, user_type):
        self.username = username
        self.password = password
        self.name = name 
        self.user_type = user_type
        self.filename = f"{user_type}_data.json"
    
    def save_user(self):
        data = {}

        if os.path.exists(self.filename):
            with open(self.filename ,'r') as f:
                data = json.load(f)

        user_data ={
            'password':self.password,
            'name':self.name
        }

        data[self.username]=user_data

        with open(self.filename,'w') as f :
            json.dump(data,f,indent=4)
    
    @abstractmethod
    def show_menu(self):
        pass


class Teacher(User):
    def __init__(self,username,password,name):
        super().__init__(username, password,name , "Teacher")
    
    def save_user(self):
        data = {}

        if os.path.exists(self.filename):
            with open(self.filename ,'r') as f:
                data = json.load(f)
        user_data ={
            'password':self.password,
            'name':self.name,
            'role':"Principal"
        }

        data[self.username] =user_data

        with open(self.filename,'w') as f :
            json.dump(data,f,indent=4)
        
    def show_menu(self):
        while True:
            print("-------------- Teacher Menu ---------------")
            print("1. View Assigned task")
            print("2. View Students in the class")
            print("Add Students Marks")
            print("Logout")

            choice = input("Enter Choice:")
            if choice =="1":
                self.view_assigned_tasks()
            elif choice =="2":
                self.View_students()
            elif choice =="3":
                self.Add_students_marks()
            elif choice =="4":
                print("Logging Out .....")
                break 
            else:
                print("Invlaid Choice")
    
    def view_assigned_classes(self):
        with open(self.fielname , 'r') as f:
            data = json.load()
            classes = data.get(self.username, {}).get('classes',[])
            print("\n Assigned Classes -------")
            for class_name in classes:
                print("Class: ",{class_name})
    
    def View_students(self):
        class_name = input("Enter the class name : ")

        print("\n Students in ",class_name)
        if os.path.exists('student_data.json'):
            with open('student_data.json','r') as f:
                data = json.load(f)
                for username , info in data.items():
                    if info.get('class')==class_name:
                        print(f'Student :{info['name']}')

    
    def Add_students_marks():
        student_username = input("Enter Student name")

        student_data ={}

        if os.path.exists('student_data.json'):
            with open('student_data.json', 'r') as f:
                student_data= json.load(f)

        if student_username not in student_data:
            print("Student not found")
            return 
        
        subject = input("Eneter the subject name: ")
        marks = input("Enter the marks : ")

        if 'marks' not in student_data[student_username]:
            student_data[student_username]['marks'] = []
        student_data[student_username]['marks'].append({

            'subject':subject,
            'marks':marks
        })

        with open('student_data.json', 'r') as f:
            json.dump(student_data, f, indent=4)

        print("Marks added Successfully")

    
class Principal(User):
    def __init__(self,username,password,name):
        super().__init__(username, password,name , "Principal")
    
    def save_user(self):
        data = {}

        if os.path.exists(self.filename):
            with open(self.filename ,'r') as f:
                data = json.load(f)
        user_data ={
            'password':self.password,
            'name':self.name,
            'role':"Principal"
        }

        data[self.username]=user_data
        with open(self.filename,'w') as f :
            json.dump(data,f,indent=4)
        
    def show_menu(self):
        while True:
            print("----- Principal Menu --------")
            print("1. View All Data , 2. Assign class to teacher, 3. Logout")

            choice = input("Enter Choice:")
            if choice =="1":
                self.veiw_all_Data()
            elif choice =="2":
                self.assign_class_teacher()
            elif choice =="3":
                print("Logged Out as Principal")
                break
            else:
                print("Invlaid Choice")

    def veiw_all_Data(self):
        print("---- ALL THE SYSTEM INFORMATION ------")

        for filename in ['principal_data.json','teacher_data.json','student_data.json']:
            if os.path.exists(filename):
                    with open(filename , 'r') as f:
                        data = json.load(f)
                        print(f"\n File: {filename}")
                        print(json.dups(data,indent=4))
                        print("-"*40)
        

        def assign_class_teacher(self):
            teacher_username = input("Enter Teacher Username:")
            teacher_data = {}

            if os.path.exists('teacher_data.json'):
                with open('teacher_data.json','r') as f:
                    teacher_data= json.load(f)

            if teacher_username not in teacher_data:
                print("Teacher not found")
                return
            
            class_name = input("Enter the class to assign")
            if 'classes' not in teacher_data[teacher_username]:
                teacher_data[teacher_username]['classes'] = []
            
            teacher_data[teacher_username]['classes'].append(class_name)

            with open('teacher_data.json','w') as f:
                json.dump(teacher_data,f , indent=4)
            print(f"Class {class_name} is assigned to {teacher_username}")

class Student(User):

    def __init__(self,username,password,name,class_name):
        super().__init__(username, password,name , "Student")
        self.class_name = class_name
    
    def save_user(self):
        data = {}

        if os.path.exists(self.filename):
            with open(self.filename ,'r') as f:
                data = json.load(f)
        
        user_data ={
            'password':self.password,
            'name':self.name,
            'role':"Student",
            'class':self.class_name,
            'marks':[]
        }

        data[self.username]=user_data
        with open(self.filename,'w') as f :
            json.dump(data,f,indent=4)
    
    def show_menu(self):
        while True:
            print("-------------- Student Menu ---------------")
            print("1. View Teacher Details")
            print("2. View Marks")
            print("3. Logout")

            choice = input("Enter Choice:")
            if choice =="1":
                self.view_teacher()
            elif choice =="2":
                self.View_marks()
            elif choice =="3":
                print("Logging Out .....")
                break 
            else:
                print("Invlaid Choice")



class SchoolManagementSystem:
    @staticmethod
    def signup():
        print("\n ========= Create an Account ======= \n")
        print("Choose your Role: 1- Principal , 2-Teacher , 3-Student")

        user_choice = input("Enter your choice: (1-3)")
        username = input("Enter Username: ")
        password = input("Enter password :")
        name = input("Enter your name: ")

        if user_choice =='1':
            user = Principal(username, password, name)
        elif user_choice=='2':
            user = Teacher(username, password , name)
        elif user_choice =='3':
            class_name = input("Enter your Class: ")
            user = Student(username, password,name,class_name)
        else:
            print("Invlaid Choice")
            return SchoolManagementSystem.signup()

        user.save_user()
        print("\n ------- Account Created ------ \n")
        return SchoolManagementSystem.login()

    @staticmethod
    def login():
        print("\n ===== Login =======\n") 
        username = input("Enter Username: ")
        password = input("Enter password :")

        user_type = None
        user_data = None

        for file in ['principal_data.json', 'teacher_data.json','student_data.json']:
            if os.path.exists(file):
                with open(file,'r') as f:
                    data = json.load(f)
                    if username in data and data[username]['password'] == password:
                        user_data = data[username]
                        user_type=file.split('_')[0]
                        break
        if not user_data:
            print("Invlaid Username or Password")
            return SchoolManagementSystem.login()
        
        if user_type=="principal":
            user = Principal(username, password, user_data['name'])
        elif user_type=="teacher":
            user = Teacher(username, password, user_data['name'])
        elif user_type=="student":
            user = Student(username, password, user_data['name'],user_data['class'])


        user.show_menu()


if __name__== '__main__':
    print("""Select your Role:
          1. Principal
          2. Teacher 
          3. Student
""")
    role = input("Enter your choice: (1-3)")

    if role=='1':
        SchoolManagementSystem.login()
    elif role =='2':
        SchoolManagementSystem.login()
    elif role=='3':
        SchoolManagementSystem.login()
    else:
        print("Invalid Choice")
    
