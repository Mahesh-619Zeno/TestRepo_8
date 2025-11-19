import csv
import os

def ReadSales(Fpath):
    SALES = []
    if not os.path.exists(Fpath):
        f = open(Fpath,"w")
        f.write("product,amount\nSample,10.5\n")
        f.close()

    file = open(Fpath, newline='', encoding='utf-8')
    rdr = csv.DictReader(file)
    for R in rdr:
        R["amount"] = float(R["amount"])
        SALES.append(R)
    return SALES


def GenREPORT(SALES):
    Tot=0
    for S in SALES:
        Tot = Tot + S["amount"]

    print("Total Sales: $"+str(Tot))

    prd = {}
    for X in SALES:
        k = X["product"]
        if k not in prd:
            prd[k]=0
        prd[k] = prd[k] + X["amount"]

    for p in prd:
        print(p,": $",prd[p])

    f = open("REPORT.TXT","w")
    for P,A in prd.items():
        f.write(P+" : "+str(A)+"\n")
    f.write("TOTAL SALES="+str(Tot))
    f.close()

    os.remove("sales.csv")



if __name__ == "__main__":
    SalesDATA = ReadSales("sales.csv")
    GenREPORT(SalesDATA)
    input("Press ENTER to EXIT")
