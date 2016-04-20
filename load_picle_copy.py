try:
    import cPickle as pickle
except:
    import pickle

import json

from parse_html import parse
from zaro_winkler import zaro_calculate

url = 'http://abuaminaelias.com/brotherhood-in-the-quran-and-sunnah/'

with open('output.pickle', 'rb') as data:
    word_dict = pickle.load(data)

with open('output.json','r') as json_data:
    dic_in = json.load(json_data)

def data_process(url):
    output_str = u""

    for value in parse(url):
        result_dict = {}
        words = value.split()

        for word in words:
            if word in word_dict:
                for val in word_dict[word]:
                    if val in result_dict:
                        result_dict[val] +=1
                    else:
                        result_dict[val] = 1
        best_matches = sorted(result_dict.items(),key=lambda x:x[1],reverse=True)[:3]
        output_str += "The arabic input is: <br/>"
        output_str += value + "<br/>"
        output_str += "The best matches in decreasing order:<br/>"
        for index,match in enumerate(best_matches):
            best = dic_in['sura'][best_matches[index][0][0]][u'aya'][best_matches[index][0][1]][u'text'].split()
            count = 0.0
            for input_word,compare_word in zip(words,best):
                if input_word == compare_word:
                    count += 1.0
                else:
                    count += zaro_calculate(input_word, compare_word)
            output_str += str(count/len(words)*100) + "<br/>"
        output_str += "----------------------------------><br/>"

        #print type(result_dict.items()[0])

    return output_str