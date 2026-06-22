import customtkinter as ctk
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

app = ctk.CTk()
app.geometry("600x400")
app.resizable(False, False)
app.title("Pogoda")
app.grid_columnconfigure(0, weight=1)

text_box = ctk.CTkTextbox(app, width=380, height=200)
text_box.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

entry = ctk.CTkEntry(
    app,
    width=200,
    height=30,
    placeholder_text="Podaj miasto..."
)
entry.grid(row=1, column=0, pady=10)


def get_weather(city):
    url = (
        f"http://api.openweathermap.org/data/2.5/forecast"
        f"?appid={API_KEY}&q={city}&lang=pl&units=metric"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        weather_description = data["list"][0]["weather"][0]["description"]
        temperature = data["list"][0]["main"]["temp"]
        humidity = data["list"][0]["main"]["humidity"]

        forecast = []

        used_dates = set()

        for item in data["list"]:
            date = item["dt_txt"].split(" ")[0]

            if date not in used_dates:
                used_dates.add(date)

                forecast.append({
                    "date": date,
                    "temp": item["main"]["temp"],
                    "desc": item["weather"][0]["description"]
                })

            if len(forecast) == 5: 
                break

        return weather_description, temperature, humidity, forecast

    except requests.exceptions.RequestException:
        return "Błąd pobierania danych", 0, 0, []


def change_city():
    city = entry.get().strip()

    if not city:
        return

    weather_description, temperature, humidity, forecast = get_weather(city)

    text_box.configure(state="normal")
    text_box.delete("0.0", ctk.END)

    text_box.insert(ctk.END, f"Pogoda w {city}: {weather_description}\n")
    text_box.insert(ctk.END, f"Temperatura: {temperature:.1f} ℃\n")
    text_box.insert(ctk.END, f"Wilgotność: {humidity}%\n\n")

    text_box.insert(ctk.END, "Prognoza na kolejne dni:\n")
    text_box.insert(ctk.END, "-" * 35 + "\n")

    for day in forecast:
        text_box.insert(
            ctk.END,
            f"{day['date']} | {day['temp']:.1f} ℃ | {day['desc']}\n"
        )

    text_box.configure(state="disabled")

    entry.delete(0, ctk.END)


button = ctk.CTkButton(
    app,
    text="Sprawdź pogodę",
    command=change_city
)
button.grid(row=2, column=0, pady=10)

entry.bind("<Return>", lambda event: change_city())

app.mainloop()