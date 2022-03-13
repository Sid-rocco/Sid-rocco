# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 11:50:58 2022

@author: siddh
"""

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import words

vocabulary = {}
with open("data/SMSSpamCollection.txt", 'r') as data:
    nltk.download('words')
    set_word = set(words.words())
    
    
def build_vocabulary(curr_message):
    idx = len(vocabulary)
    for word in curr_message:
        if word.lower() not in vocabulary and word.lower() in set_word:
            vocabulary[word] = idx
            idx+=1
            
            
if __name__== '__main__':
    for i in range(data.shape[0]):
        curr_message = data.iloc[i,0].split()
        print(f'current message is {i}/ {data.shape[0]} and the length of vocabulary is {len(vocabulary)}')
        build_vocabulary(curr_message)
    file = open("vocabulary.txt", "w")
    file.write(str(vocabulary))
    file.close()