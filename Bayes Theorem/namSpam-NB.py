import pandas as pd
import numpy as np
import string
import tensorflow as tf
from tf.keras import models

# =============================================================================
# def remove_pun(string):
#     punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     for i in range (0,len(string)):
#         for chhar in punc:
#             string[i]=string[i].replace(chhar,'')
#     return string
# 
# =============================================================================

with open("data/SMSSpamCollection.txt", 'r') as data:
    read_file = data.read()
    temp_data = {}
    for line in data:
        line = line.translate(str.maketrans('', '', string.punctuation))
        word = line.split()
        if not line:
            continue
        if word[0] in list(temp_data.keys()):
            temp_data[word[0]] += word[1:]
        else:
            temp_data[word[0]] = word[1:]



# =============================================================================
# temp_data['ham']=remove_pun(list(temp_data['ham']))
# temp_data['spam']=remove_pun(list(temp_data['spam']))
# =============================================================================

vocab_df = pd.DataFrame({key:pd.Series(value) for key, value in temp_data.items()})
vocab_df
freq_ham = vocab_df['ham'].value_counts().rename_axis('ham_word').to_frame('counts')
freq_spam = vocab_df['spam'].value_counts().rename_axis('spam_word').to_frame('counts')
prob_ham  = len(list(temp_data['ham']))/(len(list(temp_data['ham']))+len(list(temp_data['spam'])))
prob_spam  = len(list(temp_data['spam']))/(len(list(temp_data['spam']))+len(list(temp_data['ham'])))

total_spam_rep_words_rep_words = 0
total_ham_rep_words_rep_words = 0

for count in freq_spam.loc[:,'counts']:
    total_spam_rep_words_rep_words += count
    
for count in freq_ham.loc[:,'counts']:
    total_ham_rep_words_rep_words += count
    


test = input(">> ")
           
test = test.translate(str.maketrans('', '', string.punctuation))
line_word = test.split()

prob_freq_wrd_sp = 1
prob_freq_wrd_ham = 1
for word in line_word:
    if word.lower() in freq_spam.loc['spam_word'].lower():
        prob_freq_wrd_sp *= freq_spam.loc[word]/total_spam_rep_words_rep_words
    else:
        continue
for word in line_word:
    if word.lower() in freq_ham.loc['ham_word'].lower():
        prob_freq_wrd_ham *= freq_ham.loc[word]/total_ham_rep_words_rep_words
    else:
        continue      

p_spam_message = prob_spam*prob_freq_wrd_sp/(prob_spam*prob_freq_wrd_sp+prob_ham*prob_freq_wrd_ham)
p_ham_message = prob_ham*prob_freq_wrd_ham/(prob_spam*prob_freq_wrd_sp+prob_ham*prob_freq_wrd_ham)
print(f"Ham: {p_ham_message} \n Spam: {p_ham_message}\n")
if p_spam_message > p_ham_message:
    print("It is a SPAM")
else:
    print("It is a ham")

