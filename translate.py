import google_trans_new
import random

lang_list = list(google_trans_new.LANGUAGES.keys())
translator = google_trans_new.google_translator()  
invalid = True


user_phrase = input("Put in the phrase you want to translate \n")
while invalid:
    trans_times = input("How many times do you want it to be translated?\n")
    if not trans_times.isdigit():
        print("please put in a valid integer\n")
        continue
    invalid = False

initial_lang = translator.detect(user_phrase)

for i in range(int(trans_times)):
    lang_choice = random.randint(0,len(lang_list)-1)
    user_phrase = translator.translate(user_phrase,lang_tgt=lang_list[lang_choice])  
    temp_phrase=translator.translate(user_phrase,lang_tgt="en")
    print(temp_phrase+ "\n")
