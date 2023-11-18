import re
import json


re_text = re.compile(r'\w+\s?\w+')
re_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
re_phone = re.compile(r'\+\d*[\s(-]{0,2}\d*[\s)-]{0,2}\d*[\s-]?\d*[\s-]?\d*')
re_date = re.compile(r'\d{1,4}\W\d{1,2}\W\d{1,4}')

def validfunc(query):
    val_array = []
    for k, v in query.items():
        if re.fullmatch(re_phone, v):
            val_array.append('phone')
        elif re.fullmatch(re_text, v):
            val_array.append('text')
        elif re.fullmatch(re_email, v):
            val_array.append('email')
        elif re.fullmatch(re_date, v):
            val_array.append('date')
        else:
            val_array.append('Shit happens!')
        result = len(val_array) == len(query)
    if val_array[0] == 'Shit happens!':
        result = False
    print(val_array)
    print(query)
    return  result