from app import app
from flask import render_template, request, jsonify
import requests
import json
import math
from config import api_key

@app.route("/")
def index():
		
	return render_template('index.html')

@app.route("/searchrequest", methods=['POST', 'GET'])
def searchrequest():

	news = { }
	results = 0
	totalpages = 0

	if request.method == 'GET':

		searchquery = request.args.get('searchrequest', '')
		begindate = request.args.get('begindate', '').replace('-', '')
		enddate = request.args.get('enddate', '').replace('-', '')
		page = request.args.get('page', '')

		if searchquery != "":

			if page == "":
				print ("empty")
				page = 0

			params = {'api-key' : api_key, 'q' : searchquery, 'begin_date' : begindate, 'end_date' : enddate, 'page' : page}

			try:
				r = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json", params=params)
				data = json.loads(r.content.decode('utf-8'))

				results = data['response']['meta']['hits']
				totalpages = math.ceil(data['response']['meta']['hits'] / 10)
				page = data['response']['meta']['offset'] / 10 + 1
				print (results, " ", totalpages, " ", page)

				for i in data['response']['docs']:
					news[(i['headline']['main'])] = (i['web_url'])

			except requests.exceptions.RequestException as e:
				print (e)


	return jsonify(news=news, results=results, totalpages=totalpages, page=page, searchquery=searchquery)
