
#
# Catware Wikipedia Scraper
#

import os
import wikipedia
from time import sleep

SAVE_DIRECTORY = "wikipedia_pages/"

try:
        os.mkdir(SAVE_DIRECTORY)
        print(" >>> Создана папка для сохраненных статей: " + SAVE_DIRECTORY)
except:
        print(" >>> Папка " + SAVE_DIRECTORY + " уже имеется. ")

language = input(" >>> Введите ключ языка, нак на котором будут сохраняться статьи (по умолчанию ru): ")
if language == "":
        language = "ru"
else:
        wikipedia.set_lang(language)

search = input(" >>> С какой статьи начнём скрапить статьи: ")
print("Отлично. Через 3 секунды начнётся процесс скрапинга.")
sleep(3)

def writeto(text, file):
        aye = open(file, "w", encoding="utf-8")
        aye.write(text)
        aye.close()

query = [search]
alive = True
got = []
count = 0

while alive:
        for x in query:
                try:
                        if x not in got:
                                count += 1
                                st = wikipedia.summary(x)
                                al2 = True
                                while al2:
                                        if str(count) not in os.listdir(SAVE_DIRECTORY):
                                                writeto(st, SAVE_DIRECTORY + str(count) + ".txt")
                                                al2 = False
                                        else:
                                                count += 1
                                got.append(st)
                                print(" + Сохранена статья: " + " ".join(st.split(" ")[:5]))
                                for b in st.split(" "):
                                        query.append(b)
                except Exception as e:
                        print("Не удалось сохранить статью ;( ")
