#Author: Caroline Glazer
#Date: July 2016

from music21 import *
import os
import re
from colorama import Fore

for f in sorted(os.listdir('../sources/music/')):
    if f.endswith('.xml'):
        peggy = converter.parse('../sources/music/'+f)
        key = str(peggy.analyze('key'))
        print(f)

        peggy.metadata.alternativeTitle = input("title: ")
        peggy.metadata.localeOfComposition = input("location: ")
        peggy.metadata.number = key
        peggy.metadata.opusNumber = input("meter: ")
        peggy.metadata.date = input("year: ")        
        
        print(peggy.metadata.all())


#################################
'''
for i in peggy[2].measures(0,len(peggy[2])):
    print(i.offset)
    pitches = {}
    for thing in i.getElementsByClass('Note'):
        pitches[thing.pitch] = thing.offset
    for k,v in pitches.items():
        print(k,v)
'''


