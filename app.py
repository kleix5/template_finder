from flask import Flask, request, redirect, url_for, flash, render_template
from tinydb import TinyDB, Query
import re
import json

app = Flask(__name__)
db = TinyDB('db.json')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/add_form', methods=["POST"])
def add_form():
    if request.method == "POST":
        data = request.form.to_dict()
        collection = {}
        for k, v in data.items():
            ks = k.split('_')
            if ks[0] == 'name':
                collection[v] = data['type_' + ks[1]]
            elif k == 'template_name':
                collection['name'] = v
        db.insert(collection)
        return "new tamplete was added"
    
@app.route('/get_form', methods=["POST"])
def get_form():
    if request.method == "POST":
        data = request.form.to_dict()
        collection = {}
        for k, v in data.items():
            ks = k.split('_')
            if ks[0] == 'name':
                collection[v] = data['type_' + ks[1]]
            elif k == 'template_name':
                collection['name'] = v
        with open("get_form.json", "w") as my_file:
            my_file.write(json.dumps(collection))
            my_file.close()
#         for k, v in collection.items():
            
# всё, что нужно передаётся постом и пишется в файл, осталось реализовать валидацию и вернуть необходимые данные           
        return data
 
    
@app.route("/db_structure")
def db_structure():
    return db.all()
        