from textblob import Word
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('wordlink.html')

@app.route('/find/')
def get_wordlinks():
    term1 = request.args.get('term1')
    term2 = request.args.get('term2')

    results1 = get_syns_list(term1)
    results2 = get_syns_list(term2)

    common = list(set(results1) & set(results2))

    return render_template('wordlink.html',
                           term1=term1,
                           term2=term2,
                           results1=results1,
                           results2=results2,
                           common=common)

def get_syns_list(term):
    results = []
    for ss in Word(term).synsets:
        for ln in ss.lemma_names():
            results.append(ln.encode('ascii', 'replace'))
        for sim in ss.similar_tos():
            for simln in sim.lemma_names():
                results.append(simln.encode('ascii', 'replace'))
    return list(set(results))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
