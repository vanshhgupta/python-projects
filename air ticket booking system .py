import pymysql
#connecting database
db=pymysql.connect(host="localhost",user="root",password="1234")
cur=db.cursor()
cur.execute("create database ticket;")
cur.execute("use ticket;")
#table1
cur.execute("create table flightdetails(flight_number int(10) , departure varchar(30), destination varchar(30), flight_date date,time_of_flight time,airline varchar(20), cost int(6), available_seats int(4));")
db.commit()
cur.execute("insert into flightdetails values(1000,'delhi','mumbai','2022-11-01','10:15:00','spicejet',12000,125);")
cur.execute("insert into flightdetails values(1001,'delhi','lucknow','2022-11-01','13:20:00','air India', 11000,120);")
cur.execute("insert into flightdetails values(1002,'mumbai','banglore','2022-11-12','06:30:00','spicejet',9500,100);")
cur.execute("insert into flightdetails values(1003,'delhi','kolkata','2022-11-05','03:45:00','akasa',8000,80);")
cur.execute("insert into flightdetails values(1004,'raipur','mumbai','2022-12-06','16:15:00','air India',13000,180);")
cur.execute("insert into flightdetails values(1005,'delhi','srinagar','2022-12-09','15:15:00','spicejet',7500,95);")
cur.execute("insert into flightdetails values(1006,'amritsar','mumbai','2023-01-01','19:30:00','spicejet',6575,85);")
cur.execute("insert into flightdetails values(1007,'goa','mumbai','2022-12-25','10:35:00','air India',5600,92);")
cur.execute("insert into flightdetails values(1008,'roorkee','kanpur','2022-12-20','10:15:00','spicejet',7650,105);")
db.commit()
#table2
cur.execute("create table personaldetails(unique_id int(10) , name varchar(20), age int(3),DOB date, gender char(2),email_address varchar(50),house_address varchar(100),phone_no varchar(10), passport_no varchar(10), flight_no int(6));")
db.commit()
#table3
cur.execute("create table requesttable(requested_departure varchar(30), requested_destination varchar(30), requested_flight_date date, requested_time_of_flight time, requested_cost int(6));")
db.commit()

#user define functions
def flightdetail():
    fno=str(input("Enter flight number: "))
    start=str(input("Enter flight starting point: "))
    end=str(input("Enter flight destination: "))
    fdate=input("Enter the flight date in format (yyyy-mm-dd): ")
    ftime=input("Enter the flight departure timings in format (HH:MM:SS): ")
    fname=str(input("Enter name of the airlines: "))
    fcost=int(input("Enter the price of the flight ticket: "))
    fseatno=int(input("Enter the number of seats available in the flight: "))
    query="insert into flightdetails values({},'{}','{}','{}','{}','{}',{},{})".format(fno,start,end,fdate,ftime,fname,fcost,fseatno)
    cur.execute(query)
    db.commit()
    print("Record of the flight is inserted Successfully.")

def flightdetailmodify():
    fno=str(input("Enter flight number to be updated: "))
    start=str(input("Enter new flight starting point: "))
    end=str(input("Enter new flight destination: "))
    fdate=input("Enter the new flight date in format (yyyy-mm-dd): ")
    ftime=input("Enter the new flight departure timings in format (HH:MM:SS): ")
    fname=str(input("Enter new name of the airlines: "))
    fcost=int(input("Enter the new price of the flight ticket: "))
    fseatno=int(input("Enter the new number of seats available in the flight: "))
    query="update flightdetails set departure='{}', destination='{}', flight_date='{}', time_of_flight='{}',airline='{}', cost={},\
available_seats={} where flight_number={}".format(start,end,fdate,ftime,fname,fcost,fseatno,fno)
    cur.execute(query)
    db.commit()
    print("Record of the flight is updated")

def flightdetaildelete():
    fno=int(input("Enter the flight number of the flight whose details are to be deleted: "))
    cur.execute("delete from flightdetails where flight_number=%d"%fno)
    db.commit()
    print("Record deleted")

def flightavailable():
    query="select * from flightdetails;"
    row=cur.execute(query)
    while True:
        y= cur.fetchone()
        if y== None:
            break
        print(y)

