#!/bin/python3
from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return ""+f.read()

def main():
    try:
        path = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(path)
    counts = character_counts(text)
    print(f"{count_words(text)} words found in the document")
#    print(counts)
    pretty_print(path,text)
#    print(sort_dict(get_book_text(path)))

main()
