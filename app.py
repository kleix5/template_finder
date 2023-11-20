from flask import Flask, request, redirect, url_for, flash, render_template
from tinydb import TinyDB, Query
import re
import json

app = Flask(__name__)
db = TinyDB('db.json')

def get_collection(data):
    collection = {}
    for k, v in data.items():
        ks = k.split('_')
        if ks[0] == 'name':
            collection[v] = data['type_' + ks[1]]
        elif k == 'template_name':
            collection['name'] = v
    return collection

def validation_replace(data):
    val_array = []
    for k, v in data.items():
        if re.fullmatch(re_date, v):
            val_array.append('date')
        elif re.fullmatch(re_phone, v):
            val_array.append('phone')
        elif re.fullmatch(re_email, v):
            val_array.append('email')
        elif re.fullmatch(re_text, v):
            val_array.append('text')
        else:
            val_array.append('Shit happens!')
        result = len(val_array) == len(query)
    if val_array[0] == 'Shit happens!':
        return False, val_array
    else:
        return val_array

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/add_form', methods=["POST"])
def add_form():
    if request.method == "POST":
        data = get_collection(request.form.to_dict())
        db.insert(data)
        return "new tamplete was added"
    
@app.route('/get_form', methods=["POST"])
def get_form():
    if request.method == "POST":
        data = get_collection(request.form.to_dict())
        data = validation_replace(data)

            
# всё, что нужно передаётся постом и пишется в файл, осталось реализовать валидацию и вернуть необходимые данные           
        return data
 
    
@app.route("/db_structure")
def db_structure():
    return db.all()
        