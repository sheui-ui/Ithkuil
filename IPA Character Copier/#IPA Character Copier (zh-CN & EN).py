#IPA Character Copier (zh-CN & EN)
import sys
import os
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
from tkinter import Tk
root = Tk()
root.withdraw()

texts_zh = [
    "请输入要写入的字符类型，辅音扣1，元音扣2，音调扣3，变音符扣4",
    "选择肺部气流辅音扣1，非肺部气流辅音（如挤喉音，内爆音等）扣2，其他辅音（如/w/，/ɕ/等）扣3",
    "字符集如下：",
    "请输入你想要选择的符号对应的序号",
    "添加成功，目前字符串为",
    "添加失败，可能是因为没有对应的符号或输入的不是整数",
    "是否继续添加字符，继续添加扣1，复制字符扣2，若要删除前面的一个字符扣3",
    "复制成功，是否重新开始，重新开始扣1，退出程序扣2",
    "复制失败，是否重新开始，重新开始扣1，退出程序扣2",
    "删除成功，目前字符串为",
    "删除失败"
]
texts_EN = [
    'Please enter the character type to be written: deduct 1 for consonants, 2 for vowels, 3 for tones, and 4 for diacritics',
    'Select 1 for pulmonic consonants, 2 for non-pulmonic consonants (such as ejectives, voiced implosives, etc.), and 3 for other consonants (such as /w/, /ɕ/, etc.)',
    'The character set is as follows:',
    'Please enter the serial number corresponding to the symbol you wish to select',
    'Added successfully. The current string is ',
    'Addition failed. This may be because there is no corresponding symbol or the input was not an integer',
    'Do you wish to continue adding characters? Continue adding: deduct 1; copy character: deduct 2; to delete the previous character: deduct 3',
    'Copying successful. Do you wish to start again? Start again: deduct 1; exit the programme: deduct 2',
    'Copying failed. Do you wish to start again? Start again: deduct 1; exit the programme: deduct 2',
    'Deletion successful, The current string is ',
    "Deletion failed"
]

