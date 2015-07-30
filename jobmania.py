#imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import requests
import json

#config
DEBUG = False
SECRET_KEY = 'Claire'

#creating the application
app = Flask(__name__)
app.config.from_object(__name__)

#submitting the web form
@app.route('/search', methods=['GET'])
def search():
	print (request.args)
	keyword = request.args.get('keywords')
	postcode = request.args.get('postcode')
	r = requests.request('GET', "http://api.lmiforall.org.uk/api/v1/vacancies/search?", params={'keywords':keyword, 'postcode':postcode})
	data = json.loads(r.content)
	return render_template('search.html', results=data)

#creating the index page
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

#creating the job page
@app.route('/job/<int:job_id>', methods=['GET'])
def job(job_id):
	r = requests.request('GET', "http://api.lmiforall.org.uk/api/v1/vacancies/search?", params={'keywords':job_id})
	data = json.loads(r.content)
	return render_template('job.html', job=data[0])

#starting the server
if __name__ == ('__main__'):
    app.run()

