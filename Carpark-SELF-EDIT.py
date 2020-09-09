import calendar
import datetime
from datetime import timedelta
from datetime import date
import sys
import os
clear = lambda: os.system('cls')
os.system("mode con cols=139 lines=30")

studentID = []
fname = []
lname = []
phone = []
email = []
carplate = []
register_date = []
expiry_date = []

status = [] #This we show the parkingID in view all
store = [] #This store the parkingID after the parking SLOT is taken
parklocation = [] #This store the index location of the parkingID list
parkingID = []

userID = []
password = []
user_fname = []
user_lname = []

userID.append("admin") #Default admin user
password.append("1234")
user_fname.append("Rachel")
user_lname.append("Lim")

"""studentID.append("TP038850")
fname.append("Rachel")
lname.append("Lim")
email.append("Chowwenhoe@gmail.com")
carplate.append("WYA4804")
register_date.append("12/05/2016")"""

for n in range(0,15):
    if n < 9:
        parkingID.append("L10"+str(n+1))
    elif n < 15:
        parkingID.append("L1"+str(n+1))

for n in range(15,45):
    if n < 24:
        parkingID.append("L20"+str(n-14))
    elif n < 30:
        parkingID.append("L2"+str(n-14))

for n in range(30,45):
    if n < 39:
        parkingID.append("L30"+str(n-29))
    elif n < 45:
        parkingID.append("L3"+str(n-29))
            
"""                               THIS IS WHERE FUNCTIONS START                                """

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break

    
def menu(): #####################################################################   MENU
    clear()
    print("------- WELCOME TO CARPARK REGISTRATION SYSTEM -------".center(138))
    print("\n1. Add a New Record")
    print("2. Modify a record")
    print("3. Delete a record")
    print("4. Search a record")
    print("5. View All records")
    print("6. Display parking slots")
    print("7. Log out")
    print("8. Quit")
    option=None
    flag=0
    while option !=5:
        
        if flag == 0:
            option = str(input("\nEnter Your Choice: "))
        else:
            option = str(input("Invalid Choice! Please Try Agian: "))
            
        if option == "1":
            add()
                
                
        elif option == "2":
            modify()

                    
        elif option == "3":
            delete()
                
        elif option == "4":
            search()
            
        elif option == "5":
            view_all()

        elif option == "6":
            parkingslot()
            print("\n")
            os.system("pause")
            menu()
            
        elif option == "7":
            home()
            
        elif option == "8":
            print("Goodbye!")
            sys.exit()

        else:
            flag=flag+1

    return 


def parkingslot(): #####################################################################   Display parking slot
    clear()
    print("\nSelect Parking Slot: ")
    print("------- PARKING SLOTS -------".center(138))
    print("\n")
    print("----- LEVEL 1 -----\n".center(138))
    print("   |   ".join(parkingID[0:5]).center(138))
    print("   |   ".join(parkingID[5:10]).center(138))
    print("   |   ".join(parkingID[10:15]).center(138))
    print("\n")
    print("----- LEVEL 2 -----\n".center(138))
    print("   |   ".join(parkingID[15:20]).center(138))
    print("   |   ".join(parkingID[20:25]).center(138))
    print("   |   ".join(parkingID[25:30]).center(138))
    print("\n")
    print("----- LEVEL 3 -----\n".center(138))
    print("   |   ".join(parkingID[30:35]).center(138))
    print("   |   ".join(parkingID[35:40]).center(138))
    print("   |   ".join(parkingID[40:45]).center(138))
    """current = 0
    flag = 0
    for (parkingID[current]) in range(0,46): #Use to check how many empty/taken parkingID in list
        if "****" in parkingID:
            flag += 1
            
    print("{0}/{1}".format((45-flag),("45"))) #Print out the available/total parkingID in list
    current = None
    flag = None""" #####Fail code#####
          
    return


def searchfail(): #####################################################################   Called while searching fail
    print("\nNo RecordS Found")
    print("1. Search Again")
    print("2. Back")
    option=None
    flag=0
    while option !=2:
        
        if flag == 0:
            option = str(input("\nEnter Your Choice: "))
        else:
            option = str(input("Invalid Choice! Please Try Agian: "))

        if option == "1":
            search()
        elif option == "2":
            menu()
        else:
            flag += 1
    return

