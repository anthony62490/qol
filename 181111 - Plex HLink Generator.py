# Anthony Magno - 2018/11/11
# Provided a destination, a source, and a block of text from theTVDB, should
# output a simple list of cmd commands to create HLinks for Plex
###############################################################################
import os

def splitByNewLine(array, userInput):
    #The user's input is treated slightly different when each line is entered by hand
    #or pasted as a block of text. To remedy this, the all user input as it is received,
    #split it by newlines, and append each of them to the supplied array
    split = userInput.split('\n')
    print split
    return array

def main():
    dest = raw_input("Enter a full destination Filepath:") or "F:\Plex\Shows\Digimon\Digimon - Season 05"
    source = raw_input("Enter a full source Filepath:") or "F:\Seeds\Digimon All Seasons + Movies\Season 5 - Digimon Data Squad"
    tempBlob = "1\tThere Are Monsters Among Us\t04/02/2006\t\n2\tMarcus' Inner Strength\t04/09/2006\t"
    print("Paste a theTVDB text blob. Press Ctrl+D on a new line to confirm:")
    blob = []
    while True:
        try:
            line = raw_input("")
        except EOFError:
            break
        blob = (line)
    print "dest: " + dest
    print "source: " + source
    print "blob: "
    print blob
    ##print "tempblob: " + tempBlob
main()

"""1	There Are Monsters Among Us	04/02/2006	
2	Marcus' Inner Strength	04/09/2006	
3	The Return of Thomas!	04/16/2006	
4	The New Team of Marcus and Thomas!	04/23/2006	
5	Digital World, Here We Come!	04/30/2006	
6	The Ultimate Team No More?	05/07/2006	
7	A Birthday Kristy Will Never Forget!	05/14/2006	
8	The Singer's Secret	05/21/2006	
9	Never Meet Your Heroes	05/28/2006	
10	Curse This Curse (Marcus's Bad Day)	06/04/2006	
11	The Vile of Vilemon!	06/18/2006	
12	The Digi-egg That Fell to Earth	06/25/2006	
13	The Rise of RiseGreymon	07/02/2006	
14	The Wild Boy of the Digital World	07/09/2006	
15	The Gorge of Deception!	07/23/2006	
16	Falcomon - Friend or Foe?	07/30/2006	
17	The Singing Voice that Calls Upon a Miracle - The Lilamon Evolution	08/06/2006	
18	The DATS Team Annihilated?! Clash, Mercurimon	08/13/2006	
19	The Target is Ikuto!? Gotsumon's Plot	08/20/2006	
20	Rescue Mother, Ikuto - Hagurumon's Cage	08/27/2006	
21	Big Panic in the Human World - The Digimon Army Advances	09/03/2006	
22	Defeat the Ultimate Level! The Anger Wave of Saber Leomon	09/10/2006	
23	Once More, To the Digital World - Insekimon's Great Rampage	09/17/2006	
24	The Revealed Past - Heartless! Gizmon: AT	09/24/2006	
25	Smash Kurata's Ambition - Flight, Yatagaramon	10/01/2006	
26	Masaru's Memory is Erased - The Lost Bond	10/08/2006	
27	Chase Kurata - The Operation of Digimon Extermination Begins!	10/15/2006	
28	Evolution is Impossible! The Digivices Break Down	10/22/2006	
29	Resurrecting Digivices - A New Brilliance	10/29/2006	
30	An Imprisoned Masaru - The Holy City's Trap	11/05/2006	
31	Genius Showdown! Tohma vs. Nanami	11/12/2006	
32	Fiercely Attack Kurata's Army Corps - Protect the Holy Capitol	11/19/2006	
33	The Final Decisive Battle! Kouki, Ultimate Evolution	11/26/2006	
34	The Day of Parting - The Strongest Enemy: Tohma!	12/03/2006	
35	The Power of Destruction - ShineGreymon Runs Wild	12/10/2006	
36	Demon Lord Belphemon Revives	12/17/2006	
37	Awake, Agumon - Defeat Belphemon!	12/24/2006	
38	Burst Mode - The Power that Exceeds Ultimate	01/07/2007	
39	Human World Terminated! Yggdrasil's Decision	01/14/2007	
40	The Strongest Order of Knights - The Royal Knights Gather	01/21/2007	
41	Confirm it with a Fist! Thoughts of My Father	01/28/2007	
42	The Burst Mode of Tohma's Determination	02/04/2007	
43	Indeed Strength is Justice! Beast Knight Duftmon	02/11/2007	
44	Break! Craniummon's Strongest Shield	02/25/2007	
45	The One-on-One Match Between Men! Masaru vs. Suguru	03/04/2007	
46	Impact! The Truth About Bantyo Leomon	03/11/2007	
47	Protect the Future! DATS' Final Battle	03/18/2007	
48	A Complete Conclusion! Farewell, the Leader of Fights	03/25/2007"""
