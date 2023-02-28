import requests
import smtplib

MY_LAT = 51.472160
MY_LONG = -0.165410
API = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "ca7de53f1eeab5bbdf32d0b94c559f46"

def send_mail():
    my_email = "darnelllearnscoding@gmail.com"
    password = "iwdxegfntusngpdr"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs="darnelllearnscoding@yahoo.com",
                        msg=f"Subject:Weather Update\n\n{email_msg}")
    connection.close()


para = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

api_response = requests.get(API, params=para)

will_rain = False

weather_data = api_response.json()
weather_slice = weather_data["list"][:4]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True


if will_rain:
    email_msg = "Bring an umbrella"
else:
    email_msg = "You cool, no rain coming"

send_mail()