def add(): #####################################################################   Add new records
    clear()
    print("------- Enter Student's details ------".center(138))
    temp = input("\nEnter Student's TP number: ")
    temp = temp[:1].upper() + temp[1:].capitalize()
    studentID.append(temp)
    tempname = input("Enter Student's First Name: ")
    fname.append(tempname.title())
    tempname = input("Enter Student's Last Name: ")
    lname.append(tempname.title())
    tempname = inputNumber("Enter Student's Mobile Number: ")
    tempname = str(tempname)
    #tempname = input("Enter Student's Mobile Number: ")
    phone.append(tempname)
    
    tempname = input("Enter Student's E-mail address: ")
    email.append(tempname)
    tempname = input("Enter Student's Car Plate Number: ")
    carplate.append(tempname)
    #tempname = int(input("Enter Date of Registration in DD-MM-YYYY format: "))
    #register_date.append(tempname)
    """year = int(input('Enter a year'))
    month = int(input('Enter a month'))
    day = int(input('Enter a day'))
    date1 = datetime.date(year, month, day)
    register_date.append(date1)"""

    date_entry = input('Enter a date in DD-MM-YYYY format: ')
    day, month, year = map(int, date_entry.split('-')) 
    date1 = datetime.date(year, month, day)
    date2 = ("{:%d-%m-%Y}".format(date1))
    register_date.append(date2)
    
    
    end_date = date1 + datetime.timedelta(days=120)
    end_date = ("{:%d-%m-%Y}".format(end_date))
    expiry_date.append(end_date)
    print(expiry_date[0])
    
    parkingslot()
    
    flag=0
    for tempname in parkingID:
        
        if flag == 0:
            tempname = str(input("\nEnter Parking Space ID: "))
            tempname = tempname.title()
        else:
            tempname = str(input("\nInvalid Parking Space ID! Please Try Again: "))
            tempname = tempname.title()

        if tempname == "****":
            flag += 1

        elif tempname in parkingID:
            flag=0
            status.append(tempname) #Store for used in view all
            store.append(tempname) #Store for when replacing the ID back to the location
            location = ((parkingID.index(tempname))+1) 
            parklocation.append(location-1) #Store the location of inside parkingID that has been taken
            (parkingID[location-1]) = ("****")
            x = studentID.index(temp)  
            print (location)
            break
        
        else:
            flag += 1

    clear()
    
    listall()
    print("\nAdded Successfully !")
    print("1. Add Another New Record\n2. Back")
    option=None
    flag=0
    while option != 2:
        
        if flag == 0:
            option = str(input("\nEnter Your Choice: "))
        else:
            option = str(input("Invalid Choice! Please Try Again: "))
        if option == "1":
            add()
        elif option == "2":
            menu()
        else:
            flag += 1
      
    return


def modify(): #####################################################################   Modify records
    clear()
    print("------- MODIFY STUDENTS DETAILS ------".center(138))
    listall()
    modify_records()
    return

