import os

def get_texts_statistics(datafile_path):
    source_file = open(datafile_path, 'r')
    source_text = source_file.read()

    letters_in_text = sorted([
        symbol.lower()
        for symbol in source_text
        if symbol.isalpha()
    ])




path_to_datafile = os.path.abspath('text.txt')
texts_statistics = get_texts_statistics(path_to_datafile)
