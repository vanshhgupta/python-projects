# creating a menu driven program based on text files
#1. display the file 
#2. display the file size
#3. display the number of line number
#4. display every line
#5. count the number of words in the file
#6.  count the number of words in the file
#7. count the number of consonant 
#8. Count the number of digits 
#9. Count the number of alphabet 
#10. Count the number of lowercase alphabet
#11. Display the first line of file 
#12. display last line of file
#13. Display line starting with digit
#14. Count and display the number of this in the file 
#15. check and display alphabet of file 
#16. Display all the lines not starting with digit
#17. Copy the content of one file into a file name info.txt 
#18. Capitalise first letter of every line 
#19. Display the line not starting with p
#20. Find the total number of lines starting with S

print("choose the file to start the program")
print(" FILE 1. Dust of Snow\n FILE 2. Fire and Ice")
a=int(input("enter the file number to choose:"))
if a==1:
    file='C:\\Users\\ggaur\\Desktop\\dust of snow.txt'
elif a==2:
    file='C:\\Users\\ggaur\\Desktop\\fire and ice.txt'
else:
    print("choose correct number")
    
print("")
print("MENU")
print("")
print('1:display the file ')
print('2:display the file size')
print('3:display the number of line number')
print('4:display every line')
print('5:count the number of words in the file')
print('6: count the number of words in the file')
print('7:count the number of consonant ')
print('8:Count the number of digits ')
print('9:Count the number of alphabet ')
print('10:Count the number of lowercase alphabet')
print('11:Display the first line of file ')
print('12:display last line of file')
print('13:Display line starting with digit')
print('14:Count and display the number of ''this'' in the file ')
print('15:check and display alphabet of file ')
print('16:Display all the lines not starting with digit')
print('17:Copy the content of one file into a file name info.txt ')
print('18:Capitalise first letter of every line ')
print('19:Display the line not starting with(p)')
print('20:Find the total number of lines starting with (S)')
print("")

#user defined functions start
def displayfile():
    f= open(file,'r')
    print(f.read())
    f.close()

def filesize():
    f = open(file,'r')
    g=f.read()
    h=len(g)
    print('no of byte in file:',h)
    f.close()

def linenumber():
    f = open(file,'r')
    g=f.readlines()
    h=len(g)
    print('no of lines in file:',h)
    f.close()

def displayline():
    f = open(file,'r')
    g=f.readlines()
    for i in g:
        print(i)
    f.close()

def countwords():
    f = open(file,'r')
    g=f.read()
    h=g.split()
    k=0
    for i in h:
        k+=1
    print("the number of words in file are: ",k)
    f.close()

def countvowels():
    f = open(file,'r')
    g=f.read()
    h=g.lower()
    k=0
    for i in h :
        if i in ('a','i','u','o','e'):
            k=k+1
    print("the number of vowels in file are: ",k)
    f.close()

def countconsonent():
    f = open(file,'r')
    g=f.read()
    h=g.lower()
    k=0
    for i in h :
        if i >= 'a' and i <= 'z':
            k+=1
        if i in ('a','i','u','o','e'):
            k-=1
    print("the number of consonents in file are: ", k)
    f.close()

def countdigit():
    f = open(file,'r')
    g=f.read()
    k=0
    for i in g :
        if i.isdigit():
            k+=1
    print("the number of digits in file are: ",k)
    f.close()

def countalpha():
    f = open(file,'r')
    g=f.read()
    k=0
    for i in g :
        if i.isalpha():
            k+=1
    print("the number of alpabets in file are: ",k)
    f.close()
    
def lowercase():
    f = open(file,'r')
    g=f.read()
    k=0
    for i in g :
        if i.islower():
            k+=1
    print("the number of lowercase alphabets in file are: ",k)
    f.close()

def firstline():
    f = open(file,'r')
    g=f.readlines()
    print("the first line of the file: ",g[0])
    f.close()

def lastline():
    f = open(file,'r')
    g=f.readlines()
    h=len(g)-1
    print("the first line of the file: ",g[h])
    f.close()

def startdigit():
    f = open(file,'r')
    g=f.readlines()
    for i in g:
        if i[0].isdigit():
            print(i,end=" ")
        else:
            break
    print("no line starts with a digit")
    f.close()
            
def countthis():
    f = open(file,'r')
    g=f.read()
    h=g.lower()
    k=0
    for i in h :
        if i=='this':
            k+=1
    print("the number of 'this' in the file are: ",k)
    f.close()

def alphanumeric():
    f = open(file,'r')
    g=f.read()
    k=0
    for i in g :
        if i.isalpha():
            k+=1
        elif i.isnumeric():
            k+=1
    print("the number of alphanumeric in file are: ",k)
    f.close()

def startnodigit():
    f = open(file,'r')
    g=f.readlines()
    for i in g:
        if i[0].isdigit():
            print("this line starts with a digit")
        else:
            print(i,end=' ')
    f.close()

def copytonew():
    f= open(file,'r')
    f1= open('info.txt.','w')
    for i in f:
        f1.write(i)
    f1.close()
    f1 = open('info.txt','r')
    f3=f1.read()
    print('The content in file info are\n',f3)
    f.close()
    f1.close()

def capeachword():
    f= open(file,'r')
    g= f.readlines()
    for i in g:
        if i[0].isalpha():
            print(i.capitalize(), end=" ")
    print()
    f.close()

def notstartwithp():
    f= open(file,'r')
    g= f.readlines()
    for i in g:
        if i[0] not in ('p', 'P'):
            print(i, end=" ")
    print()
    f.close()

def startwiths():
    f= open(file,'r')
    g= f.readlines()
    k= 0
    for i in g:
            if i[0] in ('S','s'):
                k=+1
    print('total no. of line starting with s:', k)
    f.close()

while True:
    choice= str(input("enter a valid choice from the given menu: "))
    if choice=='1':
        displayfile()

    elif choice=='2':
        filesize()

    elif choice=='3':
        linenumber()

    elif choice=='4':
        displayline()

    elif choice=='5':
        countwords()

    elif choice =='6':
        countvowels()
        
    elif choice=='7':
        countconsonent()

    elif choice=='8':
        countdigit()

    elif choice=='9':
        countalpha()

    elif choice=='10':
        lowercase()

    elif choice=='11':
        firstline()

    elif choice=='12':
        lastline()

    elif choice=='13':
        startdigit()

    elif choice =='14':
        countthis()
        
    elif choice=='15':
        alphanumeric()

    elif choice=='16':
        startnodigit()

    elif choice=='17':
        copytonew()

    elif choice=='18':
        capeachword()

    elif choice=='19':
        notstartwithp()

    elif choice=='20':
        startwiths()
        
    elif choice in ('b','B'):
        print("moving out of program")
        break

    else:
        print("enter a valid choice")
