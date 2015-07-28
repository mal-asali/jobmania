#imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import requests

#config
DEBUG = True
SECRET_KEY = 'development key'

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
	return (r.content)

#creating the index page
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

#starting the server
if __name__ == ('__main__'):
    app.run()

