#Imports
import nltk
import os
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
# import tflearn
import tensorflow as tf
import random
import json
import pickle
from flask import Flask, render_template, request, jsonify


#Loading Data
with open("intents.json") as file:
	data = json.load(file)
    
print(data['intents'])	
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/get')
def get_bot_response():
	# global seat_count
	message = request.args.get('msg')
	for tg in data['intents']:
					if tg['tag'] == tag:
						responses = tg['responses']
				# response = random.choice(responses)
				# print(response)	
	return message
if __name__ == "__main__":
	app.run()