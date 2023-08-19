import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishtofrench")
def englishtofrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchtext = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(englishtext)
    return "Translated text to French"

@app.route("/frenchtoenglish")
def frenchtoenglish():
    textToTranslate = request.args.get('textToTranslate')
    englishtext = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(frenchtext)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
