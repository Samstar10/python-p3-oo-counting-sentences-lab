#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        sentences = [sentence for sentence in filter(None, re.split(r'[.!?]', self.value))]
        return len(sentences)
