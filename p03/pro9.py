import requests

def get_weather(city):
    api_key = "308d0d91acd0611f592f0b26974fcdbc"  # kalide motabar khodet ro jaygozin kon
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # barresi movafagh boodan darkhast

        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌍 Vaziate hava dar {city}:")
        print(f"🌡 Dama: {temp}°C")
        print(f"💧 Rotubat: {humidity}%")
        print(f"🌥 Vaziat: {description}")
        print(f"🌀 Feshare hava: {pressure} hPa")
        print(f"🍃 Sorate baad: {wind_speed} m/s")

    except requests.exceptions.HTTPError as err:
        print("❌ Khata: Lotfan name shahr ro dorost vared konid.")
    except Exception as e:
        print("⚠️ Khatayi rokh dade:", e)

city_input = input("Name shahr ro vared konid: ")
get_weather(city_input)
