#Author: Caroline Glazer
#Date: August 2016

from music21 import *
import os
from copy import deepcopy

for f in sorted(os.listdir('../sources/music/xml_same_key/')):
    if f.endswith('.xml'):
        peggy = converter.parse('../sources/music/xml_same_key/'+f)
        key = str(peggy.analyze('key'))
        print(f)
        peggy2 = deepcopy(peggy)
        
        #add stuff to the metadata object
#        peggy2.metadata.composer = input("location: ")        
#        peggy2.metadata.movementNumber = input("year: ")
        peggy2.metadata.title = input("title: ")

        #overwrite xml files with metadata-y version
        outfile = '../sources/music/xml_same_key/'+f
        print(outfile)
        peggy2.write(fmt='xml', fp=outfile)
        print(peggy2.metadata.all())
        peggytest = converter.parse(outfile)
        print(peggytest.metadata.all())
