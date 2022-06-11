import pprint
import requests
import datetime


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude")
    }
    return location_data


def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    file = f"location_check_{now}.txt"
    pretty_print = pprint.pformat(get_location())

    with open(file, "a") as f:
        f.write(pretty_print + "\n\n")


if __name__ == "__main__":
    main()
