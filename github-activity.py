import requests
import argparse

pares = argparse.ArgumentParser()
pares.add_argument("name",type=str,help="the name of usr")

args = pares.parse_args()

urls = f"https://api.github.com/users/{args.name}/events"

response = requests.get(urls)
data  = response.json()
url2 = f"https://api.github.com/repos/{data[0]["repo"]["name"]}/commits/{data[0]["payload"]["head"]}"
response2 = requests.get(url2)
data2 = response2.json()

print(f"Time: {data2["commit"]["committer"]["date"]}")
print(f"Event: {data[0]["type"]}")
print(f"Name: {data2["commit"]["committer"]["name"]}")
print(f"Repo: {data[0]["repo"]["name"]}")
print(f"Filename: {data2["files"][0]["filename"]}")
print(f"Commit: {data2["commit"]["message"]}")