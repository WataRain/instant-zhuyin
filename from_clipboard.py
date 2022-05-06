import pyperclip
from dragonmapper import hanzi

text = pyperclip.paste()
guoyin = hanzi.to_zhuyin(text).replace('\n', ' ')
input(text + '\n' + guoyin)
pyperclip.copy(guoyin)
