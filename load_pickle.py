try:
    import cPickle as pickle
except:
    import pickle

import json

from parse_html import parse

url = 'http://abuaminaelias.com/brotherhood-in-the-quran-and-sunnah/'

with open('output.pickle', 'rb') as data:
    word_dict = pickle.load(data)

with open('output.json','r') as json_data:
    dic_in = json.load(json_data)

with open("qt_output.txt","w") as file_handle:

    for value in parse(url):
        print "---------------------------->"
        result_dict = {}
        words = value.split()
        print len(words)

        for word in words:
            if word in word_dict:
                for val in word_dict[word]:
                    if val in result_dict:
                        result_dict[val] +=1
                    else:
                        result_dict[val] = 1
            #else:
            #    print index, list(word)
            #print result_dict
        best_matches = sorted(result_dict.items(),key=lambda x:x[1],reverse=True)[:3]
        print "The arabic input is: \n"
        print value
        print "The best matches in decreasing order:\n"
        for index,match in enumerate(best_matches):
            file_handle.write(dic_in['sura'][best_matches[index][0][0]][u'aya'][best_matches[index][0][1]][u'text'])

    #print type(result_dict.items()[0])

