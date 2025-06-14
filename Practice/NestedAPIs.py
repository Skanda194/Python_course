myData= {
  "Tutor": "Arvinder Pal",
  "Mode": "Online",
  "Bootcamp": "Online Python Course",
  "data": {
    "studentProfile": {
      "personalInfo": {
        "name": "Govind Sharma",
        "age": 13,
        "grade": 7,
        "studentId": "STU123456",
        "dateOfBirth": "2012-04-15",
        "nationality": "Indian",
        "languages": ["English", "Hindi", "Kannada"],
        "contact": {
          "email": "govind.sharma@example.com",
          "phone": "+91-9876543210",
          "address": {
            "street": "123 MG Road",
            "city": "Bangalore",
            "state": "Karnataka",
            "country": "India",
            "pincode": 123456
          },
          "emergencyContact": {
            "name": "Priya Sharma",
            "relationship": "Mother",
            "phone": "+91-9123456789"
          }
        }
      },
      "academicInfo": {
        "course": "Python Programming",
        "enrollmentDate": "2024-09-01",
        "progress": {
          "modulesCompleted": 8,
          "totalModules": 20,
          "percentage": 50.0
        },
        "grades": [
          {"module": "Basics", "score": 85},
          {"module": "Functions", "score": 78},
          {"module": "Data Structures", "score": 92}
        ],
        "attendance": {
          "totalClasses": 50,
          "classesAttended": 48,
          "attendancePercentage": 96.0
        }
      },
      "hobbies": ["Cricket", "Video Games", "Coding", "Music", "Chess"],
      "extracurricular": [
        {
          "activity": "Cricket Club",
          "role": "Member",
          "achievements": ["Best Batsman 2024"],
          "activeSince": "2023-06-01"
        },
        {
          "activity": "Coding Club",
          "role": "Junior Developer",
          "achievements": ["Hackathon Winner 2024"],
          "activeSince": "2024-01-15"
        },
        {
          "activity": "Music Club",
          "role": "Vocalist",
          "achievements": [],
          "activeSince": "2024-10-01"
        }
      ]
    },
    "schoolInfo": {
      "name": "Bright Future Academy",
      "type": "Private International School",
      "established": "2005",
      "accreditation": "CBSE",
      "location": {
        "city": "Bangalore",
        "state": "Karnataka",
        "country": "India",
        "pincode": 123456,
        "coordinates": {
          "latitude": 12.9716,
          "longitude": 77.5946
        }
      },
      "contact": {
        "email": "contact@bfa.edu.in",
        "phone": "+91-8001234567",
        "website": "https://www.bfa.edu.in"
      },
      "facilities": ["Science Labs", "Library", "Sports Complex", "Computer Labs"]
    },
    "countryInfo": {
      "name": "India",
      "capital": "New Delhi",
      "officialLanguage": ["Hindi", "English"],
      "currency": "Indian Rupee (INR)",
      "timezone": "IST (UTC+5:30)",
      "culturalHighlights": ["Diverse festivals like Diwali and Holi", "Rich history in mathematics and science"]
    },
    "metadata": {
      "lastUpdated": "2025-06-07T15:30:00Z",
      "source": "Student Management System"
    }
  }
}
#                          BEGINNER
# Print the tutor name , Bootcamp.
#print(myData['Tutor'])
#print(myData['Bootcamp'])
# Print the student’s nationality from studentProfile.personalInfo.
#print(myData['data']['studentProfile']['personalInfo']['nationality'])
# List all languages in studentProfile.personalInfo.languages.
#print(myData['data']['studentProfile']['personalInfo']['languages'])
# Print the school’s contact email from schoolInfo.contact.
#print(myData['data']['schoolInfo']['contact']['email'])
# Check if schoolInfo.accreditation is "CBSE".
#y=myData['data']['schoolInfo']['accreditation']
#if y=="CBSE":
#  print("True")
#else:
#  print("False")
#                           INTERMEDIATE
# Update the progress.percentage in academicInfo based on modulesCompleted and totalModules.Add comment More actions
#myData['data']['studentProfile']['academicInfo']['progress']['percenatge']=40.0
#print(myData['data']['studentProfile']['academicInfo']['progress']['percenatge'])
# List all modules in academicInfo.grades with a score above 85.
#myData['data']['studentProfile']['academicInfo']['grades']['module']['basics']='86'
#myData['data']['studentProfile']['academicInfo']['grades']['module']['Functions']='87'
#myData['data']['studentProfile']['academicInfo']['grades']['module']['Data Structures']='88'
#print(myData['data']['studentProfile']['academicInfo']['grades']['module']['basics'])
#print(myData['data']['studentProfile']['academicInfo']['grades']['module']['Functions'])
#print(myData['data']['studentProfile']['academicInfo']['grades']['module']['Data Structures'])
# Append a new grade for "Algorithms" with a score of 87 to academicInfo.grades.
myData['data']['studentProfile']['academicInfo']['grades']['module'].append("Algorithms")

# Calculate the average score from academicInfo.grades.

# Format the student’s address as a single string.

# Delete the coordinates field from schoolInfo.location.

# Update studentProfile.personalInfo.age to 13.

# List all extracurricular activities with their roles from studentProfile.extracurricular.

# Calculate the number of classes missed based on academicInfo.attendance.

# Print all cultural highlights from countryInfo.culturalHighlights.