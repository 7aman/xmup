import requests
import json

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)'
}

def get_all():
    url = 'http://120.92.92.241:8083/firmware'
    try:
        response = requests.get(url, headers=headers)
        result = json.loads(response.text)
    except requests.exceptions.ConnectionError:
        print("Connection Error. Try again later.")
        exit()
    return result["versions"]

def search(devid, db):
    result = []
    for key in db.keys():
        if devid in key:
            result.append(db[key][0])
    return result

def check(devid):
    url = 'http://120.92.92.241:8083/list'
    req = {
        "UUID": "",
        "DevID": devid["DevID"],
        "DevType": "",
        "CurVersion": "2000-01-01",
        "Expect": "Latest",
        "Language": "English",
        "Manual": "True"
    }
    try:
        response = requests.post(url, json=req, headers=headers)
        result = json.loads(response.text)
        return result
    except requests.exceptions.ConnectionError:
        print("Connection Error. Try again later.")
        exit()


def download(devid, path, info):
    url = 'http://120.92.92.241:8083/download'
    req = {
        "UUID":"",
        "DevID": devid["DevID"],
        "FileName": devid["FileName"],
        "Date": devid["Date"],
        "Manual":"True"
    }
    try:
        print('Downloading...')
        file = path.joinpath(req["FileName"])
        if file.exists():
            print(f"file {file.absolute()} exists on Download folder. skipping...")
        else:
            response = requests.head(url, json=req, headers=headers)
            if response.status_code == 200:
                response = requests.post(url, json=req, headers=headers)
                with open(file, 'w+b') as binfile:
                    binfile.write(response.content)
                with open(file.with_suffix('.txt'), 'w') as txtfile:
                    txtfile.write(info)
                print(f"Saved as {file.absolute()}\n")
            else:
                print(f"Something went wrong. Status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("Connection Error. Try again later.")
        exit()
