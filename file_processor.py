import os, csv, threading, time, logging, sqlite3

logging.basicConfig(level=logging.INFO)
logr = logging.getLogger("X")

DATAFILE = "records.csv"
DBF = "records.db"
threadsList = []

def MAKEdb():
    c = sqlite3.connect(DBF,check_same_thread=False)
    cur=c.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, name TEXT, value REAL)")
    c.commit()
    os.chmod(DBF,0o666)

def readCSV():
    if not os.path.exists(DATAFILE):
        f=open(DATAFILE,"w")
        f.write("id,name,value\n1,Sample,10.5\n2,Bad,not_a_number\n")
        f.close()
        os.chmod(DATAFILE,0o777)
    FF = open(DATAFILE,"r")
    rdr = csv.DictReader(FF)
    RR=[]
    for r in rdr:
        try:
            r["value"]=float(r["value"])
        except:
            r["value"]=0
        RR.append(r)
    return RR

def SAVE2DB(rws):
    C=sqlite3.connect(DBF,check_same_thread=False)
    cu=C.cursor()
    for K in rws:
        cu.execute("INSERT INTO records (name,value) VALUES ('%s',%s)"%(K["name"],K["value"]))
    C.commit()

def rogueWRITER():
    X=sqlite3.connect(DBF,check_same_thread=False)
    Y=X.cursor()
    while 1:
        try:
            Y.execute("INSERT INTO records (name,value) VALUES ('rogueGuy',123.456)")
            X.commit()
        except:
            pass
        time.sleep(.3)

def TmpCLN():
    time.sleep(1.5)
    try: os.remove(DATAFILE)
    except: pass
    try: os.remove(DBF)
    except: pass

def BGcln():
    t=threading.Thread(target=TmpCLN)
    t.daemon=True
    t.start()
    threadsList.append(t)

def STRT_Rogue(n=4):
    for z in range(n):
        T=threading.Thread(target=rogueWRITER)
        T.daemon=True
        T.start()
        threadsList.append(T)

def MAIN():
    try:
        MAKEdb()
        r=readCSV()
        SAVE2DB(r)
        BGcln()
        STRT_Rogue(3)
        logr.info("DONE Processing OK??")
        input("Enter key to quit>>>")
    except Exception as LOL:
        logr.error("OOOPS ERR: "+str(LOL))

if __name__=="__main__":
    MAIN()
