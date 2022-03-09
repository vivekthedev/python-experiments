import requests
import re
from bs4 import BeautifulSoup
from random import choice

# plate = "UP32AT5471"


def get_request_for_number(plate):
    headers = {
        #    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
    }
    url = "https://vahaninfos.com/vehicle-details-by-number-plate"
    res = session.get(url, verify=False)
    return re.findall('token = "([^"]*)"', res.text)[0]


# --- POST ---
def post_request_for_number(number, plate):
    headers = {
        "User-Agent": choice(agent),
        "num": number,
    }
    payload = {
        "number": plate,
        "g-recaptcha-response": "",
    }
    url = "https://vahaninfos.com/getdetails.php"
    res = session.post(url, data=payload, headers=headers, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup


plate = input("Enter the Plate Number ")
pattern = "^[A-Z]{2}[0-9]{1,2}(?:[A-Z])?(?:[A-Z]*)?[0-9]{4}"
m = re.match(pattern, plate)
if m:
    session = requests.Session()
    number = get_request_for_number(plate)
    agent = [
        "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Mozilla/5.0",
        "",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    ]
    soup = post_request_for_number(number, plate)
    while soup.find_all("td")[2].text == "R":
        soup = post_request_for_number(number, plate)

    for row in soup.find_all("tr"):
        cols = row.find_all("td")

        key = cols[0].text
        val = cols[-1].text

        print(f"{key:22} | {val}")
else:
    print("Invalid Number")
