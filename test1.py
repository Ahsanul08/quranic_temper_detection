import json

with open('output.json','r') as json_data:
        dic_in = json.load(json_data)

print dic_in[u'sura'][48][u'name'] 
