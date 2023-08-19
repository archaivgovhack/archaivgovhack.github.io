import pandas
import pkg_resources
from symspellpy import SymSpell, Verbosity
from bs4 import BeautifulSoup as bs
import os
import re
import nltk

def get_transcript_fname_by_id(ts_path, id_num):
    fname = os.path.join(ts_path, 'transcript-'+str(id_num)+'.xml')
    if os.path.exists(fname):
        return fname
    else:
        return None
    
    
def clean_xml(text):
    clean = re.sub('<[^<]+?>', '', text).replace("\n", " ")
    return clean


def find_in_soup(soup, term):
    text = str(soup.find(term)).replace('<![CDATA[', '').replace("\n", " ")
    text = re.sub('<[^<]+?>', '', text).replace("\n", " ")
    
    return text


sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt")
bigram_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_bigramdictionary_en_243_342.txt")
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)


def spellcheck(sentence):
    suggestions = sym_spell.lookup_compound(sentence, max_edit_distance=2)
    return suggestions[0].term

    
def parse_transcript(fname, sentence_len_thresh=50):
    '''
    fname: filename of transcript xml file
    sentence_len_thresh: minimum length of sentence to be produced
    '''
    with open(fname, 'rb') as xml_file:
        soup = bs(xml_file, features="html/parser")
    
        # Get PM
        pm = find_in_soup(soup, 'prime-minister')
        
        # Get Date
        date = find_in_soup(soup, 'release-date')
        
        # Get Release
        release_type = find_in_soup(soup, 'release-type')
        
        # Get content
        content = find_in_soup(soup, 'content')
        
        # Get sentences
        sentences = nltk.tokenize.sent_tokenize(content)
        sentences = [spellcheck(x) for x in sentences if len(x)>sentence_len_thresh]
    
    return {'pm': pm,
            'date': date,
            'content': content,
            'sentences': sentences}
    