#字符集
PULCONS = """
+----------------------------------------------------------------------------------------------------------------------------------------------+
|p: 0   b: 1 |            |             t: 2   d: 3              |ʈ: 4   ɖ: 5 |c: 6   ɟ: 7 |k: 8   g: 9 |q: 10  ɢ: 11|            |ʔ: 12       |
|       m: 13|       ɱ: 14|                    n: 15             |       ɳ: 16|       ɲ: 17|       ŋ: 18|       ɴ: 19|            |            |
|       ʙ: 20|            |                    r: 21             |            |            |            |       ʀ: 22|            |            |
|            |       ⱱ: 23|                    ɾ: 24             |       ɽ: 25|            |            |            |            |            |
|ɸ: 26  β: 27|f: 28  v: 29|θ: 30  ð: 31|s: 32  z: 33|ʃ: 34  ʒ: 35|ʂ: 36  ʐ: 37|ç: 38  ʝ: 39|x: 40  ɣ: 41|χ: 42  ʁ: 43|ħ: 44  ʕ: 45|h: 46  ɦ: 47|
|            |            |             ɬ: 48  ɮ: 49             |            |            |            |            |            |            |
|            |       ʋ: 50|                    ɹ: 51             |       ɻ: 52|       j: 53|       ɰ: 54|            |            |            |
|            |            |                    l: 55             |       ɭ: 56|       ʎ: 57|       ʟ: 58|            |            |            |
+----------------------------------------------------------------------------------------------------------------------------------------------+
"""
UPLCONS = """
+---------------------------------------------------------------+
|      Clicks       | ʘ: 0  | ǀ: 1   | ǃ: 2   | ǂ: 3   | ǁ: 4   |
| Coiced implosives | ɓ: 5  | ɗ: 6   | ʄ: 7   | ɠ: 8   | ʛ: 9   |
|     Ejectives     | ʼ: 10 | pʼ: 11 | tʼ: 12 | kʼ: 13 | sʼ: 14 |
+---------------------------------------------------------------+
"""
OTHCONS = """
+--------------------------------------------------------------------+
| ʍ: 0  w: 1 | ɥ: 2 | ʜ: 3 | ʢ: 4 | ʡ: 5 | ɕ: 6 | ʑ: 7 | ɺ: 8 | ɧ: 9 |
+--------------------------------------------------------------------+
"""
VOWS = """
+--------------------------------------+
| i: 0  y: 1 | ɨ: 2  ʉ: 3 | ɯ: 4  u: 5 |
| ɪ: 6  ʏ: 7 |            |     ʊ: 8   |
| e: 9  ø: 10|ɘ: 11  ɵ: 12|ɤ: 13  o: 14|
|            |    ə: 15   |            |
|ɛ: 16  œ: 17|ɜ: 18  ɞ: 19|ʌ: 20  ɔ: 21|
|    æ: 22   |    ɐ: 23   |            |
|a: 24  ɶ: 25|            |ɑ: 26  ɒ: 27|
+--------------------------------------+
"""
SUPRA = """
+------------------------------------------------------------------------+
| ˈ: a0 | ˌ: a1 | ː: a2 | ˑ: a3 | ă: a4 | |: a5 | ‖: a6 | .: a7 | ‿: a8 |
+------------------------------------------------------------------------+
"""
TONE = """
+----------------------------------+
| ˥: 0 | ˦: 1 | ˧: 2 | ˨: 3 | ˩: 4 |
| a̋: 5 | á: 6 | ā: 7 | à: 8 | ȁ: 9 |
| ǎ: 10| â: 11| a᷄: 12| a᷅: 13| a᷈: 14|
| ꜜ: 15| ꜛ: 16| ↗: 17| ↘: 18|      |
+----------------------------------+
"""
DIAC = """
+---------------------------------------------------------------------+
| 0: ḁ | 1: a̬ | 2: aʰ| 3: a̹ | 4: a̜ | 5: a̟ | 6: a̠ | 7: ä | 8: a̽ | 9: a̩ |
|10: a̯ |11: a˞|12: a̤ |13: a̰ |14: a̼ |15: aʷ|16: aʲ|17: aˠ|18: aˤ|19: o̴ |
|20: a̝ |21: a̞ |22: a̘ |23: a̙ |24: a̪ |25: a̺ |26: a̻ |27: ã |28: aⁿ|29: aˡ|
|30: a̚ |31: ͜  |32: ͡  |      |      |      |      |      |      |      |
+---------------------------------------------------------------------+
"""

#字典
dic_pulcon = {
    0:"p",1:"b",2:"t",3:"d",4:"ʈ",5:"ɖ",6:"c",7:"ɟ",8:"k",9:"ɡ",
    10:"q",11:"ɢ",12:"ʔ",13:"m",14:"ɱ",15:"n",16:"ɳ",17:"ɲ",18:"ŋ",19:"ɴ",
    20:"ʙ",21:"r",22:"ʀ",23:"ⱱ",24:"ɾ",25:"ɽ",26:"ɸ",27:"β",28:"f",29:"v",
    30:"θ",31:"ð",32:"s",33:"z",34:"ʃ",35:"ʒ",36:"ʂ",37:"ʐ",38:"ç",39:"ʝ",
    40:"x",41:"ɣ",42:"χ",43:"ʁ",44:"ħ",45:"ʕ",46:"h",47:"ɦ",48:"ɬ",49:"ɮ",
    50:"ʋ",51:"ɹ",52:"ɻ",53:"j",54:"ɰ",55:"l",56:"ɭ",57:"ʎ",58:"ʟ"
}
dic_uplcon = {
    0:"ʘ",1:"ǀ",2:"ǃ",3:"ǂ",4:"ǁ",5:"ɓ",6:"ɗ",7:"ʄ",8:"ɠ",9:"ʛ",10:"ʼ",11:"pʼ",12:"tʼ",13:"kʼ",14:"sʼ"
}
dic_othcon = {
    0:"ʍ",1:"w",2:"ɥ",3:"ʜ",4:"ʢ",5:"ʡ",6:"ɕ",7:"ʑ",8:"ɺ",9:"ɧ"
}
dic_dow = {
    0:"i",1:"y",2:"ɨ",3:"ʉ",4:"ɯ",5:"u",6:"ɪ",7:"ʏ",8:"ʊ",9:"e",
    10:"ø",11:"ɘ",12:"ɵ",13:"ɤ",14:"o",15:"ə",16:"ɛ",17:"œ",18:"ɜ",
    19:"ɞ",20:"ʌ",21:"ɔ",22:"æ",23:"ɐ",24:"a",25:"ɶ",26:"ɑ",27:"ɒ"
}
dic_supra = {
    "a0":"ˈ","a1":"ˌ","a2":"ː","a3":"ˑ","a4":"̆","a5":"|","a6":"‖","a7":".","a8":"‿"
}
dic_tone = {
    0:"˥",1:"˦",2:"˧",3:"˨",4:"˩",5:"̋",6:"́",7:"̄",8:"̀",9:"̏",10:"̌",11:"̂",12:"᷄",13:"᷅",14:"᷈",15:"ꜜ",16:"ꜛ",17:"↗",18:"↘"
}
dic_diac = {
    0: "̥",1: "̬",2:"ʰ",3:"̹",4:"̜",5:"̟",6:"̠",7:"̈",8:"̽",9:"̩",10:"̯",11:"˞",12:"̤",
    13:"̰",14:"̼",15:"ʷ",16:"ʲ",17:"ˠ",18:"ˤ",19:"̴",20:"̝",21:"̞",22:"̘",23:"̙",
    24:"̪",25:"̺",26:"̻",27:"̃",28:"ⁿ",29:"ˡ",30:"̚",31:"͜",32:"͡"
}

