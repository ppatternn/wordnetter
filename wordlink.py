"""
wordlink
Robert Florance
"""
import json
from textblob import Word
from flask import Flask

app = Flask(__name__)

@app.route('/word/<term>')
def get_synset(term):
    print(term)
    synsets = Word(term).synsets
    syns = list(set([syn.name[:-5] for syn in synsets]))
    result = json.dumps(syns)
    return result

if __name__ == '__main__':
    app.debug = True
    app.run()


