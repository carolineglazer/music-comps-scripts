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
        peggy.insert(0,metadata.Metadata())
        
        #add stuff to the metadata object
        peggy.metadata.localeOfComposition = input("location: ")
        peggy.metadata.date = input("year: ")        
        peggy.metadata.number = key
        
        #overwrite xml files with metadata-y version
        outfile = '../sources/music/'+f
        peggy.write(fmt='xml', fp=outfile)
        print(peggy.metadata.all())
        peggytest = converter.parse('../sources/music/'+f)
        print(peggytest.metadata.all())
