from flask import Flask,render_template,request
import requests
import json

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    
    if(request.method=='POST'):
        city = request.form['city']
        country = request.form['country']
        api_key = "5a49289c4c702200245509905c5f8672"

        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={api_key}&q={city},{country}&units=imperial')
        weather_data = weather_url.json()
        
        temperature = weather_data['list'][0]['main']['temp']
        humidity = weather_data['list'][0]['main']['humidity']
        wind_speed = weather_data['list'][0]['wind']['speed']

        return render_template("results.html",temperature=temperature,humidity=humidity,wind_speed=wind_speed,city=city)
    
    return render_template("index.html")

if(__name__=="__main__"):
    app.run(debug=True)