choose = ""

def zh_CN_mode(output):
    while True:
        print(texts_zh[0])
        choose = input()
        if choose == "1":
            print(texts_zh[1])
            choose_con = input()
            if choose_con == "1":
                print(texts_zh[2])
                print(PULCONS)
                print(texts_zh[3])
                choose_pulcon = input()
                try:
                    output += dic_pulcon[int(choose_pulcon)]
                    print(texts_zh[4]+output)
                except: print(texts_zh[5])
                finally:
                    while True:
                        print(texts_zh[6])
                        con = input()
                        if con == "1":
                            break
                        if con == "2":
                            try:
                                root.clipboard_clear()
                                root.clipboard_append(output)
                                root.update()
                                print(texts_zh[7])
                            except:
                                print(texts_zh[8])
                            finally:
                                exi = input()
                                if exi == "1":
                                    break
                                else:
                                    exit(0)
                        if con == "3":
                            try:
                                output = output[:-1]
                                print(texts_zh[9]+output)
                                continue
                            except:
                                print(texts_zh[10])
                    continue
            if choose_con == "2":
                print(texts_zh[2])
                print(UPLCONS)
                print(texts_zh[3])
                choose_uplcon = input()
                try:
                    output += dic_uplcon[int(choose_uplcon)]
                    print(texts_zh[4]+output)
                except: print(texts_zh[5])
                finally:
                    while True:
                        print(texts_zh[6])
                        con = input()
                        if con == "1":
                            break
                        if con == "2":
                            try:
                                root.clipboard_clear()
                                root.clipboard_append(output)
                                root.update()
                                print(texts_zh[7])
                            except:
                                print(texts_zh[8])
                            finally:
                                exi = input()
                                if exi == "1":
                                    break
                                else:
                                    exit(0)
                        if con == "3":
                            try:
                                output = output[:-1]
                                print(texts_zh[9]+output)
                                continue
                            except:
                                print(texts_zh[10])
                    continue
            if choose_con == "3":
                print(texts_zh[2])
                print(OTHCONS)
                print(texts_zh[3])
                choose_othcon = input()
                try:
                    output += dic_othcon[int(choose_othcon)]
                    print(texts_zh[4]+output)
                except: print(texts_zh[5])
                finally:
                    print("是否继续添加字符，继续添加扣1，复制字符扣2")
                    con = input()
                    if con == "1":
                        continue
                    if con == "2":
                        try:
                            root.clipboard_clear()
                            root.clipboard_append(output)
                            root.update()
                            print(texts_zh[7])
                        except:
                            print(texts_zh[8])
                        finally:
                            exi = input()
                            if exi == "1":
                                continue
                            else:
                                exit(0)
        if choose == "2":
            print(texts_zh[2])
            print(VOWS)
            print(texts_zh[3])
            choose_vow = input()
            try:
                output += dic_dow[int(choose_vow)]
                print(texts_zh[4]+output)
            except: print(texts_zh[5])
            finally:
                    while True:
                        print(texts_zh[6])
                        con = input()
                        if con == "1":
                            break
                        if con == "2":
                            try:
                                root.clipboard_clear()
                                root.clipboard_append(output)
                                root.update()
                                print(texts_zh[7])
                            except:
                                print(texts_zh[8])
                            finally:
                                exi = input()
                                if exi == "1":
                                    break
                                else:
                                    exit(0)
                        if con == "3":
                            try:
                                output = output[:-1]
                                print(texts_zh[9]+output)
                                continue
                            except:
                                print(texts_zh[10])
                    continue
        if choose == "3":
            print(texts_zh[2])
            print(TONE)
            print(texts_zh[3])
            choose_tone = input()
            try:
                output += dic_tone[int(choose_tone)]
                print(texts_zh[4]+output)
            except: print(texts_zh[5])
            finally:
                    while True:
                        print(texts_zh[6])
                        con = input()
                        if con == "1":
                            break
                        if con == "2":
                            try:
                                root.clipboard_clear()
                                root.clipboard_append(output)
                                root.update()
                                print(texts_zh[7])
                            except:
                                print(texts_zh[8])
                            finally:
                                exi = input()
                                if exi == "1":
                                    break
                                else:
                                    exit(0)
                        if con == "3":
                            try:
                                output = output[:-1]
                                print(texts_zh[9]+output)
                                continue
                            except:
                                print(texts_zh[10])
                    continue
        if choose == "4":
            print(texts_zh[2])
            print(DIAC)
            print(SUPRA)
            print(texts_zh[3])
            choose_tone = input()
            try:
                try:
                    output += dic_diac[int(choose_tone)]
                except:
                    output += dic_supra[choose_tone]
                print(texts_zh[4]+output)
            except: print(texts_zh[5])
            finally:
                    while True:
                        print(texts_zh[6])
                        con = input()
                        if con == "1":
                            break
                        if con == "2":
                            try:
                                root.clipboard_clear()
                                root.clipboard_append(output)
                                root.update()
                                print(texts_zh[7])
                            except:
                                print(texts_zh[8])
                            finally:
                                exi = input()
                                if exi == "1":
                                    break
                                else:
                                    exit(0)
                        if con == "3":
                            try:
                                output = output[:-1]
                                print(texts_zh[9]+output)
                                continue
                            except:
                                print(texts_zh[10])
                    continue

