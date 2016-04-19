try:
    import cPickle as pickle
except:
    import pickle

from parse_html import parse

url = 'http://abuaminaelias.com/brotherhood-in-the-quran-and-sunnah/'

with open('output.pickle', 'rb') as data:
    word_dict = pickle.load(data)




for index, value in enumerate(parse(url)):
    print "---------------------------->"
    result_dict = {}
    words = value.split()
    print len(words)

    for index, word in enumerate(words):
        if word in word_dict:
            for val in word_dict[word]:
                if val in result_dict:
                    result_dict[val] +=1
                else:
                    result_dict[val] = 1
        #else:
        #    print index, list(word)
        #print result_dict
    print sorted(result_dict.items(),key=lambda x:x[1],reverse=True)
    #print type(result_dict.items()[0])
