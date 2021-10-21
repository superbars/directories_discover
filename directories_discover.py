import requests

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

taget_url = str(input("[!!!] Please write full URL of target: "))
wordlist = str(input("[!!!] Please specify your wordlist: "))
print("PLease wait...")
file = open(wordlist, "r")
for line in file:
    word = line.strip()
    full_url = taget_url + "/" + word
    response = request(full_url)
    if response:
        print("[*] Link was discovered: " + full_url)