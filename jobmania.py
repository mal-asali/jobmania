from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

#config
DEBUG = True
SECRET_KEY = 'development key'

#creating the application
app = Flask(__name__)
app.config.from_object(__name__)
if __name__ == '__main__':
    app.run()

