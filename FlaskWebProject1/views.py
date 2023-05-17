"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)
from FlaskWebProject1 import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hash_text', methods=['POST'])
def hash_text():
    text = request.form['text']

    noko = subprocess.Popen(["python", "hashid.py", text], stdout=subprocess.PIPE)

    output = noko.stdout.read().decode('utf-8').strip()
    
    if "MD5" in output:
        output_formatted = "MD5 hash function identified."
    elif "SHA-256" in output:
        output_formatted = "SHA-256 hash function identified."
    elif "SHA-384" in output:
        output_formatted = "SHA-384 hash function identified."
    elif "SHA-512" in output:
        output_formatted = "SHA-512 hash function identified."
    elif "Blowfish" in output:
        output_formatted = "Blowfish hash function identified."
    elif "Whirlpool" in output:
        output_formatted = "Whirlpool hash function identified."
    elif "Snefru" in output:
        output_formatted = "Snefru hash function identified."
    else:
        output_formatted = "Hash function not identified. Please try again with a valid hash."
    
    return redirect(url_for('output1', output=output_formatted))

@app.route('/output1')
def output1():
    output_formatted = request.args.get('output')
    return render_template('output1.html', output=output_formatted)


@app.route('/about')
def about():
    return render_template('about.html')