def modify_records():
    print("\nWhich Record Do You Want To Modify?")
    option = int(input("Enter Your Choice: "))
             
    location = (option-1)
    if (option-1) < len(studentID):
        print("\nWhich part of the",("{0} {1}'s".format((fname[option-1]),(lname[option-1]))),"Student details do you want to modify?")
        print("\n1.TP number\t\t2.First Name\t\t\t3.Last Name\t\t\t4.Phone\t\t\t         5.Email\n6.Carplate\t\t7.Register_date\t\t\t8.ParkingslotID\t\t\t9.Modify Whole Student's details")
        option=None
        flag=0
        while option !=7:
            
            if flag == 0:
                option = str(input("\nEnter Your Choice: "))
            else:
                option = str(input("Invalid Choice! Please Try Again: "))
                
            if option == "1":
                temp = input("\nEnter Student's TP number: ")
                temp = temp[:1].upper() + temp[2:].capitalize()
                studentID[location] = temp
                break
            
            elif option == "2":
                tempname = str(input("Enter Student's First name: "))
                fname[location] = tempname.title()
                break
                
            elif option == "3":
                tempname = str(input("Enter Student's Last name: "))
                lname[location] = tempname.title()
                break
                
            elif option == "4":
                phone[location] = str(input("Enter Student's Mobile Number: "))
                break
                
            elif option == "5":
                email[location] = str(input("Enter Student's E-mail address: "))
                break
                
            elif option == "6":
                carplate[location] = str(input("Enter Student's Car Plate Number: "))
                break
                
            elif option == "7":
                register_date[location] = str(input("Enter Date of Registration: "))
                break
                
            elif option == "8":
                parkingslot()
                parkingID[parklocation[location]] = (store[location])
                del status[location]
                del store[location]
                del parklocation[location]
                flag=0
                for tempname in parkingID:
                    
                    if flag == 0:
                        tempname = str(input("\nEnter Parking Space ID: "))
                        tempname = tempname.title()
                    else:
                        tempname = str(input("\nInvalid Parking Space ID! Please Try Again: "))
                        tempname = tempname.title()

                    if tempname == "****":
                        flag += 1

                    elif tempname in parkingID:
                        flag=0
                        status.append(tempname) #Store for used in view all
                        store.append(tempname) #Store for when replacing the ID back to the location
                        location = ((parkingID.index(tempname))+1) 
                        parklocation.append(location-1) #Store the location of inside parkingID that has been taken
                        (parkingID[location-1]) = ("****")
                        #x = studentID.index(temp)  
                        print (location)
                        break
                    
                    else:
                        flag += 1
                        break
                break
                
            elif option == "9":
                temp = input("\nEnter Student's TP number: ")
                temp = temp[:1].upper() + temp[2:].capitalize()
                studentID[location] = temp
                tempname = str(input("Enter Student's First name: "))
                fname[location] = tempname.title()
                tempname = str(input("Enter Student's Last name: "))
                lname[location] = tempname.title()
                phone[location] = str(input("Enter Student's Mobile Number: "))
                email[location] = str(input("Enter Student's E-mail Address: "))
                carplate[location] = str(input("Enter Student's Car Number: "))
                register_date[location] = str(input("Enter Date Of Registration for the car park: "))
                break
            
            else:
                flag += 1
                
        clear()
        print("------- MODIFY STUDENT'S DETAILS ------".center(138))
        listall()
        print("\nModify Successfully !")
        print("1. Modify Another One\n2. Back")
        option=None
        flag=0
        while option !=2:
            
            if flag == 0:
                option = str(input("\nEnter Your Choice: "))
            else:
                option = str(input("Invalid Choice! Please Try Again: "))
                
            if option == "1":
                modify()
                
            elif option == "2":
                menu()
                
            else:
                flag += 1
                  
    else:
        modify()
       
    return


def delete(): #####################################################################   Delete records
    clear()
    print("------- DELETE STUDENT'S DETAILS ------".center(138))
    listall()
    delete_records()
    return

def delete_records():
    option=None
    flag=0
    print("Which Student's Details Need to be Deleted?")
    option = int(input("Enter Your Choice: "))
    #print("Which Student's Details Need to be Deleted?")
    #option = int(input("Enter Your Choice: "))
    if (option-1) < len(studentID):
        
        del studentID[option-1]
        del fname[option-1]
        del lname[option-1]
        del phone[option-1]
        del email[option-1]
        del carplate[option-1]
        del register_date[option-1]
        
        parkingID[parklocation[option-1]] = (store[option-1]) #This is the magic code HAHAH
        #parkingID[parklocation[option-1]]
        #This indicate the parkingID location that has previously change to ****
        #(store[option-1])
        #This is the value i store earlier when the ID of the parkingID location is being replace to ****
        del status[option-1]
        del store[option-1]
        del parklocation[option-1]
        
        clear()
        print("------- MODIFY STUDENT'S DETAILS ------".center(138))
        listall()
        print("\nDelete Successfully !")
        print("1. Delete Another Student's Details\n2. Back")
        option=None
        flag=0
        while option !=2:
            if flag == 0:
                option = str(input("\nEnter Your Choice: "))
            else:
                option = str(input("Invalid Choice! Please Try Again: "))
                
            if option == "1":
                delete()
                
            elif option == "2":
                menu()
                
            else:
                flag=flag+1
    else:
        delete()
    
    return


