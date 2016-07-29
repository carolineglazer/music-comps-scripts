import os

#This is an unwanted but committed change

for i in os.listdir('../sources/lyrics'):
    variant = '../sources/lyrics/' + i
    f = open(variant, 'r')
    verses = -1
    print 'start: ', verses

    for line in f:
        if line == '\n':
            verses += 1
            print variant, 'verse'

    print variant, ": ", verses
    f.close()
    print 'end: ', verses
