# try:
#   with open("attendees.txt", "r") as file:
#     content = file.read()
#     print(content);
# except FileNotFoundError:
#   print("file does not exist")
# except:
#   print("an error occurred");


def addAttendee():
  nameOfAttendee = input("Enter the name of the attendee: ")
  with open("attendees.txt", "a") as file:
    file.write(f"{nameOfAttendee}\n")

# addAttendee()

def getAttendees():
  with open("attendees.txt", "r") as file:
    content = file.read()
    print(content)

# getAttendees()

def getTop10Attendees():
  with open("attendees.txt", "r") as file:
    content = file.readlines()
    top10 = content[:10]
    i = 0
    while i < len(top10):
      print(f"{i + 1}. {top10[i]}", end="")
      i = i + 1

getTop10Attendees()
