import requests
from bs4 import BeautifulSoup


class Translator:
    langs = {1: 'arabic', 2: 'german', 3: 'english', 4: 'spanish', 5: 'french',
             6: 'hebrew', 7: 'japanese', 8: 'dutch', 9: 'polish', 10: 'portuguese',
             11: 'romanian', 12: 'russian', 13: 'turkish'}

    def __init__(self, source, target):
        self.source_lang = source
        self.target_lang = target
        self.trans_response = None
        self.word_trans = None
        self.word_trans_example = None

    def translate(self, word):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63',
                   'Referer': 'https://context.reverso.net/translation/',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,\
                    application/signed-exchange;v=b3;q=0.9',
                   'Accept-Encoding': 'gzip, deflate, br'
                   }
        url = f'https://context.reverso.net/translation/{Translator.langs[self.source_lang]}-{Translator.langs[self.target_lang]}/{word}'
        self.trans_response = requests.get(url, headers=headers)
        return f'You chose "{self.target_lang}" as the as the language to translate "{word}"'

    def parsing(self):
        soup = BeautifulSoup(self.trans_response.content, features="html.parser")
        self.word_trans = ['Translation']
        div = soup.find(id='translations-content')
        for item in div.find_all('a'):
            if item.text != '':
                self.word_trans.append(item.text.strip())
        section_ex = soup.find(id='examples-content')
        self.word_trans_example = ['Translation']
        for item in section_ex.find_all('div', class_="example"):
            orig_text = item.find(class_="src ltr")
            self.word_trans_example.append(orig_text.get_text().strip())
            trans_text = item.find(class_="trg ltr")
            self.word_trans_example.append(trans_text.get_text().strip())

    def show_translation(self):
        number_of_examples = 5
        print(f'{Translator.langs[self.target_lang].capitalize()} Translations:')
        print('\n'.join(self.word_trans[1:number_of_examples + 1]))
        print('')
        print(f'{Translator.langs[self.target_lang].capitalize()} Examples:')
        for example in zip(self.word_trans_example[1:2 * number_of_examples + 1:2],
                           self.word_trans_example[2:2 * number_of_examples + 1:2]):
            print(f'{example[0]}:\n {example[1]}\n')

    @staticmethod
    def show_avaible_lang():
        for items in Translator.langs.items():
            print(f'{items[0]}. {items[1].capitalize()}')


Translator.show_avaible_lang()
source_l_n = int(input('Type the number of your language:'))
target_l_n = int(input('Type the number of language you want to translate to:'))
translator = Translator(source_l_n, target_l_n)
word_to_translate = input('Type the word you want to translate:')
translator.translate(word_to_translate)
if translator.trans_response.status_code == 200:
    print('200 OK\n')
translator.parsing()
translator.show_translation()