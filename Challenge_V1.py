#owner: ahylauuu

from pprint import PrettyPrinter
import json
from datetime import date
import datetime

from numpy import save
pp=PrettyPrinter()
#enter the number corresponding to the challenge
#enter q when wanna quit the system
#enter 0 to add new challenge

filerecord="record_V1.json"
challengefile="challenge_V1.json"

challengelist={}

def loadrecord(file):
    try:
        with open(file,"r")as f:
            data=json.load(f)
            return data
    except:
        return []

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

def checklistday(tracklistno,date):
    global data
    tracklistno=""
    for i in range(len(data)):
            if data[i][0]==date:
                tracklistno=i
                #print(i,data[tdylistnumber][1])
                break
            else:
                continue
    if tracklistno=="": #no d1 history
        data.append([date,{}])
        tracklistno=(len(data)-1)
    return tracklistno

#basic setup
def setup():
    global x,chadata,data,today,d2,tdylistnumber
    print("V1")
    today=date.today()
    d2 = today.strftime("%B %d, %Y")
    #print(type(d2))
    print("Time:\t\t", d2)

    chadata=loadrecord_dict(challengefile)
    print("Challenge:\t",chadata)
    #pp.pprint(chadata)

    data=loadrecord(filerecord)
    #pp.pprint(data)
    #try:
     #   print("Tdy's Progress:\t",data[0])
    #except:
    
            #print(tdylistnumber)
    tdylistnumber=""
    tdylistnumber=checklistday(tdylistnumber,d2)        

    #print(data[(len(data)-1)][1])
    if len(data[tdylistnumber][1])==0:
        print("Tdy's Progress:\tNo progress yet! Start now!")
        #print(data[tdylistnumber][1])
    else:
        print("Tdy's Progress:\t",data[tdylistnumber][1])
        #print(len(data))
        #print(data)
    for i in range(len(data)):
        if data[i][0]==d2:
            tdylistnumber=i
            #print(tdylistnumber)
        """""
    if len(data)==0:
        print("Tdy's progress:\t no challenge yet")
        data=data.append([d2,{}])
        print(data)
        tdylistnumber=0
    else:
        data=data.append([d2,{}])
        #savefile(filerecord,data)
        for i in range(len(data)):
            if data[i][0]==d2:
                tdylistnumber=i
                print("Tdy's progress: ",data[i][1])
        print(data)
        """
    print("Enter\t'0' to add new challenge.\n\t'a' to add range of challenge taken\n\t'l' to load all the challenge you have taken\n\t'q' to quit entering" )
    x=input("Challenge number: ")

def appenddate(date,challenge,vx):
    global x,chadata,data,today,d2
    data[date]["Challenge"]=challenge
    data[date]["Challenge"]["Status"]=vx

setup()

while x!="q"or "a":
    if x=="show":
        print("Latest Progess:")
        pp.pprint(loadrecord(filerecord))
    try:
        int(x)
    except:
        
        break

    challengeno=x
    
    
    if int(challengeno)==0:
        #print(type(chadata))
        newcha=input("Please enter the new challenge: ")

        chadata[str(len(chadata)+1)]=newcha
        addchallenge(chadata)

        #print(len(chadata)," ",newcha)
        data[tdylistnumber][1][newcha]="V"
        #appenddate(d2,newcha,"V")
        savefile(filerecord,data)
        print("Added!")
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
            print("Saved!")
            break
            
            #data[d2]={chadata[i]:"V"}
            
            #else:
                #continue
    else:
        print("unexpected error")
    
    #x="q"
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
def checklistday(tracklistno,date):
    global data
    tracklistno=""
    for i in range(len(data)):
            if data[i][0]==date:
                tracklistno=i
                #print(i,data[tdylistnumber][1])
                break
            else:
                continue
    if tracklistno=="": #no d1 history
        data.append([date,{}])
        tracklistno=(len(data)-1)
    return tracklistno

def addbackhistory(file):
    global chadata,data,today,d2
    s=input("MM/DD/YYYY: ")
    e=input("MM/DD/YYYY: ")
    startdate=datetime.datetime.strptime(s, "%m/%d/%Y")
    enddate=datetime.datetime.strptime(e, "%m/%d/%Y")
    date_generated = [startdate + datetime.timedelta(days=n) for n in range(0, ((enddate-startdate).days+1))]
    challengeno=""

    thatdaylistno=""
    if (enddate-startdate).days==0:
        d1=startdate.strftime("%B %d, %Y")
        thatdaylistno=checklistday(thatdaylistno,d1)
        while challengeno!="stop":
            challengeno=input("Past Challenge no: ")
            data[thatdaylistno][1][chadata[challengeno]]="V"
        savefile(file,data)
        print("All Saved!")
    else:
        while challengeno!="stop":
            challengeno=input("Past Challenge no: ")
            if challengeno=="stop":
                break
            for day in date_generated:
                d1 = day.strftime("%B %d, %Y")
                #print(d1)
                thatdaylistno=checklistday(thatdaylistno,d1) #ensure there list of d1
                #print(data)
                data[thatdaylistno][1][chadata[challengeno]]="V" #add challenge into d1
                savefile(file,data)
                loadrecord(file)
            print("All Saved!")

while x=="a":
    addbackhistory(filerecord)
    break

while x=="l":
    pp.pprint(loadrecord(filerecord))
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
    data=loadrecord(filerecord)
    data=sorted(data,key=lambda x:x[0],reverse=True)
    savefile(filerecord,data)
    print(data)
sortdict(filerecord)