def bookflight():
    U1 = int(input("Enter passenger's aadhar number: "))
    U2 = input("Enter passenger's name: ")
    U3= int(input("Enter passenger's age : "))
    U4= input("Enter passenger's DOB (yyyy-mm-dd): ")
    U5= input("Enter passenger's gender (M/F/O): ")
    U6 = input("Enter passenger's email address: ")
    U7 = input("Enter passenger's address: ")
    U8= int(input("Enter passenger's phone number: "))
    U9= input("Enter passenger's passport number: ")
    print(" ")
    print ("Flight details")
    query="select flight_number, departure, destination, flight_date, cost, available_seats from flightdetails;"
    row=cur.execute(query)
    while True:
        y= cur.fetchone()
        if y== None:
            break
        print(y)
    U10=int(input("Enter the flight number to book the ticket among the following: "))
    query="update flightdetails set available_seats=available_seats-1 where flight_number={}".format(U10)
    cur.execute(query)
    db.commit()
    query="insert into personaldetails values({},'{}',{},'{}','{}','{}','{}',{},'{}',{})".format(U1,U2,U3,U4,U5,U6,U7,U8,U9,U10)
    cur.execute(query)
    db.commit()
    print(" ")
    print("Flight booked")

def requestupgarde():
    start=str(input("Enter new flight starting point: "))
    end=str(input("Enter new flight destination: "))
    fdate=input("Enter the new flight date in format (yyyy-mm-dd): ")
    ftime=input("Enter the new flight departure timings in format (HH:MM:SS): ")
    fcost=int(input("Enter the new price of the flight ticket: "))
    query="insert into requesttable values('{}','{}','{}','{}',{})".format(start,end,fdate,ftime,fcost,)
    cur.execute(query)
    db.commit()
    print("Record of the requested flight is added in the systems for consultation")

def cancelticket():
    UID=int(input("Enter the AADHAR CARD number of the passenger wose ticket to be canceled: "))
    cur.execute("Delete from personaldetails where unique_id=%d"%UID)
    db.commit()
    print("Ticket canceled")

def requestflighttable():
    query="select * from requesttable;"
    row=cur.execute(query)
    while True:
        y= cur.fetchone()
        if y== None:
            break
        print(y)

def tickettable():
    query="select p.unique_id, p.name, p.age, p.gender, p.house_address, p.phone_no, p.passport_no, f.flight_number,f.departure,\
f.destination, f.flight_date, f.time_of_flight, f.airline, f.cost from flightdetails f, personaldetails p where f.flight_number=p.flight_no;"
    row=cur.execute(query)
    while True:
        y= cur.fetchone()
        if y== None:
            break
        print(y)

def ticketbooked():
    fno=int(input("Enter the UID for getting booking details: "))
    query="select p.unique_id, p.name, p.age, p.gender, p.house_address, p.phone_no, p.passport_no, f.flight_number,\
f.departure, f.destination, f.flight_date, f.time_of_flight, f.airline, f.cost from flightdetails f, personaldetails p where f.flight_number=p.flight_no and p.unique_id=%d"%fno
    row=cur.execute(query)
    while True:
        y= cur.fetchone()
        if y== None:
            break
        print(y)
        
    
print("AIR TICKET BOOKING SYSTEM")
while True:
    print("")
    user= input("Enter 1. staff member\nEnter 2. passenger\nEnter 3. QUIT\nEnter option: ")
    print("")
    if user=='1':
        b=input( " Enter password: ")
        while b=='1234':
            print("Menu for staff")
            print("1. Adding in flight detail\n2.Modifying flight details\n3.Deleting flight records\n4.Check flight requests\n5.Check ticket booked\n6. Quit")
            print(" ")
            c= input("Enter your choice")
            if c=='1':
                flightdetail()
            elif c=='2':
                flightdetailmodify()
            elif c=='3':
                flightdetaildelete()
            elif c=='4':
                requestflighttable()
            elif c=='5':
                tickettable()
            elif c=='6':
                break
            else:
                print("enter corect choice")
        while b not in ('1234'):
            print(" NON STAFF MEMBERS ARE NOT ALLOWED")
            break

    while user=='2':
        print("Menu for Passenger")
        print("1.Available flight Detail")
        print ("2.Request for updation of flight details as per your needs")
        print("3.Booking of Ticket")
        print("4. Check tickets booked by you")
        print("5.Cancellation of Ticket")
        print("6.Quit")
        n=int(input("Enter serial number of your choice"))
        if n==1:
            flightavailable()
        elif n==2:
            requestupgarde()
        elif n==3:
            bookflight()
        elif n==4:
            ticketbooked()
        elif n==5:
            cancelticket()
        elif n==6:
            break
        else:
            print("Enter valid choice")

    if user=="3":
        break

    else:
        print("Enter a valid choice")


