from pysword.modules import SwordModules
from pysword.bible import SwordBible
import pysword
from . import bibles

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('fible', __name__)

@bp.route('/')
def main():
    collection = bibles.Bibles("/Users/david/.sword")
    print(request.args)
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
    return render_template('index.html', data = data)
