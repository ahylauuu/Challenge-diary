from pprint import PrettyPrinter
import json
from datetime import date
import datetime
pp=PrettyPrinter()
#enter the number corresponding to the challenge
#enter q when wanna quit the system
#enter 0 to add new challenge

filerecord="record.json"
challengefile="challenge.json"

challengelist={}

def loadrecord(file):
    try:
        with open(file,"r")as f:
            data=json.load(f)
            return data
    except:
        return ["",{}]
def loadrecord_dict(file):
    try:
        with open(file,"r")as f:
            data=json.load(f)
            return data
    except:
        return {}

def savefile(file,data):
    with open(file,"w") as f:
        json.dump(data,f,indent=1)



def addchallenge(data):
    savefile(challengefile,data)
    pp.pprint(data)

#basic setup
def setup():
    global x,chadata,data,today,d2,tdylistnumber

    today=date.today()
    d2 = today.strftime("%B %d, %Y")
    print(type(d2))
    print("Time:\t\t", d2)

    chadata=loadrecord_dict(challengefile)
    print("Challenge:\t",chadata)
    #pp.pprint(chadata)

    data=loadrecord(filerecord)
    #print(type(data))
    #for dict type record
    if len(data)==0:
        print("Tdy's progress:\t no challenge yet")
        tdylistnumber=0

    else:
        for i in range(len(data)):
            if data[i][0]==d2:
                tdylistnumber=i
                print("Tdy's progress: ",data[i][1])
    print(tdylistnumber)
    x=input("challenge number: ")

setup()

def appenddate(date,challenge,vx):
    global x,chadata,data,today,d2
    data[date]["Challenge"]=challenge
    data[date]["Challenge"]["Status"]=vx


while x!="q"or "a":
    
    try:
        int(x)
    except:
        print("Please enter a number")
        break

    challengeno=x
    
    
    if int(challengeno)==0:
            newcha=input("Please enter the new challenge: ")

            chadata[str(len(chadata)+1)]=newcha
            addchallenge(chadata)

            #print(len(chadata)," ",newcha)
            data[tdylistnumber][1][newcha]="V"
            #appenddate(d2,newcha,"V")
            savefile(filerecord,data)
            print("Added!\nLatest progess:", loadrecord(filerecord))
            break
            
    elif challengeno in chadata.keys():

        if chadata[challengeno] in data[tdylistnumber][1].keys():
            print("Already recorded!\nTomorrow do it again, you are on the right track!")
            break
        else:
            #appenddate(d2,chadata[challengeno],"V")
            #print(chadata[challengeno])
            
            addedchallenge=chadata[challengeno]
            #print(type(addedchallenge))
            data[tdylistnumber][1][addedchallenge]="V"
            savefile(filerecord,data)
            print("Saved!"," \nLatest progess:", loadrecord(filerecord))
            break
            
            #data[d2]={chadata[i]:"V"}
            
            #else:
                #continue
    else:
        print("unexpected error")
        
    x="q"
#'''''
def count():

    global data,chadata
    for i in chadata.values():
        count=0
        for n in range(len(data)):
            for j in data[n][1].keys():
                if j==i:
                    count+=1
        print(i,count)
#'''''
count()

def addbackhistory(file):
    global chadata,data,today,d2
    s=input("MM/DD/YYYY: ")
    e=input("MM/DD/YYYY: ")
    startdate=datetime.datetime.strptime("02/16/2022", "%m/%d/%Y")
    enddate=datetime.datetime.strptime("02/23/2022", "%m/%d/%Y")
    date_generated = [startdate + datetime.timedelta(days=n) for n in range(0, (enddate-startdate).days+1)]
    challengeno=input("Past Challenge no: ")

    if (enddate-startdate).days==0:
        d1=startdate.strftime("%B %d, %Y")
        data.append([d1,{chadata[challengeno]:"V"}])
        savefile(file,data)
        print("All Saved!")
    else:
        for day in date_generated:
            d1 = day.strftime("%B %d, %Y")
            #print(d1)
            data.append([d1,{chadata[challengeno]:"V"}])
            #print(data)
            savefile(file,data)
            print("All Saved!")
            loadrecord(file)

while x=="a":
    addbackhistory(filerecord)
    break

def sortdict(file):
    data=loadrecord(file)
    for i in range(len(data)):
        d=data[i][1]
        d=sorted(d.items())
        #print(d)
        c={k:v for k,v in d}
        #print(c)
        data[i][1]=c
        #print(data)
        savefile(file,data)
        

sortdict(filerecord)

data=loadrecord(filerecord)
d=data.sort()
print(d)