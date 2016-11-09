import json
try:
    import cPickle as pickle
except:
    import pickle


with open('output.json','r') as json_data:
    dic_in = json.load(json_data)


#for i in dic_in['sura'][113][u'aya']:
#    print i[u'text']


print dic_in['sura'][113][u'aya'][0][u'text']


print len(dic_in['sura'][113][u'aya'])


inverse_dict = {}

for sura_number in xrange(114):
    for aya_number in xrange(len(dic_in['sura'][sura_number][u'aya'])):
        for position, word in  enumerate(dic_in['sura'][sura_number][u'aya'][aya_number][u'text'].split()):
            inverse_dict.setdefault(word,set()).add((sura_number,aya_number))


with open('output.pickle','wb') as f:
    pickle.dump(inverse_dict,f)

