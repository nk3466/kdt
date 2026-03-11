import os
import torch
import whisperx
from gtts import gTTS

class SpeechTextPipeline:
    """
    STT (WhisperX) 와 TTS (gTTS) 를 결합한 통합 파이프라인 클래스
    """
    def __init__(self, stt_model_size="base", stt_language="ko", tts_language="ko"):
        print("초기화 중... WhisperX 모델을 로드합니다.")
        # 디바이스 설정 (CUDA 사용 가능시 GPU, 아니면 CPU)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # CPU일 경우 int8, GPU일 경우 float16 연산 사용 권장
        self.compute_type = "float16" if self.device == "cuda" else "int8"
        self.stt_language = stt_language
        self.tts_language = tts_language
        
        # WhisperX 모델 로드
        self.stt_model = whisperx.load_model(stt_model_size, self.device, compute_type=self.compute_type)
        print(f"WhisperX 모델 '{stt_model_size}' 로드 완료! (Device: {self.device})")

    def transcribe_audio(self, audio_path: str) -> str:
        """
        주어진 오디오 파일을 WhisperX를 통해 텍스트로 변환 (STT)
        """
        print(f"[{audio_path}] 음성 인식을 시작합니다...")
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"오디오 파일을 찾을 수 없습니다: {audio_path}")
            
        # 오디오 파일 로드
        audio = whisperx.load_audio(audio_path)
        
        # 트랜스크립션 수행
        result = self.stt_model.transcribe(audio, batch_size=16, language=self.stt_language)
        
        # 결과 텍스트 추출 (세그먼트들의 텍스트 결합)
        transcribed_text = " ".join([segment["text"] for segment in result["segments"]])
        return transcribed_text

    def synthesize_speech(self, text: str, output_path: str = "output_tts.mp3") -> str:
        """
        주어진 텍스트를 gTTS를 통해 오디오 파일로 변환 (TTS)
        """
        print("텍스트를 음성으로 변환 중입니다...")
        if not text.strip():
            print("경고: 빈 텍스트가 입력되어 TTS 변환을 건너뜁니다.")
            return ""
            
        tts = gTTS(text=text, lang=self.tts_language)
        tts.save(output_path)
        print(f"TTS 생성 완료! 파일 저장됨: {output_path}")
        return output_path

    def process_pipeline(self, input_audio_path: str, output_audio_path: str = "output_tts.mp3") -> dict:
        """
        사용자의 음성 입력(STT) -> 텍스트 도출 -> 텍스트 변환/그대로 사용 -> 음성 합성(TTS) 전체 과정
        """
        print("=== [ STT -> TTS 파이프라인 시작 ] ===")
        # 1. STT: 음성 입력 -> 텍스트
        try:
            transcribed_text = self.transcribe_audio(input_audio_path)
            print(f"> 인식된 텍스트: {transcribed_text}")
        except Exception as e:
            print(f"STT 에러 발생: {e}")
            return {"status": "error", "message": str(e)}

        # 2. TTS: 텍스트 -> 새로운 음성 출력
        # 필요시 이 부분에서 LLM을 호출하여 답변 텍스트(Response)를 생성받은 뒤 TTS로 전달할 수 있습니다.
        # 현재는 인식된 텍스트를 그대로 다시 읽어주는 에코(Echo) 형태로 구현합니다.
        try:
            saved_file = self.synthesize_speech(transcribed_text, output_path=output_audio_path)
        except Exception as e:
            print(f"TTS 에러 발생: {e}")
            return {"status": "error", "message": str(e)}

        print("=== [ 파이프라인 종료 ] ===\n")
        return {
            "status": "success",
            "input_file": input_audio_path,
            "transcribed_text": transcribed_text,
            "output_file": saved_file
        }


if __name__ == "__main__":
    # ===== 테스트 실행 예시 =====
    # (1) 본인의 환경에 맞는 입력 오디오 파일 경로를 설정하세요. (예: stt.py에 있던 'sample.wav')
    sample_input = "sample.wav" 
    sample_output = "result_response.mp3"
    
    # 더미 오디오 파일이 없는 경우를 대비한 생성 코드 (테스트용)
    if not os.path.exists(sample_input):
        print(f"테스트용 '{sample_input}' 파일이 없어 gTTS를 이용해 임시 생성합니다...")
        temp_tts = gTTS("안녕하세요, 테스트 음성입니다.", lang='ko')
        temp_tts.save(sample_input)
    
    # パ이프라인 객체 생성 (기본 모델 'base', 한국어 인식 세팅)
    pipeline = SpeechTextPipeline(stt_model_size="base", stt_language="ko")
    
    # 단독으로 한 파일을 처리
    result_data = pipeline.process_pipeline(input_audio_path=sample_input, output_audio_path=sample_output)
    
    print("\n[최종 결과]")
    print(result_data)
