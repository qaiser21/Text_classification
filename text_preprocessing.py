
'''
helper function that is used for text preprocessing

'''

import nltk
import re
import string
from nltk.corpus import wordnet


def tokenize_text(text):
  '''
  function used for tokenizing string
  '''
  sentences = nltk.sent_tokenize(text)
  tokenize_word = [nltk.word_tokenize(sentence) for sentence in sentences]
  return tokenize_word
  
    
 
def remove_characters_after_tokenization(tokens):
  '''
  removing character after tokenization
  '''
  pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
  filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])
  return filtered_tokens
  


def remove_characters_before_tokenization(sentence,keep_apostrophes = False):
  '''
  removing character before tokenization
  '''
  sentence = sentence.strip()
  if keep_apostrophes:
    pattern = r'[?|$|&|*|%|@|(|)|~]'
    filtered_sentence = re.sub(pattern,r'',sentence)
  else:
    pattern = r'[^a-zA-Z0-9]'
    filtered_sentence = re.sub(pattern,r'', sentence)
  return filtered_sentence


def expand_contractions(sentence, contraction_mapping):
  '''
  '''
  contraction_pattern = re.compile('({})'.format('|'.join(concentration_mappping.keys())),flags = re.IGNORECASE|re.DOTALL)
  
  def expand_match(contraction):
    match = contraction.group(0)
    first_char = match[0]
    expanded_contraction = contraction_mapping.get(match)\
                           if contraction_mapping.get(match)\
                           else contraction_mapping.get(match.lower())
    expanded_contraction= first_char + expanded_contraction[1:]
    return expanded_contraction
  expanded_sentence = contractions_pattern.sub(expand_match, sentence)
  
  
def remove_stopwords(tokens):
  '''
  removing stop word after tokenization
  '''
  stopword_list  = nltk.corpus.stopwords.words('englis')
  filtered_tokens = [token for token in tokens if token not in stopword_list]
  return filtered_tokens


def remove_repeated_characters(tokens):
  '''
  function where repeated character in token get replaced
  '''
  repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
  match_substitution = r'\1\2\3'
  def replace(old_word):
    if wordnet.synsets(old_word):
      return old_word
    new_word = repeat_pattern.sub(match_substitution, old_word)
    return replace(new_word) if new_word !=old_word else new_word
  correct_tokens = [replace(word) for word in tokens]
  return correct_tokens


  

  
  
  
  
    
    
    
    
    
    
    
    
    
    
