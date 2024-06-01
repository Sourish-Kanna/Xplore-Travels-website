from flask import Flask, render_template
import json
import dbms
import re

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

@app.route('/tag/<tag_id>')
def city_select(tag_id):
    value = dbms.getcitys(tag_id)
    data = json.dumps(value)
    return render_template("activity.html",tag=data, t_name=tag_id)

@app.route('/city/<city>')
def display_city(city):
    value=dbms.get_destination_info(city)
    data = json.dumps(value)
    c_name = re.sub(r'\(.*?\)', '', city).strip()
    value1 = [city.split()[0]+str(x) for x in range(1,5)]
    data1 = json.dumps(value1)
    return render_template("city.html", city_slide=data1, city=c_name, city_detail=data)

@app.route("/<click>")
def other(click):
    return render_template(template_name_or_list=f"{click}.html")

if __name__ == '__main__':  
   import webbrowser
   webbrowser.open("http://127.0.0.1:5000/")
   app.run()
