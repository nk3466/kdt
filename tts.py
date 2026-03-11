from gtts import  gTTS


# 영어 문장 사운드 파일 생성 및 저장
text = 'Can I help you?'
file_name ='sample.mp3'
tts_en = gTTS(text=text, lang='en')
tts_en.save(file_name)

# 코랩 환경에서 .mp3 파일 재생
from IPython.display import  Audio

sound = Audio(file_name, autoplay=True)