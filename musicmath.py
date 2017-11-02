#12 notes
#major wwhwwwh
#minor whwwhww
#harmonic minor whwwh wh h
import random

notedic = {0:'c',1:'c#',2:'d',3:'d#',4:'e',
           5:'f',6:'f#',7:'g',8:'g#',9:'a',
           10:'a#',11:'b',' ':' '}

numdic = {'c':0,'c#':1,'d':2,'d#':3,'e':4,
           'f':5,'f#':6,'g':7,'g#':8,'a':9,
           'a#':10,'b':11}
majoroffset = [0,2,4,5,7,9,11]
minoroffset = [0,2,3,5,7,8,10]
harmonicminoroffset = [0,2,3,5,7,8,11]
currentlyplaying = []
notelist = []
spacing = []

key = input('Enter your key :: ').lower()
numkey = numdic[key]
tone = input('Major or Minor or Harmonic Minor :: ').lower()
lines = int(input('Enter your number of lines :: '))
length = int(input('Enter your length :: '))
for i in range(lines):
    spacing.append(int(input('Enter your spacing for line '+str(i)+' :: ')))
    notelist.append([])

choices = []
if(tone == 'major'):
    for offset in majoroffset:
        choices.append((numkey+offset) % 12)
if(tone == 'minor'):
    for offset in minoroffset:
        choices.append((numkey+offset) % 12)
if(tone == 'harmonic minor'):
    for offset in harmonicminoroffset:
        choices.append((numkey+offset) % 12)

for i in range(lines):
    currentlyplaying.append(None)

def testnote(notelistx,note):
    for n in notelistx:
        if(n == None):
            continue
        if(note-n >= 9 or n-note >= 9 or n-note == 1 or n-note == 2 or note-n == 1 or note-n == 2):
            return False
    return True

for i in range(length):
    for j in range(lines):
        if(i == 0 or i % spacing[j] == 0):
            currentlyplaying[j] = None
    for j in range(lines):
        if(i == 0 or i % spacing[j] == 0):
            while(True):
                trynote = random.choice(choices)
                if(testnote(currentlyplaying,trynote)):
                    notelist[j].append(trynote)
                    currentlyplaying[j] = trynote
                    break
        else:
            notelist[j].append(' ')

for i in range(length):
    for j in range(lines):
        print(notedic[notelist[j][i]]+' ',end='')
    print()
