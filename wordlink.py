"""
wordlink
Robert Florance
"""
from textblob import Word
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('wordlink.html')

@app.route('/word/<term>')
def get_synset(term):
    synsets = Word(term).synsets
    syns_raw = list(set([syn.name[:-5] for syn in synsets]))
    syns = {'syns': syns_raw}
    return jsonify(syns)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

#if __name__ == '__main__':
#   app.debug = True
#   app.run()

