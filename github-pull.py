import requests

#To get output of all whole available data
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls") #https://api.github.com/repos/{owner}/{repo}/pulls
output = response.json()

#To get output of specific data
print(output[0]["id"])
print(output[0]["user"]["url"])

#To filter out login information from whole data 
for i in range(len(output)):
    print(output[i]["user"]["login"])


