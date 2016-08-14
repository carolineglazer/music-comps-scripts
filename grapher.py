#Author: Caroline Glazer
#Date: July 2016

from music21 import *
import networkx as nx
import matplotlib.pyplot as plt
import os
import re

for f in sorted(os.listdir('../sources/music/xml_same_key')):
    if f.endswith('.xml'):
        
        #hierarchical peggy
        peggy = converter.parse('../sources/music/'+f)
        has_pickup = False
        measures = len(peggy.parts[0].getElementsByClass('Measure'))
        print(f)
        print("measures: ", measures)
        if peggy.parts[0].measure(0):
            has_pickup = True
        print("has_pickup: ", has_pickup)

        #flat peggy
        peggy = peggy.flat
        notes = []
        offsets = []
        key_signatures = []
        time_signatures = []
        for k in peggy.getElementsByClass('KeySignature'):
            key_signatures.append(k)
            print(k)
        for t in peggy.getElementsByClass('TimeSignature'):
            time_signatures.append(t)
            print(t)
        for e in peggy.notes:
            notes.append(e.nameWithOctave)
            offsets.append(e.offset)
        print()
            
        
