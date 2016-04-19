# -*- coding: UTF-8 -*-

import json
try:
    import cPickle as pickle
except:
    import pickle


with open('output.json','r') as json_data:
    dic_in = json.load(json_data)


print list(dic_in['sura'][2][u'aya'][102][u'text'].split()[11])


#input_str = "وَاعْتَصِمُوا بِحَبْلِ اللَّهِ جَمِيعًا وَلَا تَفَرَّقُوا وَاذْكُرُوا نِعْمَتَ اللَّهِ عَلَيْكُمْ إِذْ كُنتُمْ أَعْدَاءً فَأَلَّفَ بَيْنَ قُلُوبِكُمْ فَأَصْبَحْتُم بِنِعْمَتِهِ إِخْوَانًا وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍ مِّنَ النَّارِ فَأَنقَذَكُم مِّنْهَا كَذَٰلِكَ يُبَيِّنُ اللَّهُ لَكُمْ آيَاتِهِ لَعَلَّكُمْ تَهْتَدُونَ"
#input_str = unicode(input_str, encoding= "utf-8")
#print input_str.split()


#print lst
#u'\u0625\u0650\u0630\u0652'
#[u'\u0643', u'\u064f', u'\u0646', u'\u062a', u'\u064f', u'\u0645', u'\u0652']
#[u'\u0643', u'\u064f', u'\u0646', u'\u0652', u'\u062a', u'\u064f', u'\u0645', u'\u0652']