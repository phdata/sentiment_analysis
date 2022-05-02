import re

import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# count number of characters 
def count_chars(text):
    return len(text)

# count number of words 
def count_words(text):
    return len(text.split())

# count number of capital characters
def count_capital_chars(text):
    count=0
    for i in text:
        if i.isupper():
            count+=1
    return count

# count number of capital words
def count_capital_words(text):
    return sum(map(str.isupper,text.split()))

# count number of punctuations
def count_punctuations(text):
    punctuations='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    d=dict()
    for i in punctuations:
        d[str(i)+' count']=text.count(i)
    return d

# count number of words in quotes
def count_words_in_quotes(text):
    x = re.findall("\'.\'|\".\"", text)
    count=0
    if x is None:
        return 0
    else:
        for i in x:
            t=i[1:-1]
            count+=count_words(t)
        return count
    
# count number of sentences
def count_sent(text):
    return len(nltk.sent_tokenize(text))

# calculate average word length
def avg_word_len(char_cnt,word_cnt):
    return char_cnt/word_cnt

# calculate average sentence length
def avg_sent_len(word_cnt,sent_cnt):
    return word_cnt/sent_cnt

# count number of unique words 
def count_unique_words(text):
    return len(set(text.split()))
            
# words vs unique feature
def words_vs_unique(words,unique):
    return unique/words
    
# count of hashtags
def count_htags(text):
    x = re.findall(r'(\#\w[A-Za-z0-9]*)', text)
    return len(x)

# count of mentions
def count_mentions(text):
    x = re.findall(r'(\@\w[A-Za-z0-9]*)', text)
    return len(x)

# count of stopwords
def count_stopwords(text):
    stop_words = set(stopwords.words('english'))  
    word_tokens = word_tokenize(text)
    stopwords_x = [w for w in word_tokens if w in stop_words]
    return len(stopwords_x)

# stopwords vs words
def stopwords_vs_words(stopwords_cnt,text):
    return stopwords_cnt/len(word_tokenize(text))