from flask.helpers import make_response
from pysword.modules import SwordModules
from pysword.bible import SwordBible
import pysword
from . import bibles
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('fible', __name__)

#make this route settable

@bp.route('/bible')
def bible():
    #make this path settable
    collection = bibles.Bibles("./.sword")
    print(request.args)
    #make default book, version settable
    version = "DRC"
    book = "Matt"
    if "version" in request.args: version = request.args["version"] 
    if "book" in request.args: book = request.args["book"]
    if "everse" in request.args: 
        if request.args["everse"] != "All": verses = [int(request.args["sverse"]), int(request.args["everse"])]
        else: verses = None
        print(request.args["sverse"])
    if "chapter" in request.args: data = collection.return_page_data(book, version, [int(request.args["chapter"])], verses) 
    else: data = collection.return_page_data(book, version)
    if "type" in request.args:
        if request.args["type"] == "text":
            response = make_response("\n".join(data["text"]), 200)
            response.mimetype = "text/plain"
            return response
    
    return render_template('bible.html', data = data)

@bp.route('/')
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
