import whisperx
from gtts import gTTS


# CPU만 사용
device = "cpu"


# STT 함수
def speech_to_text(audio_path):
    # WhisperX 모델 불러오기 (base 모델 사용)
    model = whisperx.load_model("base", device, compute_type="int8")  # CPU는 int8 사용

    # 오디오 파일 불러오기
    audio = whisperx.load_audio(audio_path)

    # 음성 인식 수행
    result = model.transcribe(audio, language="ko")

    # 인식된 텍스트 합치기
    text = ""
    for segment in result["segments"]:
        text += segment["text"] + " "

    return text.strip()


# TTS 함수
def text_to_speech(text, output_file="output.mp3"):
    # gTTS를 사용해 텍스트를 음성으로 변환 (한국어)
    tts = gTTS(text=text, lang="ko")
    tts.save(output_file)
    print(f"음성 파일 저장 완료: {output_file}")


# 전체 파이프라인 실행
audio_file = "sample.wav"
output_file = "output.mp3"

print("음성 인식 중...")
recognized_text = speech_to_text(audio_file)
print("인식된 텍스트:", recognized_text)

print("음성 합성 중...")
text_to_speech(recognized_text, output_file)

print("완료!")
