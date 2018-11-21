# Anthony Magno - 2018/11/11
# Provided a destination, a source, and a block of text from theTVDB, should
# output a simple list of cmd commands to create HLinks for Plex
###############################################################################
import re

def splitByNewLine(array, userInput):
    #The user's input is treated slightly different when each line is entered by hand
    #or pasted as a block of text. To remedy this, the all user input as it is received,
    #split it by newlines, and append each of them to the supplied array
    chunks = userInput.split('\t')
    if chunks[-1] == '':
        chunks.pop()
    array.append(chunks)
    return array

def printAll(source, destination, data):
    print("dest    : " + destination)
    print("source  : " + source)
    for x in data:
        print("index", data.index(x), ":", x)

def main():
    dest = input("Enter a full destination Filepath:") or "F:\\Plex\\Shows\\Show"
    source = input("Enter a full source Filepath:") or "F:\\Video\\to-be-linked"
    print("Paste a theTVDB text blob. Enter a blank line to confirm:")
    blob = []
    while True:
        try:
            line = input("")
            if not line:
                raise EOFError
        except EOFError:
            break
        # TODO: Validate input
        blob = splitByNewLine(blob, line)
    # At this point, the blob contains an array of arrays. Each array should contain the episode number, the title, and the release date
    for i in blob:
        # Take the date, split it by the delimiter, arrange them in YYYYMMDD format, and put the result back into the blob
        dateElements = i[2].split('/')
        year = dateElements.pop()
        dateElements.insert(0, year)
        dateBlock = ''.join(dateElements)
        # Now everything is formatted correctly. Create a template using the gathered information
        print(dateBlock, "-", i[0], i[1])
    printAll(source, dest, blob)
       
        

main()

"""1	Episode1	01/01/2001	
2	Episode2	01/02/2001	
3	Episode3	01/03/2001	
4	Episode4	01/04/2001	
5	Episode5	01/05/2001	"""
