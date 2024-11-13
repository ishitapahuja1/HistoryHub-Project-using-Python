import pickle

def read_sample_historical_events_data():
    print('-'*100)
    print("Sample Historical events from different years ...\n")
    print('-'*100)
    f=open("Historical_Events.dat","rb")
    try:
        
        while True:
            s=pickle.load(f)
            for i in range (len(s)-1-5,len(s),1):
                print(s[i])
    except Exception:
        f.close()
        print("\n File Closed ...")
        

def search_historical_events_day():
    f=open("Historical_Events.dat","rb") #statement 1
    r=int(input("Which day historical events you want to know about?\n Type a day number between 1 to 31: "))
    if r in range(1,32):
        print('-'*100)
        print('The historical events happened on day',r, 'of the month are as follows:')
        print('-'*100)
        found=0
        try:
            f.seek(0)
            s=pickle.load(f) 
            count=0
            for i in s: # statement 3
                if i[0]==r and count<5: # statement 4
                    print(i[3],'\n')
                    count+=1
                    found=1
        except EOFError:
            print("Reading of the file is complete ")
            
            f.close() # ststement 5
            
        if found==0:
            print(" Record NOT Found  ")
            
    else:
        print('-'*100)
        print('\nPlease choose a valid day number between 1 to 31')
        print('-'*100)
        search_historical_events_day()
        
     
    
def search_historical_events_month():
    f=open("Historical_Events.dat","rb") #statement 1
    month_dict={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    r=int(input("Which month historical events you want to know about?\n Type a month number between 1 to 12: "))
    if r in range(1,13):
        print('-'*100)
        print('The historical events happened in ',month_dict[r], 'month are as follows:')
        print('-'*100)
        found=0
        try:
            f.seek(0)
            s=pickle.load(f) 
            count=0
            for i in s: # statement 3
                if i[1]==r and count<5: # statement 4
                    print(i[3],'\n')
                    count+=1
                    found=1
        except EOFError:
            print("Reading of the file is complete ")
            
            f.close() # ststement 5
            
        if found==0:
            print(" Record NOT Found  ")
    else:
        print('-'*100)
        print('\nPlease choose a valid month number between 1 to 12')
        print('-'*100)
        search_historical_events_month()
        


def appendhistoricaleventdata():
    f=open("Historical_Events.dat","rb+")
    print("appending data in the File...")
    Rec=pickle.load(f)# this will read the contents of the file and put it in rec list
    while True:
        day=int(input("Enter the Day No \n Type a day number between 1 to 31: "))
        month=int(input("Enter the Month No \n Type a month number between 1 to 12: "))
        year=int(input("Enter the Year No \n Type a year number between 1900 to 2022: "))
        event=input("Enter the Event : ")
        data=[day,month,year,event]
        Rec.append(data)
        ch=input("More records (Y/N) ? ")
        if ch in 'Nn':
            break
    f.seek(0)# take the ponter to the begining of the file
    pickle.dump(Rec,f)
    print("Record Appended ...")
    f.close()
    
def deletehistoricalevent():
    f=open("Historical_Events.dat","rb") # to jusr read from file
    s=pickle.load(f)
    f.close()
    day=int(input("Enter the Day No to be deleted \n Type a day number between 1 to 31: "))
    month=int(input("Enter the Month No to be deleted \n Type a month number between 1 to 12: "))
    year=int(input("Enter the Year No to be deleted \n Type a year number between 1900 to 2022: "))
    f=open("Historical_Events.dat","wb") # to write freshly in the file
    reclst=[]
    for i in s:
        if i[0]==day and i[1]==month and i[2]==year:
            continue
        reclst.append(i)
    pickle.dump(reclst,f)
    print("\n your record has been deleted  ")
    f.close()



def updatehistoricalevent():
    f=open("Historical_Events.dat","rb+")
    day=int(input("Enter the Day No to be deleted \n Type a day number between 1 to 31: "))
    month=int(input("Enter the Month No to be deleted \n Type a month number between 1 to 12: "))
    year=int(input("Enter the Year No to be deleted \n Type a year number between 1900 to 2022: "))
    f.seek(0)# take the file pointer to the zero th position
    try:
        while True:
            rpos=f.tell()# it will give 0 as the position ie begining
            s=pickle.load(f)
            for i in s:
                if i[0]==day and i[1]==month and i[2]==year:
                    print("This is the record you wish to modify/update ")
                    i[3]=input("Enter the new event  ")
                    f.seek(rpos) # go to 0 th byte or begining of file
                    pickle.dump(s,f)
                    print("Your record has been updated ")
                    break
    except Exception:
        f.close()
        
def MainMenu():

    print("1. Read historical events data")
    print("2. Search historical events on a psrticular month")
    print("3. Search historical events on a particular day")
    print("4. Append a historical event data")
    print("5. Update a historical event")
    print("6. Delete a historical event")
    print("7. Exit...")
    print("----------------------------------------")
    
while True: # it is a loop which will run infinite times with no pre condition
    print('-'*100)
    print("""\t\t\t\t\tWELCOME TO THE HISTORY BUFFS ZONE \n\n\t\t\t\tPROJECT MADE BY ISHITA PAHUJA""")
    print('-'*100)
    MainMenu() # call to the MainMenu function
    ch=int(input("Enter your choice :  "))
    if ch==1:
        read_sample_historical_events_data()
    elif ch==2:
        search_historical_events_month()
    elif ch==3:
        search_historical_events_day()
    elif ch==4:
        appendhistoricaleventdata()     
    elif ch==5:
        updatehistoricalevent()
    elif ch==6:
        deletehistoricalevent()
    elif ch==7:
        print('-'*100)
        print('\t\t\t\tHOPE YOU HAD A GREAT TIME IN KNOWING HISTORICAL EVENTS\n\t\t\t\t\t\tSEE YOU NEXT TIME')
        print('-'*100)
        break
    else:
        print('\nPlease choose a valid option between 1 to 7')
        
        
        
