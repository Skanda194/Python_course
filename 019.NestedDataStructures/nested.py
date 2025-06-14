myData = {
    "Student":{
        "Name":"Skanda",
        "Age":12,
        "Course":"Python",
        "Hobbies":["Cricket","Video games","Coding","Music",{
            "Sad":"Low freq",
            "Base":"Medium freq",
            "Rock":"High Freq"
        }]
    },
    "Country":"India",
    "Pincode":123456,
    "States":["Haryana","Punjab","Tamilnadu","Karnatka"]
}


# Get me the country name
# print(myData.get("Country"))

# print(myData['Country'])

# get me the Student name 
print(myData['Student']['Name'])

# Get me the course name
print(myData['Student']['Course'])

# Get me the Video games Hobby of the student
print(myData["Student"]['Hobbies'][1])


# Add Singing to Hobbies
# myData['Student']['Hobbies'].append("Singing")
# print(myData['Student']['Hobbies'])

# Get me the Medium freq 
print(myData['Student']['Hobbies'][4]['Base'])

# get me TamilaNadu State
print(myData['States'][2])


# Update the Course name to Online Python Course
myData['Student']['Course']= "Online Python Course"

print(myData['Student']['Course'])


# Medium Freq to Moderate freq
myData['Student']['Hobbies'][4]['Base'] = "Moderate Freq"
print(myData['Student']['Hobbies'][4]['Base'])