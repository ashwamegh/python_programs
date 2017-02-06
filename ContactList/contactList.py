import os

os.chdir(r"C:\\Users\AshwaMegh\Desktop") #Directory Where your text file is stored

#Prompt For Choices
def enter_choice():
    print('1\tAdd Contact')
    print('2\tShow all')
    print('3\tSearch by Name')
    print('4\tSearch by Number')
    print('5\tSave_File')
    print('6\tLoad_file')
    print('0\tExit')
    c = raw_input('Enter your Choice> ')
    return(c)

#Adds a Contact
def inputcontact():
    entry=[]
    n=raw_input('name> ')
    p=raw_input('phone> ')
    entry.append(n)
    entry.append(p)
    return entry

def search_by_name(dirlist):
    name=raw_input('enter name ')
    results=[]
    for e in dirlist:
        if name == e[0]:
            results.append(e)
    return results

def search_by_no(dirlist):
    no=raw_input('enter number ')
    results=[]
    for e in dirlist:
        if no in e:
            results.append(e)
    return results

def savedata(dirlist):
    f=open('directory.txt','r+')
    for n in dirlist:
        f.write(n[0])
        f.write(',')
        f.write(n[1])
    f.write('\n')
    f.close()

def loaddata():
    dirlist=[]
    f=open('directory.txt','r')
    for n in f:
        dirlist.append(n)
    return (dirlist)

#Variables Declaration
directory = []
Continue = True

#Response check
while Continue:
    ch = enter_choice()
    
    if ch =='1' :
        e = inputcontact()
        directory.append(e)
        print (e, 'Added to Contact List')

    if ch =='2':
        f = open('directory.txt')
        directory = f.read()
        print(directory)
        Continue = False

    if ch=='3' :
        entries = search_by_name(directory)
        print(entries)
        Continue = False

    if ch=='4' :
        entries= search_by_no(directory)
        print(entries)
        Continue = False
        
    if ch=='5':
        print("Adding", directory)
        savedata(directory)
        Continue = False

    if ch=='6':
        directory=loaddata()

    if ch=='0':
        break

