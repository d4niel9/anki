import csv
from gtts import gTTS
import pathlib
import shutil


class Anki():


    def __init__(self, csv):
        self.csv = csv
        self._reader_words()


    def _reader_words(self):
        try:
            words_front =[]
            words_back = []
            with open(self.csv, "r", encoding="utf-8") as f: #write name csv
                read = csv.reader(f, delimiter=",")
                for row in read:
                    words_front.append(row[0])
                    words_back.append(row[1])
            return (words_front, words_back)
        except FileNotFoundError as error_file:
            raise
            print(error_file)


    def audio_convert(self,LANG,TLD): #ISO-639
        try:
            (wordFront, wordBack) = self._reader_words()
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


    def csv_for_anki(self):
        try:
            (wordFront, wordBack) = self._reader_words()
            with open('AnkImport.csv', 'w', newline='', encoding="utf-8") as csvfile:
                fieldnames = ['front', 'back']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for valueWF, valueWB in zip(wordFront, wordBack):
                    front = valueWF + "<br>" + '[sound:{}.mp3]'.format(valueWF)
                    back = valueWB
                    writer.writerow({'front': front, 'back': back})
        except:
            print("error to create csv for anki")            


def main():
    try:
        instructions =  """
        *******************************************
                            ANKI
        * Instructions:
        - Enter path name file csv words
        - Select option language to convert words
        *******************************************
                           OPTIONS
        [1] englich
        [2] espanish
        [3] portuguese
        [4] italian
        [5] french
        [6] ruso
        *******************************************
        """
        print(instructions)
        path_csv = str(input("Enter path name file csv: \n>>> "))
        csv_file = Anki(path_csv)

        option = int(input("Enter the option to download: \n>>> "))

        if option == 1:
            lang = "en"
            tld = "com"
            csv_file.audio_convert(lang,tld)
            csv_file.csv_for_anki()

        elif option == 2:
            lang = "es"
            tld = "com.mx"
            csv_file.audio_convert(lang,tld)
            csv_file.csv_for_anki()

        elif option == 3:
            lang = "pt"
            tld = "pt"
            csv_file.audio_convert(lang,tld)
            csv_file.csv_for_anki()

        elif option == 4:
            lang = "it"
            tld = "it"
            csv_file.audio_convert(lang,tld)
            csv_file.csv_for_anki()

        elif option == 5:
            lang = "fr"
            tld = "fr"
            csv_file.audio_convert(lang,tld)
            csv_file.csv_for_anki()
            
         elif option == 6:
            lang = "ru"
            tld = "ru"
            csv_file.audio_convert(lang,tld)
            csv_file.csv_for_anki()
        else:
            print("option no valid")
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()
