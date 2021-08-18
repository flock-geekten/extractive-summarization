import re
import emoji
import requests
import unicodedata
import nltk
from nltk.corpus import wordnet
#from bs4 import BeautifulSoup

def data_cleaning(data):
    return [text_cleaning(text) for text in data]

def text_cleaning(text):
    text = clean_text(text)
    #text = clean_html_tags(text)
    #text = clean_html_and_js_tags(text)
    text = clean_url(text)
    text = normalize(text)
    return text

def clean_text(text):
    replaced_text = text.lower()
    replaced_text = re.sub(r'[【】]', ' ', replaced_text)       # 【】の除去
    replaced_text = re.sub(r'[（）()]', ' ', replaced_text)     # （）の除去
    replaced_text = re.sub(r'[［］\[\]]', ' ', replaced_text)   # ［］の除去
    replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
    replaced_text = re.sub(
        r'https?:\/\/.*?[\r\n ]', '', replaced_text)  # URLの除去
    replaced_text = re.sub(r'　', ' ', replaced_text)  # 全角空白の除去
    return replaced_text

"""
def clean_html_tags(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    cleaned_text = soup.get_text()
    cleaned_text = ''.join(cleaned_text.splitlines())
    return cleaned_text
"""

"""
def clean_html_and_js_tags(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    [x.extract() for x in soup.findAll(['script', 'style'])]
    cleaned_text = soup.get_text()
    cleaned_text = ''.join(cleaned_text.splitlines())
    return cleaned_text
"""

def clean_url(html_text):
    cleaned_text = re.sub(r'http\S+', '', html_text)
    cleaned_text = re.sub(r'https\S+', '', cleaned_text)
    return cleaned_text

def normalize(text):
    normalized_text = normalize_unicode(text)
    normalized_text = delete_symbol(text)
    normalized_text = normalize_number(normalized_text)
    normalized_text = lower_text(normalized_text)
    return normalized_text

def normalize_unicode(text, form='NFKC'):
    normalized_text = unicodedata.normalize(form, text)
    return normalized_text

def delete_symbol(text):
    code_regex = re.compile('[\t\s!"#$%&\'\\\\()*+,-./:;；：<=>?@[\\]^_`{|}~○｢｣「」〔〕“”〈〉'\
                            '『』【】＆＊（）＄＃＠？！｀＋￥¥％♪…◇→←↓↑｡･ω･｡ﾟ´∀｀ΣДｘ⑥◎©︎♡★☆▽※ゞノ〆εσ＞＜┌┘]')
    return code_regex.sub('', text)

def normalize_number(text):
    replaced_text = re.sub(r'\d+', '0', text)
    return replaced_text

def lower_text(text):
    return text.lower()