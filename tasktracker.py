import os
import json
import argparse

pares = argparse.ArgumentParser()
sub_pares = pares.add_subparsers(dest="command")

#--------------add------------------------------
add_pares = sub_pares.add_parser("add",help="add task need task instring format")
add_pares.add_argument("task",type=str)

#------------list----------------------------
list_pares = sub_pares.add_parser("list",help="list the task")
list_pares.add_argument("all", default="all",choices=["todo","all","doing","done"])

#-------------update--------------------
update_pares = sub_pares.add_parser("update",help="update the status of task")
update_pares.add_argument("id",type=int)
update_pares.add_argument("status",choices=["done","doing","todo"])

args = pares.parse_args()

l = []

jfile = "/home/anubhav/tasklog.json"
if not os.path.exists(jfile):
    with open(jfile,"w") as j:
        json.dump([],j)
        j.close()
with open(jfile,"r") as f:
    l = json.load(f)
print()
i = len(l)
if args.command == "add":
    i += 1
    l.append({"id":f"{i}","name":f"{args.task}","status":"todo"})
    print(f"task {args.task} is added")
if args.command == "update":
    if args.status == "doing":
        l[args.id - 1]["status"] = "doing"
    if args.status == "done":
        l[args.id - 1]["status"] = "done"
    if args.status == "todo":
        l[args.id - 1]["status"] = "todo"
if args.command == "list":
    if args.all == "all":
        for x in l:
            print(x["id"],":", x["name"],":",x["status"])
    if args.all == "todo":
        for x in l:
            if x["status"] == "todo":
                print(x["id"],":", x["name"],":",x["status"])
    if args.all == "done":
        for x in l:
            if x["status"] == "done":
                print(x["id"],":", x["name"],":",x["status"])
    if args.all == "doing":
        for x in l:
            if x["status"] == "doing":
                print(x["id"],":", x["name"],":",x["status"])
with open(jfile,"w") as f1:
    json.dump(l,f1)
