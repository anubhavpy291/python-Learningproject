
import os
import json
import csv
file = "README.md"
filej = "data.json"
filec = "dats.csv"
try:
    with open(file, "w") as files:
        files.write("This is a README file for the learning project.")
    with open(file, "a") as f:
        f.write("   this is for learning purpose")
    with open(file, "x") as f:
        f.write("   this is for learning purpose")
except FileNotFoundError:
    print("file dont found")

except FileExistsError:
    print("file already exist")
try:
    with open(filej, "x") as fj:
        json.dump("hellow", fj)
    with open(filec, "x") as fc:
        w =  csv.writer(fc)
        w.writerow("wsup")
except FileExistsError:
    print("file already exist")

#----------reaadfile----

files = "README.md"

try:
    with open(files,"r") as file:
        content = file.read()
        print(content)
    with open(filej, "r") as rfj:
        contentj = json.load(rfj)
        print(contentj)
    with open(filec, "r") as rfc:
        reader = csv.reader(rfc)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"the file {files} does not exist")
