import requests

def get_weather_icon(description):
    description = description.lower()
    RESET = "\033[0m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    GRAY = "\033[90m"
    RED = "\033[91m"
    ORANGE = "\033[33m"  

    if "صاف" in description:
        return f"{YELLOW}☀{RESET}"
    elif "ابری" in description:
        return f"{GRAY}☁{RESET}"
    elif "بارانی" in description :
        return f"{BLUE}🌧{RESET}"
    elif "برفی" in description:
        return f"{WHITE}❄{RESET}"
    elif "طوفانی" in description:
        return f"{RED}⛈{RESET}"
    else:
        return f"{ORANGE}🌥{RESET}"


def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fa"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        icon = get_weather_icon(description)
        print(f"\n🏙 Shahr: {city}")
        print("──────────────")
        print(f"{icon} Vaziyat: {description}")
        print(f"🌡 Dama: {temp}°C")
        print(f"💧 Rotoobat: {humidity}%")
        return True
    else:
        print("⚠ Shahr peyda nashod! Lotfan esm shahr ra dorost vared konid.")
        return False

print("🔑 API Key khod ra vared konid:")
api_key = input().strip()

print("\n🔁 Baraye khorooj 'exit' ra vared konid.")

while True:
    city = input("Name shahr ra vared konid: ").strip()
    if city.lower() == "exit":
        break
    success = get_weather(city, api_key)
    while not success:
        city = input("Dobare esm shahr ra dorost vared konid ya 'exit' baraye khorooj: ").strip()
        if city.lower() == "exit":
            exit()
        success = get_weather(city, api_key)
