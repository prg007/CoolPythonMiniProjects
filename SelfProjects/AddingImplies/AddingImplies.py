#Adds implies sign to the beginning of each line of text on the clipboard. 
#When this program is run it replaces the text on the clipboard with 
#text that has implies sign at the start of each line

import pyperclip 
text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = "=>" + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)