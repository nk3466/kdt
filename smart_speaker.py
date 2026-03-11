## smart speaker 코드

import speech_recognition as sr
from gtts import gTTS
import playsound
import os

def speak(text):
    """텍스트를 음성으로 변환하여 재생"""
    print(f"스피커: {text}")
    tts = gTTS(text=text, lang='ko')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename) # 재생 후 임시 파일 삭제

def listen():
    """마이크로부터 음성을 듣고 텍스트로 변환"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("듣고 있어요... (말씀하세요)")
        audio = r.listen(source)

    try:
        # 구글 음성 인식 사용
        text = r.recognize_google(audio, language='ko-KR')
        print(f"나: {text}")
        return text
    except sr.UnknownValueError:
        print("음성을 이해하지 못했습니다.")
        return None
    except sr.RequestError:
        print("음성 인식 서비스에 연결할 수 없습니다.")
        return None

# 실행 루프
if __name__ == "__main__":
    speak("안녕하세요! 무엇을 도와드릴까요?")
    while True:
        user_input = listen()
        if user_input:
            if "안녕" in user_input:
                speak("반가워요! 주인님.")
            elif "종료" in user_input:
                speak("프로그램을 종료합니다. 다음에 또 봐요!")
                break
            else:
                speak(f"방금 {user_input}이라고 말씀하셨나요?")