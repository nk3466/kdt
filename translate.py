## translate 코드
from translate import Translator

text = "배고프니?? 밥 먹어."

# Translator 객체 생성
translator = Translator(to_lang='ja', from_lang='ko')

result = translator.translate(text)

print('원본: ', text)
print('번역: ', result)