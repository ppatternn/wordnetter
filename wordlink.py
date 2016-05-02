from textblob import Word
from flask import Flask, make_response, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('wordlink.html')

@app.route('/word/<term>')
def get_wordlinks(term):
    syns_list = list(set([syn.name[:-5] for syn in Word(term).synsets]))
    return jsonify({'syns': syns_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0') #app.debug = True
