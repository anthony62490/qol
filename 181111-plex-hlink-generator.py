# Anthony Magno - 2018/11/11
# Provided a destination, a source, and a block of text from theTVDB, should
# output a simple list of cmd commands to create HLinks for Plex
###############################################################################
import re

def splitByNewLine(array, userInput):
    #The user's input is treated slightly different when each line is entered by hand
    #or pasted as a block of text. To remedy this, the all user input as it is received,
    #split it by newlines, and append each of them to the supplied array
    split = userInput.split('\n')
    for x in split:
        array.append(x)
    return array

def main():
    dest = input("Enter a full destination Filepath:") or "F:\\Plex\\Shows\\Show"
    source = input("Enter a full source Filepath:") or "F:\\Video\\to-be-linked"
    tempBlob = "1\tEpisode1\t01/01/2001\t\n2\tEpisode2\t01/02/2001\t"
    print("Paste a theTVDB text blob. Press Ctrl+D on a new line to confirm:")
    blob = []
    while True:
        try:
            line = input("")
        except EOFError:
            break
        blob = splitByNewLine(blob, line)
    print("dest: " + dest)
    print("source: " + source)
    print("blob: ", blob)
    for x in blob:
        print("blob index", blob.index(x), "-", x)
    #print("tempblob: " + tempBlob)
main()

"""1	Episode1	01/01/2001	
2	Episode2	01/02/2001	
3	Episode3	01/03/2001	
4	Episode4	01/04/2001	
5	Episode5	01/05/2001	"""
