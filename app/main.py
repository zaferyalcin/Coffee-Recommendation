from email import header
from email.mime import application
from flask import Flask, request, jsonify
import app.ai_coffee_recommendation as ai_coffee_recommendation 

app = Flask(__name__)

@app.route("/")
def home():
        return "<h1>Welcome to Coffee Recommendation system</h1>"


@app.route("/coffees")
def coffees():
        data =ai_coffee_recommendation.get_all_coffee_names()
        data_1=[];
        for item in data:
                data_1.append({'coffee_name':item})
        return jsonify(data_1)


@app.route("/closest",methods=['POST'])
def closest():
        data = request.get_json()
        print(data['coffee_name'])
        coffeeList = ai_coffee_recommendation.get_coffee_recommendation(data['coffee_name'])
        print(coffeeList)
        return coffeeList