import csv
from gtts import gTTS
import pathlib
import shutil


def reader_words():
    try:
        words_front =[]
        words_back = []
        with open("words.csv", "r", encoding="utf-8") as f: #write name csv
            read = csv.reader(f, delimiter=",")
            for row in read:
                words_front.append(row[0])
                words_back.append(row[1])
        return (words_front, words_back)
    except FileNotFoundError as error_file:
        print(error_file)


def audio_convert(LANG="en", TLD="com"): #ISO-639
    try:
        (wordFront, wordBack) = reader_words()
        for word in wordFront:
            name_mp3 = word + ".mp3"
            audio = gTTS(word, lang=LANG, tld=TLD) # Convert texto to audio
            print("Your text is converting...")
            audio.save(name_mp3) # Save audio file

            # Output move file
            path = pathlib.Path().absolute() # Get path
            path = str(path) + '/output/'
            shutil.move(name_mp3, path) # move file audio to output folder
            print("Save >>> " + path + name_mp3)
    except TypeError as error:
        print(error)


def csv_for_anki():
    try:
        (wordFront, wordBack) = reader_words()
        with open('AnkImport.csv', 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['front', 'back']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for valueWF, valueWB in zip(wordFront, wordBack):
                front = valueWF + "<br>" + '[sound:{}.mp3]'.format(valueWF)
                back = valueWB
                writer.writerow({'front': front, 'back': back})
    except:
        print("error to create csv for anki")            

            
def run():
    audio_convert()
    csv_for_anki()


if __name__ == "__main__":
    run()
