"""
@author : Hyunwoong
@when : 2019-10-29
@homepage : https://github.com/gusdnd852
"""
# import spacy
from underthesea import word_tokenize
from laonlp.tokenize import word_tokenize as lo_tokenize
import spacy

class Tokenizer:
    def __init__(self):
        self.spacy_en = spacy.load('en_core_web_sm')
    
    def tokenize_vi(self,text):
        return [tok if " " not in tok else tok.replace(" ", "_") for tok in word_tokenize(text)]
    
    def tokenize_lo(self, text):
        return lo_tokenize(text)
    
    def tokenize_en(self, text):
        return [tok.text for tok in self.spacy_en.tokenizer(text)]
