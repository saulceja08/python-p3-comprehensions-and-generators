#!/usr/bin/env python3

def return_evens(num_list):
    list_of_even = [n for n in num_list if n % 2 == 0]
    return list_of_even
    
def make_exclamation(sentence_list):
    exclaimed_sentences = [sentence + "!" for sentence in sentence_list]
    return exclaimed_sentences

