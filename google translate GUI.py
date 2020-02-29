sources='https://www.cnblogs.com/by-dream/p/6554340.html'

import js
import js2py
import requests
import tkinter


# Func: Translate
def translation():

    def translate(keyword):
        """
        func: chinese_word:
        determine is it a chinese word
        """
        def chinese_word(words):
            for i in words:
                # Chinese words in unicode[\\u4e00-\\u9fa5]
                if '\u4e00' <= i <= '\u9fa5':
                    return True
            return False

        """
        func: get_tk:
        translate json
        """
        def get_tk(words):
            eval_js = js2py.EvalJs()
            js_code = js.gg_js_code
            eval_js.execute(js_code)
            tk = eval_js.TL(words)
            return tk

        # requesting with acceptable browser
        headers = {
            # 29/2/2020 user agent from translate.google
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        }
        # Fixed website,dont change it
        url = 'https://translate.google.cn/translate_a/single?client=t&sl=auto&tl={}&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&tk={}&q={}'

        # Entry box can fit until 1000words only
        if len(keyword) > 1000:
            raise RuntimeError('The length of word should be less 1000words')

        '''
        if not : chineses words Translation(target language) will set as not detect language
        else   : itis chineses words 'Translation' will set as English
        '''
        languague = ['zh-CN', 'en']
        if not chinese_word(keyword):
            # translate language = 'zh-CN'
            translate_language = languague[0]
        else:
            # translate language = 'en'
            translate_language = languague[1]
        # Request format
        res = requests.get(url.format(translate_language, get_tk(keyword), keyword), headers=headers)
        return [res.json()[0][0][0]]

    keyword = str_keyword.get()
    results = translate(keyword)
    str_translation.set(';'.join(results))

# Main
# Main window
window = tkinter.Tk()
window.title('Google Translate GUI')
window.geometry('400x250')
# font size
large_font = ('Arial', 10)
# Sentences
tkinter.Label(window, text='keyword :', font=large_font).place(x=55, y=43)
tkinter.Label(window, text='target   :', font=large_font).place(x=55, y=160)
# Button
btn_translate = tkinter.Button(window, text='Translate', command=translation).place(x=170, y=105)
# String
str_keyword = tkinter.StringVar()
str_translation = tkinter.StringVar()
str_translation.set('         Translation')
# Entry box
translate_keyword = tkinter.Entry(window, textvariable=str_keyword, font=large_font)
translation_word = tkinter.Entry(window, textvariable=str_translation, font=large_font)
translate_keyword.grid(padx=130, pady=30, ipady=15)
translation_word.grid(padx=130, pady=40, ipady=15)

window.mainloop()
