from flask.helpers import make_response
import json
import os
from bibles import Bibles
from prayers import Prayers
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

@app.route('/bible')
def bible():
    #make this path settable
    collection = Bibles("./.sword")
    #make default book, version settable
    version = "DRC"
    book = "Matt"
    if "version" in request.args: version = request.args["version"] 
    if "book" in request.args: book = request.args["book"]
    if "everse" in request.args: 
        if request.args["everse"] != "All": verses = [int(request.args["sverse"]), int(request.args["everse"])]
        else: verses = None
    if "chapter" in request.args: data = collection.return_page_data(book, version, [int(request.args["chapter"])], verses) 
    else: data = collection.return_page_data(book, version)
    if "type" in request.args:
        if request.args["type"] == "text":
            response = make_response("\n".join(data["text"]), 200)
            response.mimetype = "text/plain"
            return response
    
    return render_template('bible.html', data = data)

@app.route('/prayer')
def prayer():
    prayer_builder = Prayers()
    prayer="OurFather"
    supplemental=None
    if "prayer" in request.args:
        if request.args["prayer"] in prayer_builder.prayers:
            prayer = request.args["prayer"]
            if "supl" in request.args:
                supplemental = request.args["supl"]
            compiled_prayer = prayer_builder.compile_prayer(prayer,supplemental)
            return render_template('prayer.html', prayer = compiled_prayer)



@app.route('/')
def index():
    if "page" in request.args:
        if request.args["page"] == "timeline":
            with open('events.json', 'r') as f:
                events = json.load(f)
            
            
            return render_template("timeline.html", events=events)
        else:
            return render_template(request.args["page"]+'.html')
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)