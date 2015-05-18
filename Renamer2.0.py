__author__ = 'Karsten'

import os
import mutagen
from mutagen.id3 import ID3
import re

path = 'E:\Musik\Alestorm'

for (path, dirs, files) in os.walk(path, topdown=False):

    for filename in os.listdir(path):
        if filename.endswith('.mp3'):
           # pathToFile = path + '\\' + filename
            audio = ID3(os.path.join(path, filename))
            artist = audio['TPE1']
            artistString = str(artist)
            title = audio['TIT2']
            titleString = str(title)

            table = {
                ord('\\'): None,
                ord('/'): None,
                ord('*'): None,
                ord(':'): None,
                ord('?'): None,
                ord('\"'): None,
                ord('<'): None,
                ord('>'): None,
                ord('|'): None,
            }
            artistString = artistString.translate(table)
            titleString = titleString.translate(table)

            newFileName = titleString + " - " + artistString + '.mp3'

            oldName = os.path.join(path, filename)
            newName = os.path.join(path, newFileName)
            newName = ' '.join(newName.split())

            os.rename(oldName, newName)