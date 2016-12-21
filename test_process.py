try:
    import cPickle as pickle
except:
    import pickle

from parse_html import parse
from zaro_winkler import zaro_calculate
import json

url = 'http://abuaminaelias.com/brotherhood-in-the-quran-and-sunnah/'

with open('output.pickle', 'rb') as data:
    word_dict = pickle.load(data)

with open('output.json','r') as json_data:
    dic_in = json.load(json_data)


matchCases = {}

for value in parse(url):
    #print "---------------------------->"
    result_dict = {}
    words = value.split()
    #print len(words)

    for word in words:
        if word in word_dict:
            for val in word_dict[word]:
                if val in result_dict:
                    result_dict[val] +=1
                else:
                    result_dict[val] = 1

    #matchCases[value] = sorted(result_dict.items(),key=lambda x:x[1],reverse=True)[:3]
    best_results = sorted(result_dict.items(),key=lambda x:x[1],reverse=True)[:3]
    #print best_results
    #print "--------------------------->"
    for best_result in enumerate(best_results):
        for index in range(3):
            best = dic_in['sura'][best_results[index][0][0]][u'aya'][best_results[index][0][1]][u'text'].split()
            count = 0.0
            for input_word,compare_word in zip(words,best):
                if input_word == compare_word:
                    count += 1.0
                else:
                    count += zaro_calculate(input_word, compare_word)
            print count/len(words)*100
    print "---------------------------------->"
