import json
import requests

api_key = "308d0d91acd0611f592f0b26974fcdbc"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]
        print(f"\nHava dar {city}:")
        print(f"Damā: {temp}°C")
        print(f"Rotubat: {humidity}%")
        print(f"Vaziate Hava: {desc}")
        return {"city": city, "temp": temp, "humidity": humidity, "desc": desc}
    else:
        print("Shahr peyda nashod!")
        return None

def save_weather_data(record):
    try:
        with open("weather_data.json", "a", encoding="utf-8") as file:
            json.dump(record, file, ensure_ascii=False)
            file.write("\n")
        print("✅ Data-ye hava zakhire shod!")
    except Exception as e:
        print("Eshtebāh dar zakhire data:", e)

def view_past_weather():
    try:
        with open("weather_data.json", "r", encoding="utf-8") as file:
            print("\nRekordhā-ye ghabli:")
            for line in file:
                record = json.loads(line)
                print(record)
    except FileNotFoundError:
        print("Rekord ghabli peyda nashod.")

def clear_records():
    open("weather_data.json", "w").close()
    print("🗑️ Tamām rekordhā pak shodand!")

def compare_cities(city1, city2):
    w1 = get_weather(city1)
    w2 = get_weather(city2)
    if w1 and w2:
        print("\nMoqāyeshe:")
        print(f"{city1} Damā: {w1['temp']}°C | {city2} Damā: {w2['temp']}°C")
        print(f"{city1} Rotubat: {w1['humidity']}% | {city2} Rotubat: {w2['humidity']}%")
        print(f"{city1} Vaziate Hava: {w1['desc']} | {city2} Vaziate Hava: {w2['desc']}")

def menu():
    while True:
        print("\n🌦 Menyu-ye Hava")
        print("1. Daryāft-e havā-ye fa'āl")
        print("2. Didan-e rekordhā-ye ghabli")
        print("3. Pak kardan-e tamām rekordhā")
        print("4. Moghayese-ye havā-ye do shahr")
        print("5. Khoruj")
        choice = input("Entekhab-e shomā: ")
        if choice == "1":
            city = input("Esme shahr rā vared konid: ")
            record = get_weather(city)
            if record:
                save_weather_data(record)
        elif choice == "2":
            view_past_weather()
        elif choice == "3":
            clear_records()
        elif choice == "4":
            city1 = input("Esme shahr-e aval: ")
            city2 = input("Esme shahr-e dovom: ")
            compare_cities(city1, city2)
        elif choice == "5":
            print("Khoda hafez! ☀️")
            break
        else:
            print("Entekhab nādorost ast. Dovbārā talāsh konid.")

menu()
