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
    output_str = u"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    table {
                width:100%;
                }
    
    th, td {
                padding: 5px;
                    text-align: left;
                    }
    table tr:nth-child(even) {
                background-color: #eee;
                }
    table tr:nth-child(odd) {
               background-color:#fff;
               }
    table th {
                background-color: black;
                    color: white;
                    }
    </style>
    </head>
    <body>
    """
    
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
        output_str += "<table style=\"width:100%\"><tr><th>Sura</th><th>Aya</th><th>Match(%)</th></tr>"
        for index,match in enumerate(best_matches):
            output_str += u"<tr><td>{}</td><td>{}</td>".format(dic_in[u'sura'][best_matches[index][0][0]][u'name'], best_matches[index][0][1]+1) 
            best = dic_in['sura'][best_matches[index][0][0]][u'aya'][best_matches[index][0][1]][u'text'].split()
            count = 0.0
            for input_word,compare_word in zip(words,best):
                if input_word == compare_word:
                    count += 1.0
                else:
                    count += zaro_calculate(input_word, compare_word)
            output_str += "<td>{}</td></tr>".format(count/len(words)*100)
        output_str += "</table>"
        
    output_str += "</body></html>"

        #print type(result_dict.items()[0])
    return output_str
