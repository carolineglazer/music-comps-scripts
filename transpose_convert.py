#Author: Caroline Glazer
#Date: July 2016

from music21 import *
import os
import re
from colorama import Fore

for f in sorted(os.listdir('../sources/music/')):
    if f.endswith('.xml'):
        peggy = converter.parse('../sources/music/'+f)
        #print(peggy.metadata.title)
        key = str(peggy.analyze('key'))
        print(f)

        #convert all major to F major and all minor to f minor
        if key == 'F major':
            print('yay already in F!')
            peggy2 = peggy
        elif key == 'a minor':
            peggy2 = peggy.transpose(-4)
            print(key, '==>', peggy2.analyze('key'))
        elif key == 'G major':
            peggy2 = peggy.transpose(-2)
            print(key, '==>', peggy2.analyze('key'))
        elif key == 'C major':
            peggy2 = peggy.transpose(-7)
            print(key, '==>',peggy2.analyze('key'))
        elif key == 'e minor':
            peggy2 = peggy.transpose(1)
            print(key, '==>', peggy2.analyze('key'))
        elif key == 'A major':
            peggy2 = peggy.transpose(-4)
            print(key, '==>', peggy2.analyze('key'))
        else:
            print(Fore.RED + "OH NO!:", f, key)
            
        #write a new xml file with the same name to .../music/xml_same_key
        outfile = '../sources/music/xml_same_key/'+re.search('.*(?=.xml)', f).group()+'.xml'
        peggy2.write(fmt='xml', fp=outfile)



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


