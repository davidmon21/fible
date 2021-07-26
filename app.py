from flask.helpers import make_response
from pysword.modules import SwordModules
from typing import DefaultDict
from pysword.bible import SwordBible
import pysword
import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


class Bibles:
    bible_collection = None
    sword = None
    def __init__(self, bibles_path):
        self.sword = SwordModules(bibles_path)
        self.bible_collection = self.sword.parse_modules()

    def return_page_data(self, book, version, chapter = [1], verses = None):
        bible = self.sword.get_bible_from_module(version)
        textual_data = DefaultDict()
        textual_data["books"] = bible.get_structure().get_books()
        textual_data["book"] = "Matt"
        for title in textual_data["books"]['ot']:
            #print(textual_data["books"])
            if title.osis_name.lower() == book.lower():
                textual_data["book"] = book
        for title in textual_data["books"]['nt']:
            #print(textual_data["books"])
            if title.osis_name.lower() == book.lower():
                textual_data["book"] = book
        textual_data["chapters"] = range(1,bible.get_structure().find_book(book)[1].num_chapters+1)
        if chapter[0] in textual_data["chapters"]: textual_data["chapter"] = chapter[0]
        else: textual_data["chapter"] = 1
        textual_data["name"] = bible.get_structure().find_book(book)[1].name
        textual_data["collection"] = self.bible_collection
        textual_data["version"] = version
        textual_data["verses"] = list(range(1,bible.get_structure().find_book(book)[1].chapter_lengths[chapter[0]-1]+1))
        if verses != None:
            if verses[1] in textual_data["verses"] and ((verses[0] <= verses[1]) & verses[0] >= 1):
                textual_data["selected_verses"] = list(range(verses[0], verses[1]+1))
            else: textual_data["selected_verses"] = textual_data["verses"]
        else:
            textual_data["selected_verses"] = textual_data["verses"]
        textual_data["text"] = bible.get(books=[book],  chapters=chapter, verses=textual_data["selected_verses"]).split("\n")
        textual_data["text"] = [i for i in textual_data["text"] if i]
        return textual_data

@app.route('/bible')
def bible():
    #make this path settable
    collection = Bibles("./.sword")
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