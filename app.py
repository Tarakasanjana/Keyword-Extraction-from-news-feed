# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:55:49 2021

@author: Sanjana
"""

from monkeylearn import MonkeyLearn
from flask import Flask, request, render_template
import re
import requests

app = Flask(__name__)


#home page
@app.route('/')
def home():
    return render_template('home.html')

#home page
@app.route('/extractor')
def extractor():
    return render_template('extractor.html')

#extractor page
@app.route('/keywords',  methods=['POST'])
def keywords():
    ml = MonkeyLearn('d638287346fb2716398ec8eba984a1293a8c809d')
    typ=request.form['type']
    model_id ='ex_YCya9nrn'
    print(type)
    output = request.form['output']
    print(output)
    print(type(output))
    if typ=="text":
        output=re.sub("[^a-zA-Z.,]"," ",output)
    print(output)
   
    
    keywordresult = ml.extractors.extract(model_id,[output])
    print(keywordresult.body)
    a = keywordresult.body[0]
    print (a)
    print(type(a))
    b = a['extractions']
    print(b)
    print(type(b))
    
    keywords = []
    entities = []
    
    for i in b:
        keywords.append(i['parsed_value'])
        print (i['parsed_value'])
        
    print(keywords)
   

    
    #return keyword
    return render_template('keywords.html',keyword=keywords)

    
if __name__ == "__main__":
    app.run(debug=False)