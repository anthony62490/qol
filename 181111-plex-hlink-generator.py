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
    dest = raw_input("Enter a full destination Filepath:") or "F:\Plex\Shows\Lost\Lost - Season 02"
    source = raw_input("Enter a full source Filepath:") or "F:\Video\to-be-linked"
    tempBlob = "1\tMan of Science, Man of Faith\t09/21/2005\t\n2\tAdrift\t09/28/2005\t"
    print("Paste a theTVDB text blob. Press Ctrl+D on a new line to confirm:")
    blob = []
    while True:
        try:
            line = raw_input("")
        except EOFError:
            break
        blob = splitByNewLine(blob, line)
    print "dest: " + dest
    print "source: " + source
    print "blob: "
    for x in blob:
        print x
    #print "tempblob: " + tempBlob
main()

"""1	Man of Science, Man of Faith	09/21/2005	
2	Adrift	09/28/2005	
3	Orientation	10/05/2005	
4	Everybody Hates Hugo	10/12/2005	
5	...And Found	10/19/2005	
6	Abandoned	11/09/2005	
7	The Other 48 Days	11/16/2005	
8	Collision (a.k.a. Old Habits)	11/23/2005	
9	What Kate Did	11/30/2005	
10	The 23rd Psalm	01/11/2006	
11	The Hunting Party	01/18/2006	
12	Fire + Water	01/25/2006	
13	The Long Con	02/08/2006	
14	One of Them	02/15/2006	
15	Maternity Leave	03/01/2006	
16	The Whole Truth	03/22/2006	
17	Lockdown	03/29/2006	
18	Dave	04/05/2006	
19	S.O.S.	04/12/2006	
20	Two for the Road	05/03/2006	
21	?	05/10/2006	
22	Three Minutes	05/17/2006	
23	Live Together, Die Alone (1)	05/24/2006	
24	Live Together, Die Alone (2)	05/24/2006"""
