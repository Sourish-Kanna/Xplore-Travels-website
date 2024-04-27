from flask import request, Flask, render_template
import webbrowser 
import json
import dbms

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tag")
def tag():
    value = dbms.gettags()
    data = json.dumps(value)
    return render_template(template_name_or_list="tag.html",tag=data)

@app.route('/tag/<city>')
def city_select(city):
    value = dbms.getcitys(city)
    data = json.dumps(value)
    return render_template("activity.html",tag=data)

@app.route('/city/<city>')
def display_city(city):
    value1 = ("Rishikesh2","Kerala2","Kanha4","bangalore5")
    data1 = json.dumps(value1)
    value = dbms.getcitys(city)
    data = json.dumps(value)
    return render_template("city.html", city_slide=data1, city=city, city_detail=data)

@app.route("/<click>")
def other(click):
    return render_template(template_name_or_list=f"{click}.html")

if __name__ == '__main__':  
   webbrowser.open("http://127.0.0.1:5000/")
   app.run()
