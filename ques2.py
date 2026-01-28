#3day tech fest organised, take 3 inputs 
'''
1. Event Deets : event_id, event_name, max_participants [for eg : (101,"hackathon",5), (102,"Quiz",3)]
2. Registration Deets : event_id: {registration_id of diff students}... similar for other two, dicitionary
{101: 1001,1002} 
3. Student Deets : {registration_id: studemt_name, branch}
name, branch, event id, registration id


TASKS : 
1. list of event names that crossed 50% of max participants.
2. Add a new registration for student.
3. Remove a registered student 
4. List student names who have registered in more than one event. 
5. For each event, make a dictionary "event name": "vacant seats"
6.Display top 1 event 

'''
'''--------------------------------------------------------------------------'''
#Admin

'''total_events = int(input("Total number of events: "))

def admin():
    events = []

    for i in range(total_events):
        event_id = int(input("Enter event_id: "))
        event_name = input(f"Enter event name for id {event_id}: ").upper()
        max_participants = int(input(f"Enter max participants for {event_id}: "))

        events.append({
            "event_id": event_id,
            "event_name": event_name,
            "max_participants": max_participants
        })

    return events

all_events = admin()
print(all_events)
'''
# User 

# eventnumber = int(input("enter number of events: "))
# event = [] 
# name  = []
# part = []
# fdic = {}

# #event details

# for i in range(eventnumber):
#     eventID = input("enter event id: ")
#     eventName = input("enter event name: ")
#     maxp = int(input("enter max participants: "))
    

#     event.append(eventID)
#     name.append(eventName)
#     part.append(maxp)

# #student details
# inlist = []
# totstu = int(input("enter the total number of students participating in the fest: "))
# for i in range(totstu):
   
#     inlist = []
#     regID = input("enter registration ID: ")
#     studentName = input("enter Name: ")
#     branch = input("enter branch: ")
#     inlist.append(studentName)
#     inlist.append(branch)

#     fdic[regID] = inlist
# twodic = {}

# #registration

# for i in event:
#     list2 = []
#     particiants = int(input("number of participants: "))
#     print(f"write regisrtaion ids for participants in the event {i} : ")
#     for j in range(particiants):
#         partid = int(input("enter your regid: "))
#         list2.append(partid)
#     twodic[i] = list2

eventnumber = int(input("enter number of events: "))
event = []       
name = []        
max_participants = []        
reg_name_branch = {}  
event_reg_id = {}     

# event details
for i in range(eventnumber):
    eventID = input("enter event id: ")
    eventName = input("enter event name: ")
    maxp = int(input("enter max participants: "))
    
    event.append(eventID)
    name.append(eventName)
    max_participants.append(maxp)
    
# student details
total_students = int(input("enter total number of students: "))

for i in range(total_students):
    inlist = []
    regID = input("enter registration ID: ")
    studentName = input("enter Name: ")
    branch = input("enter branch: ")

    inlist.append(studentName)
    inlist.append(branch)

    reg_name_branch[regID] = inlist


#registration details
for i in event:
    list2 = []
    participants = int(input(f"number of participants in event {i}: "))
    print(f"write registration ids for event {i}:")
    for j in range(participants):
        partid = input("enter regid: ")
        list2.append(partid)
    event_reg_id[i] = list2

#tasks
while True:
    print("\nMenu:")
    print("1. Events that crossed 50% of max participants")
    print("2. Add a new registration")
    print("3. Remove a registered student")
    print("4. List students registered in more than one event")
    print("5. Dictionary: event name -> vacant seats")
    print("6. Display top 1 event")
    print("0. Exit")

    choice = input("Enter choice: ")


    if choice == "1":
        print("\nEvents that crossed 50%:")
        for i in range(len(event)):
            used = len(event_reg_id[event[i]])
            if used > (max_participants[i] / 2):
                print(name[i])


    elif choice == "2":
        even_id = input("enter event id: ")
        reg_id = input("enter registration id: ")

        if even_id not in event:
            print("Event does not exist.")
        else:
            if reg_id not in reg_name_branch:
                print("Student does not exist. Enter details:")
                nm = input("Name: ")
                br = input("Branch: ")
                reg_name_branch[reg_id] = [nm, br]

            idx = event.index(even_id)

            if len(event_reg_id[even_id]) >= max_participants[idx]:
                print("Event full.")
            else:
                if reg_id in event_reg_id[even_id]:
                    print("Already registered.")
                else:
                    event_reg_id[even_id].append(reg_id)
                    print("Registration added.")

    elif choice == "3":
        even_id = input("enter event id: ")
        reg_id = input("enter registration id to remove: ")

        if even_id in event_reg_id and reg_id in event_reg_id[even_id]:
            event_reg_id[even_id].remove(reg_id)
            print("Removed successfully.")
        else:
            print("Not found in this event.")

    elif choice == "4":
        count = {}

        for key in event_reg_id:
            for reg_id in event_reg_id[key]:
                count[reg_id] = count.get(reg_id, 0) + 1

        print("\nStudents in more than one event:")
        for reg_id in count:
            if count[reg_id] > 1:
                print(reg_id, "-", reg_name_branch[reg_id][0], "-", reg_name_branch[reg_id][1])

    elif choice == "5":
        vacant = {}
        for i in range(len(event)):
            used = len(event_reg_id[event[i]])
            vac = max_participants[i] - used
            vacant[name[i]] = vac

        print("\nVacant seats:")
        for k, v in vacant.items():
            print(k, ":", v)

    elif choice == "6":
        top_index = -1
        top_count = -1

        for i in range(len(event)):
            used = len(event_reg_id[event[i]])
            if used > top_count:
                top_count = used
                top_index = i

        print("\nTop Event:")
        print("Event name:", name[top_index])
        print("Participants:", top_count)
        print("Max participants:", max_participants[top_index])

    elif choice == "0":
        break

    else:
        print("Invalid choice.")
