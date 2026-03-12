# kdt project

STT, TTS, VAD, 번역 기능 통합

## 파일 구성 
* `vad.py` : 음성이 존재하는 구간을 탐지 (Voice Activity Detection)
* `stt.py` : 사용자의 음성을 텍스트로 변환 (Speech-to-Text)
* `translate.py` : 인식된 텍스트를 설정된 언어로 번역
* `tts.py` : 텍스트를 다시 자연스러운 음성으로 읽기 (Text-to-Speech)
* `smart_speaker.py` : 위 기능들을 하나로 묶어 동작시키는 메인 실행 파일

## 설치 및 실행 방법 
1. 필수 패키지 설치

# pip install -r requirement.txt

git pull
git add README.md
git commit -m "fix: readme"
git push