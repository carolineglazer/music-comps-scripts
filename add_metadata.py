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

        #add a metadata object to peggy score
        peggy.insert(0,metadata.Metadata())
        
        #add stuff to the metadata object
        peggy.metadata.number = f
        peggy.metadata.title = input("title: ")
        peggy.metadata.location = input("location: ")
        peggy.metadata.year = input("year: ")        
        peggy.metadata.orig_key = key
        peggy.metadata.meter = peggy.recurse().getElementsByClass(meter.TimeSignature)[0]
        
        #overwrite xml files with metadata-y version
        outfile = '../sources/music/'+f
        peggy.write(fmt='xml', fp=outfile)
        print(peggy.metadata.all())
        peggytest = converter.parse('../sources/music/'+f)
        print(peggytest.metadata.all())
