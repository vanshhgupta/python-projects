import pickle
def insertinbinary():
    s=[]
    while True:
        r=int(input("enter the roll no. of student"))
        n=input("enter the name of student")
        m=int(input("enter the marks of student"))
        l=[r,n,m]
        print(l)
        s.append(l)
        f=open(r"C:\Users\ggaur\Desktop\student.dat","wb")
        pickle.dump(s,f)
        print("record added")
        c=input("Do you want to enter more records: ")
        if c=="n" or c=="no" or c=='NO' or c=='No':
            break
    f.close()

def display():
    f=open(r"C:\Users\ggaur\Desktop\student.dat","rb")
    l=pickle.load(f)
    for i in l:
        print(i)
    f.close()

def search(s):
    f=open(r"C:\Users\ggaur\Desktop\student.dat","rb")
    l=pickle.load(f)
    x=0
    for i in l:
        if i[0]==s:
            print(i)
            x=1
    if x==0:
        print("Record not found")
    f.close()

def mod():
    found = False
    h=[]
    f=open(r"C:\Users\ggaur\Desktop\student.dat","rb+")
    j=int(input("enter the roll no. of record you want to modify"))
    l=pickle.load(f)
    for i in l:
        if i[0]==j:
            c=input("enter name")
            i[1]=c
            d=int(input("enter marks"))
            i[2]=d
            print("record updated")
            print(i)
            break
        f.seek(0)
        pickle.dump(l,f)
        
    f.close()

def delete():
    f=open(r"C:\Users\ggaur\Desktop\student.dat","rb+")
    l=pickle.load(f)
    j=int(input("Enter the roll no. of student whose record you want to delete"))
    lh=[]
    a=0
    for i in l:
        if i[0]!=j:
            lh.append(i)
            a=1
    if a==0:
        print("Record not found")
    pickle.dump(lh,f)
    print("the new record is:",lh)
    f.close()

def copy():
    f=open(r"C:\Users\ggaur\Desktop\student.dat","rb+")
    l=pickle.load(f)
    f1=open(r"C:\Users\ggaur\Desktop\new.dat","wb")
    h=[]
    for i in l:
        h.append(i)
    pickle.dump(h,f1)
    print("New file created and record transferred")
    f.close()
    f1.close()

def count():
    f=open(r"C:\Users\ggaur\Desktop\student.dat","rb")
    l=pickle.load(f)
    c=0
    for i in l:
        c=c+1
    print("Total no. of records are",c)

def avg():
    f=open(r"C:\Users\ggaur\Desktop\student.dat","rb")
    l=pickle.load(f)
    c=0
    h=0
    for i in l:
        c=c+1
        h=h+i[2]
    avg=h/c
    return avg

def mcopy():
    f=open(r"C:\Users\ggaur\Desktop\student.dat","rb+")
    l=pickle.load(f)
    f1=open(r"C:\Users\ggaur\Desktop\new.dat","wb")
    h=[]
    for i in l:
        if i[2]>90:
            h.append(i)
    pickle.dump(h,f1)
    print("New file created and record transferred")
    f.close()
    f1.close()

def ncopy():
    f=open(r"C:\Users\ggaur\Desktop\student.dat" ,"rb+")
    l=pickle.load(f)
    f1=open(r"C:\Users\ggaur\Desktop\new.dat","wb")
    h=[]
    for i in l:
        if i[1][0] in "Aa":
            h.append(i)
    pickle.dump(h,f1)
    print("New file created and record transferred")
    f.close()
    f1.close()

print("MENUDRIVEN PROGRAM TO PERFORM TASK ON BINARY FILES")
print("1.Insert data in the form of records")
print("2.display all the records present in the file")
print("3.Search and display a particular record")
print("4.modify a particular record")
print("5.Delete a particular record")
print("6.copy all the data into another file")
print("7.copy all the data of students having marks>90 into another file")
print("8.copy all the data  of students having name starting with 'a' into another file")
print("9.Display average marks of all the students")
print("10.Display total no. of records in the file")
print("11.Move out of program")
while True:
    c=int(input("Enter the no. for the desired task"))

    if c==1:
        insertinbinary()
    elif c==2:
        print("The records in the file are")
        display()
    elif c==3:
        j=int(input("Enter the roll no. to search"))
        search(j)
    elif c==4:
        mod()
    elif c==5:
        delete()
    elif c==6:
        copy()    
    elif c==7:
        mcopy()
    elif c==8:
        ncopy()
    elif c==9:
        print("The avg marks of students is ",avg())
    elif c==10:
        count()
    elif c==11:
        break
    else:
        print("enter a valid choice")
