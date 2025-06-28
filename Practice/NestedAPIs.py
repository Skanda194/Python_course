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
#myData['data']['studentProfile']['academicInfo']['grades']['module'].append("Algorithms")
#print(myData['data']['studentProfile']['academicInfo']['grades']['module'])
# Calculate the average score from academicInfo.grades.
#print((86+87+87+88)/5)


mydata= [
  {
    "studentProfile": {
      "personalInfo": {
        "name": "Ananya Patel",
        "age": 13,
        "grade": 8,
        "studentId": "STU789012",
        "dateOfBirth": "2012-07-22",
        "nationality": "Indian",
        "languages": ["English", "Gujarati", "Hindi"],
        "contact": {
          "email": "ananya.patel@example.com",
          "phone": "+91-8765432109",
          "address": {
            "street": "45 Sardar Road",
            "city": "Ahmedabad",
            "state": "Gujarat",
            "country": "India",
            "pincode": 380001
          },
          "emergencyContact": {
            "name": "Ravi Patel",
            "relationship": "Father",
            "phone": "+91-9012345678"
          }
        }
      },
      "academicInfo": {
        "course": "Web Development",
        "enrollmentDate": "2024-08-15",
        "progress": {
          "modulesCompleted": 10,
          "totalModules": 25,
          "percentage": 40.0
        },
        "grades": [
          {"module": "HTML", "score": 88},
          {"module": "CSS", "score": 82},
          {"module": "JavaScript", "score": 90}
        ],
        "attendance": {
          "totalClasses": 60,
          "classesAttended": 57,
          "attendancePercentage": 95.0
        }
      },
      "hobbies": ["Painting", "Dance", "Coding", "Reading"],
      "extracurricular": [
        {
          "activity": "Dance Club",
          "role": "Choreographer",
          "achievements": ["First Place in State Competition 2024"],
          "activeSince": "2023-09-10"
        },
        {
          "activity": "Art Club",
          "role": "Member",
          "achievements": [],
          "activeSince": "2024-02-20"
        }
      ]
    },
    "schoolInfo": {
      "name": "Sunrise International School",
      "type": "Private",
      "established": "2010",
      "accreditation": "CBSE",
      "location": {
        "city": "Ahmedabad",
        "state": "Gujarat",
        "country": "India",
        "pincode": 380001,
        "coordinates": {
          "latitude": 23.0225,
          "longitude": 72.5714
        }
      },
      "contact": {
        "email": "info@sunrise.edu.in",
        "phone": "+91-7923456789",
        "website": "https://www.sunrise.edu.in"
      },
      "facilities": ["Art Studio", "Dance Hall", "Computer Labs", "Library"]
    },
    "countryInfo": {
      "name": "India",
      "capital": "New Delhi",
      "officialLanguage": ["Hindi", "English"],
      "currency": "Indian Rupee (INR)",
      "timezone": "IST (UTC+5:30)",
      "culturalHighlights": ["Vibrant textile traditions", "Gujarati folk dance Garba"]
    }
  },
  {
    "studentProfile": {
      "personalInfo": {
        "name": "Liam Chen",
        "age": 14,
        "grade": 9,
        "studentId": "STU345678",
        "dateOfBirth": "2011-03-10",
        "nationality": "Singaporean",
        "languages": ["English", "Mandarin", "Malay"],
        "contact": {
          "email": "liam.chen@example.com",
          "phone": "+65-91234567",
          "address": {
            "street": "12 Orchard Lane",
            "city": "Singapore",
            "state": "",
            "country": "Singapore",
            "pincode": 238863
          },
          "emergencyContact": {
            "name": "Mei Chen",
            "relationship": "Mother",
            "phone": "+65-98765432"
          }
        }
      },
      "academicInfo": {
        "course": "Robotics",
        "enrollmentDate": "2024-07-01",
        "progress": {
          "modulesCompleted": 12,
          "totalModules": 30,
          "percentage": 40.0
        },
        "grades": [
          {"module": "Mechanics", "score": 85},
          {"module": "Programming", "score": 92},
          {"module": "Sensors", "score": 78}
        ],
        "attendance": {
          "totalClasses": 45,
          "classesAttended": 44,
          "attendancePercentage": 97.8
        }
      },
      "hobbies": ["Robotics", "Chess", "Swimming", "Music"],
      "extracurricular": [
        {
          "activity": "Robotics Club",
          "role": "Team Lead",
          "achievements": ["National Robotics Champion 2024"],
          "activeSince": "2023-05-15"
        },
        {
          "activity": "Chess Club",
          "role": "Member",
          "achievements": ["School Tournament Runner-Up 2024"],
          "activeSince": "2024-01-10"
        }
      ]
    },
    "schoolInfo": {
      "name": "Global Academy Singapore",
      "type": "International",
      "established": "2008",
      "accreditation": "IB",
      "location": {
        "city": "Singapore",
        "state": "",
        "country": "Singapore",
        "pincode": 238863,
        "coordinates": {
          "latitude": 1.3521,
          "longitude": 103.8198
        }
      },
      "contact": {
        "email": "contact@globalacademy.sg",
        "phone": "+65-67891234",
        "website": "https://www.globalacademy.sg"
      },
      "facilities": ["Robotics Lab", "Swimming Pool", "Library", "Auditorium"]
    },
    "countryInfo": {
      "name": "Singapore",
      "capital": "Singapore",
      "officialLanguage": ["English", "Mandarin", "Malay", "Tamil"],
      "currency": "Singapore Dollar (SGD)",
      "timezone": "SGT (UTC+8:00)",
      "culturalHighlights": ["Multicultural festivals", "Advanced technology hub"]
    }
  }
]
# Print the name and studentId of the first student.
print(myData [])
# Count the number of hobbies for the second student.

# Add "Photography" to the first student’s hobbies.

# Remove "Swimming" from the second student’s hobbies.

# Print the school name and website for the first student’s schoolInfo.

# Verify if the first student’s countryInfo.timezone is "IST (UTC+5:30)".

# Print the nationality of the second student.

# List all languages for the first student.

# Print the email from schoolInfo.contact for the second student.

# Check if the second student’s schoolInfo.accreditation is "IB".









