import argparse 

pares = argparse.ArgumentParser()
sub_pares = pares.add_subparsers(dest="command")
pares.add_argument("--block",required=False,type=str)
pares.add_argument("--unblock",required=False,type=str)
list_pares = sub_pares.add_parser("list")
args = pares.parse_args()

file_path = "/etc/hosts"

fline = None
if args.block:
    with open(file_path,"a") as f:
        f.write(f"127.0.0.1 www.{args.block}\n")
        f.write(f"::1 www.{args.block}\n")
        f.write(f"127.0.0.1 {args.block}\n")
        f.write(f"::1 {args.block}\n")
elif args.unblock:
    with open(file_path, "r") as f:
        fline = f.readlines()
    with open(file_path,"w") as f:
        for line in fline:
            if args.unblock not in line:
                f.write(line)
    
if args.command == "list":
    with open(file_path, "r") as f:
        fline = f.readlines()
        for line in fline:
            print(line)