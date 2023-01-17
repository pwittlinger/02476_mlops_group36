# -*- coding: utf-8 -*-
"""
@author: paulw
"""

import pandas as pd
pd.set_option('display.max_colwidth',0)
import numpy as np
from numpy import hstack, asarray, vstack

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import random
from os import listdir
from collections import Counter
from tqdm import tqdm
from datetime import datetime

import string
import re
from string import punctuation
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt")
nltk.downloader.download("vader_lexicon")
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
lemmatizer = WordNetLemmatizer()
Stop_Words = stopwords


from wordcloud import WordCloud
import wordcloud



def show_wordcloud(data, column_n, title):
    '''Prints the wordcloud. Adapted from the function provided in the lecture.'''
    #println(data)
    text = ' '.join(data[column_n].astype(str).tolist())
    stopwords = set(wordcloud.STOPWORDS)
    
    fig_wordcloud = wordcloud.WordCloud(stopwords=stopwords,
        max_font_size=100, max_words=100, background_color="white").generate(text)
    
    plt.figure(figsize=(10,7), frameon=True)
    plt.imshow(fig_wordcloud, interpolation="bilinear")  
    plt.axis('off')
    plt.title(title, fontsize=20)
    plt.show()
    
    
def text_processing(text):
    # remove punctuation 
    text = "".join([c for c in text 
                    if c not in string.punctuation])
    # lowercase
    text = "".join([c.lower() for c in text])
    # remove stopwords
    text = " ".join([w for w in text.split() 
                     if w not in Stop_Words])
    # stemming / lematizing (optional)
    text = " ".join([lemmatizer.lemmatize(w) for w in text.split()])
    return text



def get_sentiment_intensity(data_):
    '''
    Parameters
    ----------
    data : TYPE
        DESCRIPTION.

    Returns
    -------
    sentiment : TYPE
        DESCRIPTION.

    '''
    sentiment = []
    for data in data_:

        
        score = SentimentIntensityAnalyzer().polarity_scores(data)
        neg = score["neg"]
        pos = score["pos"]
        if neg > pos:
            sentiment.append("negative")
        elif pos > neg:
            sentiment.append("positive")
        else: 
            sentiment.append("neutral")

    return sentiment