def search(): #####################################################################   Used to search student's details
    clear()
    print("------- SEARCH STUDENT'S DETAILS -------".center(138))
    listall()
    print("\n1.TP number\t\t2.First Name\t\t\t3.Last Name\t\t\t4.Phone\n5.Email\t\t\t6.Carplate\t\t\t7.Register_date")
    option=None
    flag=0
    while option !=2:
        
        if flag == 0:
            print("\nWhich Method Do You Prefer to Search By?")
            option = str(input("\nEnter Your Choice: "))
        else:
            option = str(input("Invalid Choice! Please Try Again: "))
            
        if option == "1":
            tempname = str(input("\nEnter Student's TP number: "))
            tempname = tempname[:1].upper() + tempname[2:].capitalize()
            current = 0
            flag1 = 0
            clear()
            print("------- SEARCH STUDENT'S DETAILS -------".center(138))
            print("------- Student's Details -------\n".center(138))
            print(" No. | Student ID | First Name | Last Name |   Phone   |        Email        | Carplate | Registration Date | Expiry date | ParkingslotID")

            while current < len(studentID):
                if tempname in studentID[current]:
                    print("",(current+1),(". |"),('{:^11}|{:^12}|{:^11}|{:^11}|{:^21}|{:^10}|{:^19}|{:^13}|{:^14}'.format(studentID[current],fname[current],lname[current].title(),phone[current],email[current],carplate[current],str(register_date[current]),str(expiry_date[current]),status[current])))
                    flag1 = flag1 + 1
                    location = studentID.index(tempname)
                current = current + 1

            break
                
        elif option == "2":
            tempname = str(input("Enter Student's First Name: "))
            current = 0
            flag1 = 0
            clear()
            print("------- SEARCH STUDENT'S DETAILS -------".center(138))
            print("------- Student's Details -------\n".center(138))
            print(" No. | Student ID | First Name | Last Name |   Phone   |        Email        | Carplate | Registration Date | Expiry date | ParkingslotID")

            while current < len(fname):
                if tempname in fname[current]:
                    print("",(current+1),(". |"),('{:^11}|{:^12}|{:^11}|{:^11}|{:^21}|{:^10}|{:^19}|{:^13}|{:^14}'.format(studentID[current],fname[current],lname[current].title(),phone[current],email[current],carplate[current],str(register_date[current]),str(expiry_date[current]),status[current])))
                    flag1 = flag1 + 1
                    location = fname.index(tempname)
                current = current + 1

            break
                
        elif option == "3":
            tempname = str(input("Enter Student's Last Name: "))
            current = 0
            flag1 = 0
            clear()
            print("------- SEARCH STUDENT'S DETAILS -------".center(138))
            print("------- Student's Details -------\n".center(138))
            print(" No. | Student ID | First Name | Last Name |   Phone   |        Email        | Carplate | Registration Date | Expiry date | ParkingslotID")

            while current < len(lname):
                if tempname in lname[current]:
                    print("",(current+1),(". |"),('{:^11}|{:^12}|{:^11}|{:^11}|{:^21}|{:^10}|{:^19}|{:^13}|{:^14}'.format(studentID[current],fname[current],lname[current].title(),phone[current],email[current],carplate[current],str(register_date[current]),str(expiry_date[current]),status[current])))
                    flag1 = flag1 + 1
                    location = lname.index(tempname)
                current = current + 1

            break
                
        elif option == "4":
            #tempname = str(input("Enter Student's Mobile Number: "))
            while True:
                try:
                   tempname = str(input("Enter Student's Mobile Number: "))
                   userInput = int(tempname)       
                except ValueError:
                   print("Not an integer! Try again.")
                   continue
                else:
                   break
            current = 0
            flag1 = 0
            clear()
            print("------- SEARCH STUDENT'S DETAILS -------".center(138))
            print("------- Student's Details -------\n".center(138))
            print(" No. | Student ID | First Name | Last Name |   Phone   |        Email        | Carplate | Registration Date | Expiry date | ParkingslotID")

            while current < len(phone):
                if tempname in phone[current]:
                    print("",(current+1),(". |"),('{:^11}|{:^12}|{:^11}|{:^11}|{:^21}|{:^10}|{:^19}|{:^13}|{:^14}'.format(studentID[current],fname[current],lname[current].title(),phone[current],email[current],carplate[current],str(register_date[current]),str(expiry_date[current]),status[current])))
                    flag1 = flag1 + 1
                    location = phone.index(tempname)
                current = current + 1

            break
                
        elif option == "5":
            tempname = str(input("Enter Student's E-mail Address: "))
            current = 0
            flag1 = 0
            clear()
            print("------- SEARCH STUDENT'S DETAILS -------".center(138))
            print("------- Student's Details -------\n".center(138))
            print(" No. | Student ID | First Name | Last Name |   Phone   |        Email        | Carplate | Registration Date | Expiry date | ParkingslotID")

            while current < len(email):
                if tempname in email[current]:
                    print("",(current+1),(". |"),('{:^11}|{:^12}|{:^11}|{:^11}|{:^21}|{:^10}|{:^19}|{:^13}|{:^14}'.format(studentID[current],fname[current],lname[current].title(),phone[current],email[current],carplate[current],str(register_date[current]),str(expiry_date[current]),status[current])))
                    flag1 = flag1 + 1
                    location = email.index(tempname)
                current = current + 1

            break
                
        elif option == "6":
            tempname = str(input("Enter Student's Car Plate Number: "))
            current = 0
            flag1 = 0
            clear()
            print("------- SEARCH STUDENT'S DETAILS -------".center(138))
            print("------- Student's Details -------\n".center(138))
            print(" No. | Student ID | First Name | Last Name |   Phone   |        Email        | Carplate | Registration Date | Expiry date | ParkingslotID")

            while current < len(carplate):
                if tempname in carplate[current]:
                    print("",(current+1),(". |"),('{:^11}|{:^12}|{:^11}|{:^11}|{:^21}|{:^10}|{:^19}|{:^13}|{:^14}'.format(studentID[current],fname[current],lname[current].title(),phone[current],email[current],carplate[current],str(register_date[current]),str(expiry_date[current]),status[current])))
                    flag1 = flag1 + 1
                    location = carplate.index(tempname)
                current = current + 1

            break
                
        elif option == "7":
            tempname = str(input("Enter Date of Registration: "))
            current = 0
            flag1 = 0
            clear()
            print("------- SEARCH STUDENT'S DETAILS -------".center(138))
            print("------- Student's Details -------\n".center(138))
            print(" No. | Student ID | First Name | Last Name |   Phone   |        Email        | Carplate | Registration Date | Expiry date | ParkingslotID")

            while current < len(register_date):
                if tempname in register_date[current]:
                    print("",(current+1),(". |"),('{:^11}|{:^12}|{:^11}|{:^11}|{:^21}|{:^10}|{:^19}|{:^13}|{:^14}'.format(studentID[current],fname[current],lname[current].title(),phone[current],email[current],carplate[current],str(register_date[current]),str(expiry_date[current]),status[current])))
                    flag1 = flag1 + 1
                    location = register_date.index(tempname)
                current = current + 1

            break

            
                

        else:
            flag=flag+1

    print(" _________________________________________________________________________________________________________________________________________")
    if flag1 == 0:
        searchfail()
    elif flag1 > 1:
        print("\n1. Search another one\n2. Modify these student's details\n3. Delete these student's details\n4. Back")
        option=None
        flag=0
        while option !=4:
            if flag == 0:
                option = str(input("\nEnter Your Choice: "))
            else:
                option = str(input("Invalid choice, please try agian: "))

            if option =="1":
                search()
            elif option =="2":
                modify_records()
            elif option =="3":
                delete_records()
            elif option =="4":
                menu()
            else:
                flag += 1
                
    print("\n1. Search another one\n2. Modify this student's details\n3. Delete this student's details\n4. Back")
    option=None
    flag=0
    current = location
    while option !=3:
        if flag == 0:
            option = str(input("\nEnter Your Choice: "))
        else:
            option = str(input("Invalid Choice! Please Try Agian: "))

        if option == "1":
            search()

        elif option == "2":
            print("\nWhich Part of",("{0} {1}'s".format((fname[current]),(lname[current]))),"Student Details Need to be Modified?")
            print("\n1.TP number\t\t2.First Name\t\t\t3.Last Name\t\t\t4.Phone\t\t\t         5.Email\n6.Carplate\t\t7.Register_date\t\t\t8.ParkingslotID\t\t\t9.Modify Whole Student's details")
            option=None
            flag=0
            while option !=7:
                
                if flag == 0:
                    option = str(input("\nEnter Your Choice: "))
                else:
                    option = str(input("Invalid Choice! Please Try Agian: "))
                    
                if option == "1":
                    temp = input("\nEnter Student's TP number: ")
                    temp = temp[:1].upper() + temp[2:].capitalize()
                    studentID[current] = temp
                    break
                
                elif option == "2":
                    tempname = str(input("Enter Student's First name: "))
                    fname[current] = tempname.title()
                    break
                    
                elif option == "3":
                    tempname = str(input("Enter Student's Last name: "))
                    lname[current] = tempname.title()
                    break
                    
                elif option == "4":
                    phone[current] = str(input("Enter Student's Mobile number: "))
                    break
                    
                elif option == "5":
                    email[current] = str(input("Enter Student's E-mail address: "))
                    break
                    
                elif option == "6":
                    carplate[current] = str(input("Enter Student's Car Plate Number: "))
                    break
                    
                elif option == "7":
                    register_date[current] = str(input("Enter Date of Registrationk: "))
                    break
                    
                elif option == "8":
                    parkingslot()
                    parkingID[parklocation[current]] = (store[current])
                    del status[current]
                    del store[current]
                    del parklocation[current]
                    flag=0
                    for tempname in parkingID:
                        
                        if flag == 0:
                            tempname = str(input("\nEnter Parking Space ID: "))
                            tempname = tempname.title()
                        else:
                            tempname = str(input("\nInvalid Parking Space ID! Please Try Again: "))
                            tempname = tempname.title()

                        if tempname == "****":
                            flag += 1

                        elif tempname in parkingID:
                            flag=0
                            status.append(tempname) #Store for used in view all
                            store.append(tempname) #Store for when replacing the ID back to the location
                            location = ((parkingID.index(tempname))+1) 
                            parklocation.append(location-1) #Store the location of inside parkingID that has been taken
                            (parkingID[location-1]) = ("****")
                            #x = studentID.index(temp)  
                            print (location)
                            break
                        
                        else:
                            flag += 1
                            break
                    break

                elif option == "9":
                    temp = input("\nEnter Student's TP number: ")
                    temp = temp[:1].upper() + temp[2:].capitalize()
                    studentID[current] = temp
                    tempname = str(input("Enter Student's First name: "))
                    fname[current] = tempname.title()
                    tempname = str(input("Enter Student's Last name: "))
                    lname[current] = tempname.title()
                    phone[current] = str(input("Enter Student's Mobile number: "))
                    email[current] = str(input("Enter Student's E-mail address: "))
                    carplate[current] = str(input("Enter Student's Car Plate Number: "))
                    register_date[current] = str(input("Enter Date of Registration: "))
                    break
                
                else:
                    flag += 1
                    
            clear()
            print("------- SEARCH STUDENT'S DETAILS ------".center(138))
            listall()
            print("\nModify successfully !")
            print("1. Search Another One\n2. Modify Another Student's Details\n3. Back")
            option=None
            flag=0
            while option !=3:
                
                if flag == 0:
                    option = str(input("\nEnter Your Choice: "))
                else:
                    option = str(input("Invalid Choice! Please Try Again: "))
                    
                if option == "1":
                    search()
                    
                elif option == "2":
                    modify()
                    
                elif option == "3":
                    menu()
                    
                else:
                    flag += 1
        

        elif option == "3":
            del studentID[current]
            del fname[current]
            del lname[current]
            del phone[current]
            del email[current]
            del carplate[current]
            del register_date[current]
            parkingID[parklocation[current]] = (store[current])
            del status[current]
            del store[current]
            del parklocation[current]
            clear()
            print("\t\t\t\t         ------- SEARCH STUDENT'S DETAILS ------")
            listall()
            print("\nDelete Successfully !")
            print("1. Search Another One\n2. Delete Another Student's Details\n3. Back")
            option=None
            flag=0
            while option !=3:
                if flag == 0:
                    option = str(input("\nEnter Your Choice: "))
                else:
                    option = str(input("Invalid Choice! Please Try Again: "))
                    
                if option == "1":
                    search()
                elif option == "2":
                    delete()
                elif option == "3":
                    menu()
                else:
                    flag += 1
            

        elif option == "4":
            menu()

        else:
            flag += 1

    return



    

