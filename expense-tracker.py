import argparse
import json
import os
import time
cfile = "/home/anubhav/expenselog.json"
pares = argparse.ArgumentParser()
sub_pares = pares.add_subparsers(dest="command")

#----------------add-------------------------
add_pares = sub_pares.add_parser("add")
add_pares.add_argument("--description",required=True,type=str)
add_pares.add_argument("--amount",required=True,type=int)

#----------------list-------------------------
list_pares = sub_pares.add_parser("list")

#---------------summary---------------------
summary_pares = sub_pares.add_parser("summary")
summary_pares.add_argument("--month",required=False,type=int)
#--------------delete---------------------------
del_pares = sub_pares.add_parser("delete")
del_pares.add_argument("--id",required=True,type=int)

args = pares.parse_args()
l = []

current = time.strftime("%d:%m:%Y")
if not os.path.exists(cfile):
    with open(cfile,"w") as f:
        json.dump(l,f)
        f.close()
with open(cfile,"r") as f:
    l = json.load(f)
    if args.command == "list":
        print("ID, Date, Description, amount")
        for x in l:
            print(f"{x["id"]}, {x["date"]}, {x["des"]}, {x["amount"]}")
    elif args.command == "summary":
        
        total = 0
        if args.month:
            for x in l:
                if int(x["month"]) == args.month:
                    total += int(x["amount"])
        else: 
            for x in l:
                total += int(x["amount"])
        print(f"summary: {total}")  

    elif args.command == "delete":
        for x in l:
            d_id = int(x["id"])
            if d_id == args.id:
                x = l.pop(args.id - 1)
j = 0 
for x in l:
    j += 1
    x["id"] = j
length = len(l)
i = length
if args.command == "add":
    if args.amount > 0:
        with open(cfile,"w") as f:
            i += 1
            l.append({"id":f"{i}","date":f"{current}","des":f"{args.description}","amount":f"{args.amount}","month":f"{time.strftime("%m")}"})
            f.close()
    else:
        print("enter valid amount")
with open(cfile,"w") as f:
    json.dump(l,f)