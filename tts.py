from gtts import  gTTS
# 코랩 환경에서 .mp3 파일 재생
from IPython.display import  Audio

text = 'Can I help you?'
file_name ='sample.mp3'
tts_en = gTTS(text=text, lang='en')
tts_en.save(file_name)

sound = Audio(file_name, autoplay=True)

# 한글 문장
text_ko ='안녕하세요. 반갑습니다. hello'
file_name2 = "sample2.mp3"
tts_ko = gTTS(text=text_ko, lang='ko')
tts_ko.save(file_name2)