def view_all(): #####################################################################   Print all the records with options
    clear()
    current = 0
        
    listall()

    print("1. Add a new record")
    print("2. Modify record")
    print("3. Delete a record")
    print("4. Back")
    option=None
    flag=0
    while option !=5:
        if flag == 0:
            option = str(input("\nEnter Your Choice: "))
        else:
            option = str(input("Invalid Choice! Please Try Again: "))
        if option == "1":
            add()
        elif option == "2":
            modify()
        elif option == "3":
            delete()
        elif option == "4":
            menu()
        else:
            flag += 1
            
    return

def listall(): #####################################################################   Print all the records but no options
    current=0
    print("------- Student's Details -------\n".center(138))
    if len(studentID) > 0:
        print(" No. | Student ID | First Name | Last Name |   Phone   |        Email        | Carplate | Registration Date | Expiry date | ParkingslotID".center(138))    
        while current < len(studentID):
            print("",(current+1),(". |"),('{:^11}|{:^12}|{:^11}|{:^11}|{:^21}|{:^10}|{:^19}|{:^13}|{:^14}'.format(studentID[current],fname[current],lname[current].title(),phone[current],email[current],carplate[current],str(register_date[current]),str(expiry_date[current]),status[current])))
            current = current + 1
        print(" _________________________________________________________________________________________________________________________________________")
    else:
        print("No Records Found")
        print("1. Create a New One")
        print("2. Back")
        option=None
        flag=0
        while option != 2:
            if flag == 0:
                option = str(input("\nEnter Your Choice: "))
            else:
                option = str(input("Invalid choice, please try agian: "))
                
            if option == "1":
                add()
                
            elif option == "2":
                menu()
                
            else:
                flag += 1
    return

