#https://stackoverflow.com/questions/21044407/tkinter-app-allowing-for-multiple-languages
#https://stackoverflow.com/questions/67387843/how-to-create-a-language-button-for-tkinter

from babel.support import Translations 
LOCALE_PATH = 'locale' # the path of the locale folder
LANGUAGE = 'en_US' # what language you wanna use
translations = Translations.load(LOCALE_PATH, [LANGUAGE])
_ = translations.gettext

print(_('Hi')) # it would be translated to the target value from the PO file