def en_mode(output):
    while True:
        print(texts_EN[0])
        choose = input()
        if choose == "1":
            print(texts_EN[1])
            choose_con = input()
            if choose_con == "1":
                print(texts_EN[2])
                print(PULCONS)
                print(texts_EN[3])
                choose_pulcon = input()
                try:
                    output += dic_pulcon[int(choose_pulcon)]
                    print(texts_EN[4]+output)
                except: print(texts_EN[5])
                finally:
                    while True:
                        print(texts_EN[6])
                        con = input()
                        if con == "1":
                            break
                        if con == "2":
                            try:
                                root.clipboard_clear()
                                root.clipboard_append(output)
                                root.update()
                                print(texts_EN[7])
                            except:
                                print(texts_EN[8])
                            finally:
                                exi = input()
                                if exi == "1":
                                    break
                                else:
                                    exit(0)
                        if con == "3":
                            try:
                                output = output[:-1]
                                print(texts_EN[9]+output)
                                continue
                            except:
                                print(texts_EN[10])
                    continue
            if choose_con == "2":
                print(texts_EN[2])
                print(UPLCONS)
                print(texts_EN[3])
                choose_uplcon = input()
                try:
                    output += dic_uplcon[int(choose_uplcon)]
                    print(texts_EN[4]+output)
                except: print(texts_EN[5])
                finally:
                    while True:
                        print(texts_EN[6])
                        con = input()
                        if con == "1":
                            break
                        if con == "2":
                            try:
                                root.clipboard_clear()
                                root.clipboard_append(output)
                                root.update()
                                print(texts_EN[7])
                            except:
                                print(texts_EN[8])
                            finally:
                                exi = input()
                                if exi == "1":
                                    break
                                else:
                                    exit(0)
                        if con == "3":
                            try:
                                output = output[:-1]
                                print(texts_EN[9]+output)
                                continue
                            except:
                                print(texts_EN[10])
                    continue
            if choose_con == "3":
                print(texts_EN[2])
                print(OTHCONS)
                print(texts_EN[3])
                choose_othcon = input()
                try:
                    output += dic_othcon[int(choose_othcon)]
                    print(texts_EN[4]+output)
                except: print(texts_EN[5])
                finally:
                    print(texts_EN[7])
                    con = input()
                    if con == "1":
                        continue
                    if con == "2":
                        try:
                            root.clipboard_clear()
                            root.clipboard_append(output)
                            root.update()
                            print(texts_EN[7])
                        except:
                            print(texts_EN[8])
                        finally:
                            exi = input()
                            if exi == "1":
                                continue
                            else:
                                exit(0)
        if choose == "2":
            print(texts_EN[2])
            print(VOWS)
            print(texts_EN[3])
            choose_vow = input()
            try:
                output += dic_dow[int(choose_vow)]
                print(texts_EN[4]+output)
            except: print(texts_EN[5])
            finally:
                    while True:
                        print(texts_EN[6])
                        con = input()
                        if con == "1":
                            break
                        if con == "2":
                            try:
                                root.clipboard_clear()
                                root.clipboard_append(output)
                                root.update()
                                print(texts_EN[7])
                            except:
                                print(texts_EN[8])
                            finally:
                                exi = input()
                                if exi == "1":
                                    break
                                else:
                                    exit(0)
                        if con == "3":
                            try:
                                output = output[:-1]
                                print(texts_EN[9]+output)
                                continue
                            except:
                                print(texts_EN[10])
                    continue
        if choose == "3":
            print(texts_EN[2])
            print(TONE)
            print(texts_EN[3])
            choose_tone = input()
            try:
                output += dic_tone[int(choose_tone)]
                print(texts_EN[4]+output)
            except: print(texts_EN[5])
            finally:
                    while True:
                        print(texts_EN[6])
                        con = input()
                        if con == "1":
                            break
                        if con == "2":
                            try:
                                root.clipboard_clear()
                                root.clipboard_append(output)
                                root.update()
                                print(texts_EN[7])
                            except:
                                print(texts_EN[8])
                            finally:
                                exi = input()
                                if exi == "1":
                                    break
                                else:
                                    exit(0)
                        if con == "3":
                            try:
                                output = output[:-1]
                                print(texts_EN[9]+output)
                                continue
                            except:
                                print(texts_EN[10])
                    continue
        if choose == "4":
            print(texts_EN[2])
            print(DIAC)
            print(SUPRA)
            print(texts_EN[3])
            choose_tone = input()
            try:
                try:
                    output += dic_diac[int(choose_tone)]
                except:
                    output += dic_supra[choose_tone]
                print(texts_EN[4]+output)
            except: print(texts_EN[5])
            finally:
                    while True:
                        print(texts_EN[6])
                        con = input()
                        if con == "1":
                            break
                        if con == "2":
                            try:
                                root.clipboard_clear()
                                root.clipboard_append(output)
                                root.update()
                                print(texts_EN[7])
                            except:
                                print(texts_EN[8])
                            finally:
                                exi = input()
                                if exi == "1":
                                    break
                                else:
                                    exit(0)
                        if con == "3":
                            try:
                                output = output[:-1]
                                print(texts_EN[9]+output)
                                continue
                            except:
                                print(texts_EN[10])
                    continue



            
#MAIN
print("请输入语言版本（中文版扣1，英文版扣2）")
print("Please enter the language version (press 1 for the Chinese version, press 2 for the English version)")
version = input()
while True:
    output = ""
    if version == "1":
        zh_CN_mode(output)
    else:
        en_mode(output)