def home(): #####################################################################   Home page
    clear()
    print("------- WELCOME TO APU CAR PARK REGISTRATION SYSTEM -------".center(138))
    print("\n1. Login \n2. Register \n3. Exit")
    option=None
    flag=0
    while option != 3:
        if flag == 0:
            option = str(input("\nEnter Your Choice: "))
        else:
            option = str(input("Invalid choice, please try agian: "))            

        if option == "1":
            login()
            
        elif option == "2":
            register()
            
        elif option == "3":
            sys.exit()
            
        else:
            flag += 1 
    return

def login(): #####################################################################   Login page
    clear()
    print("------- LOGIN -------".center(138))
    temp_userID = input("\nUserID: ")
    temp_password = input("Password: ")
    
    if (temp_userID in userID) and (temp_password in password):
        location = userID.index(temp_userID)
        print("\nWelcome",(user_fname[location]),(user_lname[location]),"!!")
        os.system("pause")
        menu()
    else:
        print("\nInvalid UserID or Invalid Password!")
        print("\n1. Login Again \n2. Register \n3. Back")
        flag = 0
        option = None
        while option != 3:
                
            if flag == 0:
                option = str(input("\nEnter Your Choice: "))
            else:
                option = str(input("Invalid Choice! Please Try Again: "))
                
            if option == "1":
                login()
                
            elif option == "2":
                register()
                
            elif option == "3":
                home()
                
            else:
                flag += 1
    return 

def register(): #####################################################################   Register page
    clear()
    print("------- REGISTRATION -------".center(138))
    tempname = input("\nEnter UserID: ")
    userID.append(tempname)
    tempname = input("Enter Passowrd: ")
    password.append(tempname)
    tempname = input("Enter First Name: ")
    user_fname.append(tempname)
    tempname = input("Enter Last Name: ")
    user_lname.append(tempname)
    print("\nAccount Successfully Created!")
    print("\n1. Register Another New Account\n2. Login \n3. Back")
    flag = 0
    option = None
    while option != 3:
        
        if flag == 0:
            option = str(input("\nEnter Your Choice: "))
        else:
            option = str(input("Invalid Choice! Please Try Agian: "))
                         
        if option == "1":
            register()
            
        elif option == "2":
            login()
            
        elif option == "3":
            home()
            
        else:
            flag += 1                   
                
    return
           
"""                                    END OF FUNCTIONS                                """        
"""                              THIS IS WHERE THE CODE START                          """
home()





