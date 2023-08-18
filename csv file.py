import csv
def csvfile1():
    file=open('employee.csv','w',newline='')
    csvobj=csv.writer(file)
    while True:
        empno=int(input('employee no.'))
        Name=input('name:')
        salary=float(input('salary:'))
        data=[empno,Name,salary]
        csvobj.writerow(data)
        ask=input('do you want to enter more entries')
        if ask in ('n','N','no','No'):
            break
    file.close()

def csvfile2():
    file=open('employee.csv','a',newline='')
    csv1=csv.writer(file)
    data=[]
    while True:
        empno=int(input('employee no.'))
        Name=input('name:')
        salary=float(input('salary:'))
        data.append([empno,Name,salary])
        ch=input('do you want to enter more entries')
        if ch in ('n','N','no','No'):
            csv1.writerows(data)
            break
    file.close()

def preview():
    file=open('employee.csv','r',newline='')
    csvfile=csv.reader(file)
    for i in csvfile:
        print(i)
    file.close()

    
while True:
    option=int(input('1. Create csv without append function\n2:create csv with append function\n3:show csv\n4:quit\nEnter your choice: '))
    if option==1:
        csvfile1()
    elif option==2:
        csvfile2()
    elif option==3:
        preview()
    elif option==4:
        break
        
