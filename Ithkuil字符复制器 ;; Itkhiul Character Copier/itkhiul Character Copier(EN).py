#ithkuil Character Copier
from tkinter import Tk
root = Tk()
root.withdraw()

while True:
    tybe = ""
    print("The current character sets are as follows:")
    print("pʰ:1   p':2   tʰ:3   t':4   ţ:5   ż:6   cʰ:7   c':8   č:9   čʰ:10")
    print("č':11  š:12   ž:13   ç:14   kʰ:15 k':16 ň:17   qʰ:18  q':19 ř:20")
    print("':21   ļ:22   d͕:23   ẓ:24")
    print("â:31   ê:32   î:33   ô:34   û:35")
    print("ä:41   ë:42   ʰ:43   ö:44   ü:45")
    tybe = input("Please enter the number corresponding to the character you want; for example, \" p\' \" is 2.\n")
    cipher = {
        '1': "pʰ",
        '2': "p'",
        '3': "tʰ",
        '4': "t'",
        '5': "ţ",
        '6': "ż",
        '7': "cʰ",
        '8': "c'",
        '9': "č",
        '10': "čʰ",
        '11': "č'",
        '12': "š",
        '13': "ž",
        '14': "ç",
        '15': "kʰ",
        '16': "k'",
        '17': "ň",
        '18': "qʰ",
        '19': "q'",
        '20': "ř",
        '21': "'",
        '22': "ļ",
        '23': "d͕",
        '24': "ẓ",
        '31': "â",
        '32': "ê",
        '33': "î",
        '34': "ô",
        '35': "û",
        '41': "ä",
        '42': "ë",
        '43':"ʰ",
        '44': "ö",
        '45': "ü"
    }
    try:
        root.clipboard_clear()
        root.clipboard_append(cipher[tybe])
        root.update
        print("Copying successful✅")
    except:
        print("Copy error ❌ The number may not exist or the value entered is not an integer.")
    finally:
        print("To start again, press 1; to exit, press 2")
        aaa = input()
        if aaa == "1":
            continue
        else:
            break