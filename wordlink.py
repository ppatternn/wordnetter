"""
wordlink
Robert Florance
"""
from textblob import Word
from flask import Flask, make_response, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('wordlink.html')

@app.route('/wordlink_ng')
def home_ng():
    return make_response(open('templates/wordlink_ng.html').read())

@app.route('/word/<term>')
def get_wordlinks(term):
    syns_list = get_synonym_list(term)
    trys = 0
    #while (len(syns_list) < 10 and trys < 5):
    #   trys += 1
    #   for syn in syns_list:
    #       syns_list += get_synonym_list(syn)
    #       syns_list = list(set(syns_list))
    response_obj = {'syns': syns_list}
    return jsonify(response_obj)

def get_synonym_list(term):
    synsets = Word(term).synsets
    return list(set([syn.name[:-5] for syn in synsets]))

if __name__ == '__main__':
   app.run(host='0.0.0.0')
   #app.debug = True
   #app.run()
