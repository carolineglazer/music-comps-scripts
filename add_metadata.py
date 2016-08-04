#Author: Caroline Glazer
#Date: July-August 2016

from music21 import *
import os
import re
from colorama import Fore

for f in sorted(os.listdir('../sources/music/')):
    if f.endswith('.xml'):
        peggy = converter.parse('../sources/music/'+f)
        key = str(peggy.analyze('key'))
        print(f)

        #add a metadata object to peggy score
        #peggy.insert(0,metadata.Metadata())
        
        #add stuff to the metadata object
        peggy.show('text')
        peggy.metadata.localeOfComposition = input("location: ")
        peggy.metadata.date = input("year: ")        
        peggy.metadata.number = key
        
        #overwrite xml files with metadata-y version
        outfile = '../sources/music/'+f
        peggy2 = peggy
        print(peggy2.metadata.all())
        peggy2.write(fmt='xml', fp=outfile)
        peggytest = converter.parse('../sources/music/'+f)
        print(peggytest.metadata.all())
        print(peggytest.metadata.localeOfComposition)
        print(peggytest.metadata.date)
        print(peggytest.metadata.number)
