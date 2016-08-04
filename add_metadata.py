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
        peggy.metadata.date = input("year: ")        
        
        print(peggy.metadata.all())

        #overwrite xml files with metadata-y version
        outfile = '../sources/music/'+f
        peggy.write(fmt='xml', fp=outfile)
