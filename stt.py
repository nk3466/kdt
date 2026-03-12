import speech_recognition as sr


def speech_to_text(audio_path: str, language: str = "ko"):
    """
    오디오 파일을 텍스트로 변환하는 함수
    :param audio_path: 음성 파일 경로
    :param language: 인식 언어 (default: 한국어)
    :return: 변환된 텍스트
    """
    
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            print("음성을 인식 중입니다...")
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data, language=language)
        return text

    except sr.UnknownValueError:
        return "음성을 인식하지 못했습니다."

    except sr.RequestError as e:
        return f"Google STT 요청 실패: {e}"

    except FileNotFoundError:
        return "오디오 파일을 찾을 수 없습니다."


if __name__ == "__main__":
    audio_file = "sample.wav"

    result = speech_to_text(audio_file)
    print("변환된 텍스트:", result)

    # 비틀비틀 걸어가는 나의 다리, 오늘도 의미없는 또하루가 지나가고