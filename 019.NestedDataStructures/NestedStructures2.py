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
          "percentage": 70.0
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


# --------------------------------------------
# 📌 Beginner
# --------------------------------------------

# Print the name and studentId of the first student.
#print(mydata[0]["studentProfile"]["personalInfo"]["name"])
#print(mydata[0]["studentProfile"]["personalInfo"]["studentId"])
# Count the number of hobbies for the second student.
#print(len(mydata[1]["studentProfile"]["hobbies"]))
# Add "Photography" to the first student’s hobbies.
#mydata[0]["studentProfile"]["hobbies"].append("Photography")
#print(mydata[0]["studentProfile"]["hobbies"])
# Remove "Swimming" from the second student’s hobbies.
#mydata[1]["studentProfile"]["hobbies"].pop("swimming")
#print(mydata[1]["studentProfile"]["hobbies"])
# Print the school name and website for the first student’s schoolInfo.
#print(mydata[0]["studentProfile"]["schoolInfo"]["name"])
#print(mydata[0]["studentProfile"]["contact"]["website"])
# Verify if the first student’s countryInfo.timezone is "IST (UTC+5:30)".
#if mydata[0]["countryInfo"]["timezone"]=="IST (UTC+5:30)":
#  print("true")
#else:
 # print("false")
# Print the nationality of the second student.
#print(mydata[1]["countryInfo"]["name"])
# List all languages for the first student.
#print(mydata[0]["studentProfile"]["personalInfo"]["languages"])
# Print the email from schoolInfo.contact for the second student.
#print(mydata[1]["schoolInfo"]["contact"]["email"])
# Check if the second student’s schoolInfo.accreditation is "IB".
#if mydata[1]["schoolInfo"]["accreditation"]=="IB":
#  print("True")
#else:
  #print("False")
# --------------------------------------------
# 📌 Intermediate
# --------------------------------------------

# Update the progress.percentage for the first student based on modulesCompleted and totalModules.
#mydata[0]["studentProfile"]["academicInfo"]["progress"]["percentage"]=mydata[0]["studentProfile"]["academicInfo"]["progress"]["modulesCompleted"]/mydata[0]["studentProfile"]["academicInfo"]["progress"]["totalModules"]*100
#print(mydata[0]["studentProfile"]["academicInfo"]["progress"]["percentage"],"%")
# List all modules with a score above 85 for the second student.
#mydata[1]["studentProfile"]["academicInfo"]["grades"][0]=89
#mydata[1]["studentProfile"]["academicInfo"]["grades"][1]=87
#mydata[1]["studentProfile"]["academicInfo"]["grades"][2]=94
#print(mydata[1]["studentProfile"]["academicInfo"]["grades"][0],"%")
#print(mydata[1]["studentProfile"]["academicInfo"]["grades"][1],"%")
#print(mydata[1]["studentProfile"]["academicInfo"]["grades"][2],"%")
# Append a new grade for "Python" with a score of 89 to the first student’s grades.
#mydata[0]["studentProfile"]["academicInfo"]["grades"].append({"module":"Python","score":89})
#print(mydata[0]["studentProfile"]["academicInfo"]["grades"][3])
# Calculate the average score from grades for the second student.
#add=mydata[1]["studentProfile"]["academicInfo"]["grades"][0]+mydata[1]["studentProfile"]["academicInfo"]["grades"][1]+mydata[1]["studentProfile"]["academicInfo"]["grades"][2]
#print(add/3,"%")
# Format the first student’s address as a single string.
#print(str(mydata[0]["studentProfile"]["personalInfo"]["contact"]["address"]["street"]))
# Delete the coordinates field from schoolInfo.location for the first student.
#mydata[0]["schoolInfo"]["location"].pop("coordinates")
#print(mydata[0]["studentProfile"]["schoolInfo"]["location"])
# Update the second student’s age to 15.
#mydata[1]["studentProfile"]["personalInfo"]["age"]=15
#print(mydata[1]["studentProfile"]["personalInfo"]["age"])
# List all extracurricular activities and their roles for the first student.
#print(mydata[0]["studentProfile"]["hobbies"])
# Calculate the number of classes missed for the second student.
#print(mydata[1]["studentProfile"]["academicInfo"]["attendance"]["totalClasses"]-mydata[1]["studentProfile"]["academicInfo"]["attendance"]["classesAttended"])
# Print all cultural highlights for the second student.
#print(mydata[1]["countryInfo"]["culturalHighlights"])
# --------------------------------------------
# 📌 Advanced
# --------------------------------------------

# Check if the pincode in studentProfile.personalInfo.contact.address matches schoolInfo.location.pincode for the first student.
#if mydata[0]["studentProfile"]["personalInfo"]["contact"]["address"]["pincode"]==mydata[0]["studentProfile"]["schoolInfo"]["location"]["pincode"]:
#  print("match")
#else:
#  print("not match")
# Add a new extracurricular activity for "Debate Club" with role "Speaker" and activeSince "2025-03-01" to the second student.

# Count total achievements across all extracurricular activities for both students.

# Find the student with the highest attendancePercentage.
#if mydata[0]["studentProfile"]["academicInfo"]["attendance"]["attendancePercentage"]>mydata[1]["studentProfile"]["academicInfo"]["attendance"]["attendancePercentage"]:
#  print("Ananya has a higher attendance percentage")
#else:
#  print("Liam has a higher attendance percentage")
# Verify if all activeSince dates in extracurricular activities for both students are before 2025-06-07.
