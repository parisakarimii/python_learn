import requests
import json

def save_weather_data(city, temperature, humidity, description):
    weather_record = {
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "condition": description
    }
    with open("weather_data.json", "a", encoding="utf-8") as file:
        json.dump(weather_record, file, ensure_ascii=False)
        # اما وقتی ensure_ascii=False می‌ذاری، کاراکترهای غیر ASCII دقیقاً به همون شکل اصلی و خوانا تو فایل نوشته میشن، یعنی مثلاً حروف فارسی مستقیم تو فایل ذخیره میشن و راحت می‌تونی بخونی یا ویرایش کنی.
        file.write("\n")
    print("✅ Etela'at be file zakhire shod!")

api_key = input("API key ra vared konid: ").strip()

while True:
    city = input("Name shahr ra vared konid (baraye khorooj 'exit' benevisid): ").strip()
    if city.lower() == "exit":
        break

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fa"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        print(f"\nShahr: {city}")
        print(f"Dama: {temp}°C")
        print(f"Rotubat: {humidity}%")
        print(f"Vaziyat: {description}")
        save_weather_data(city, temp, humidity, description)
    else:
        print("⚠ Shahr peyda nashod! Lotfan esm dorost vared konid.")
