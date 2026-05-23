import zipfile
import os
import  argparse

pares = argparse.ArgumentParser()
pares.add_argument("--d",help="decompresess",required=False,type=str)
pares.add_argument("--c",help="compresss",required=False,type=str)

args = pares.parse_args()

if args.c:
    name = os.path.splitext(args.c)[0]
    if os.path.exists(args.c):
        
        with zipfile.ZipFile(f"{name}.zip","w",compression=zipfile.ZIP_DEFLATED) as  z:
            z.write(args.c,arcname=os.path.basename(args.c))
            print("compress complete")
elif args.d:
    name = os.path.splitext(args.d)[0]
    if os.path.exists(args.d):
        
        with zipfile.ZipFile(args.d,"r") as z:
            z.extractall(name)
            print("extract complete")
