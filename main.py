from googletrans import Translator

'''
pip install googletrans==3.1.0a0

Закинуть меню в корневую в файл menu.txt
'''

def menu_translator(lang):
    translated_menu = ''
    with open('menu.txt', 'r', encoding='utf-8') as file:
        strings = file.readlines()
        for str in strings:
            if 'name' in str:
                try:
                    arr = str.split('"')
                    translator = Translator()
                    result = translator.translate(arr[1], dest=lang)
                    arr[1] = f'"{result.text}"'
                    translated_str = ''
                    translated_str = translated_str.join(arr)
                    translated_menu += translated_str
                except Exception as ex:
                    print(ex)
            if 'url' in str:
                arr = str.split('"')
                arr[1] = f'"/{lang}{arr[1]}"'
                translated_str = ''
                translated_str = translated_str.join(arr)
                translated_menu += translated_str
            if '[[menu.' in str:
                translated_menu += f'{str[0:2]}languages.{lang}.{str[2:]}'
            if 'name' not in str and 'url' not in str and '[[menu.' not in str:
                translated_menu += str
    with open(f'menu-{lang}.txt', 'w', encoding='utf-8') as file:
        file.write(translated_menu)

if __name__ == '__main__':
    # Указываем список языков, на которые нужно перевести
    langs = ['en', 'hi', 'uz']
    for l in langs:
        menu_translator(l)
