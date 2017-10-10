from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'change to environ variable later'