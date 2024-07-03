from flask import Blueprint
from flask import render_template
from analysis_dictionary_make import create_dict
import random
#16
views = Blueprint('views',__name__)
analysis_words_dictionary = create_dict()
keys = list(analysis_words_dictionary.keys())

@views.route('/')
def main():
    word = random.choice(keys)
    definition = analysis_words_dictionary[word][2]
    year = analysis_words_dictionary[word][16]
    return render_template("main.html",
                           word = word,
                           definition = definition,
                           year = year)