import os
from flask import Flask, redirect, request, render_template, url_for
import requests
import json
import sys

apikey = sys.argv[1]
app = Flask(__name__, template_folder='template')

session = requests.Session()
session.trust_env = False

port = int(os.getenv("PORT", 5500))

@app.route('/home', methods=['POST'])
def mediator():
    wordx = request.form['wordx']
    print("### Lookup api-collegiate-dictionary for Word {0} ###".format(wordx))

    # CONNECTION with other app
    url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + str(wordx) + '?key=' + str(apikey)
    # print(url)
    try:
        r = session.get(url=url)
        print(r.status_code)
        #print(r.text)
        r.encoding = 'utf-8'

        res = json.loads(r.text)

        spell = str(str(res[0]['hwi']['hw']) + ' ' + str(res[0]['def'][0]['sseq'][0][0][1]['dt'][0][1]))

        #print(spell)

        return render_template('output.html', wordx=wordx, answer=spell)
    except:
        print('Connecting Error or Bad Response from API')
        return render_template('error.html')


@app.route('/reset', methods=['POST'])
def default_route():
    return render_template('index.html')


@app.route('/')
def default_route2():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)