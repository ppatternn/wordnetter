from textblob import Word
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('wordlink.html')

@app.route('/', methods=['POST'])
def get_wordlinks():
    results = []
    for ss in Word(request.form['term']).synsets:
        for ln in ss.lemma_names():
            results.append(ln.encode('ascii', 'replace'))
        for sim in ss.similar_tos():
            for simln in sim.lemma_names():
                results.append(simln.encode('ascii', 'replace'))
    syns = {'syns': list(set(results))}
    return jsonify(syns)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
