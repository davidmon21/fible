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
    if "version" in request.args:
        bible = collection.ready_bible(request.args["version"])
        book = request.args["book"]
        sversion = request.args["version"]
    else:
        bible = collection.ready_bible("DRC")
        book = "Matt"
        sversion = "DRC"
    if "chapter" in request.args:
        chap = request.args["chapter"]
        text = bible.get(books=[book], chapters=[int(request.args["chapter"])])
    else:
        text = bible.get(books=[book], chapters=[1])
        chap = 1
    chapters = range(1,bible.get_structure().find_book(book)[1].num_chapters+1)
    return render_template('index.html', books = collection.return_books(), bible = bible, collections = collection, book = book, chap = chap, text = text, sversion = sversion, chapters = chapters)


@bp.route('/script')
def script():
    outputer = []
    scrip = request.args.get('book', '')
    for chapter in range(1,bible.get_structure().find_book(scrip)[1].num_chapters+1):
        verse2 = list(range(1,int(bible.get_structure().find_book(scrip)[1].chapter_lengths[chapter-1])+1))
        outputer.append([int(chapter), verse2])
    return render_template('script.html', content = [scrip, bible.get(books=[scrip], chapters=[outputer[0][0]], verses=outputer[0][1]).splitlines()])


