## smart speaker 코드

class SmartSpeaker:
    def __init__(self, name):
        self.name = name
        self.volume = 5  # 기본 볼륨 설정

    def set_volume(self, volume):
        if 0 <= volume <= 10:
            self.volume = volume
            print(f"{self.name}의 볼륨이 {self.volume}로 설정되었습니다.")
        else:
            print("볼륨은 0에서 10 사이로 설정해야 합니다.")

    def play_music(self, song):
        print(f"{self.name}에서 '{song}'을(를) 재생합니다.")

    def stop_music(self):
        print(f"{self.name}에서 음악이 중지되었습니다.")
# 스마트 스피커 인스턴스 생성
my_speaker = SmartSpeaker("My Smart Speaker")
# 볼륨 설정
my_speaker.set_volume(7)
# 음악 재생
my_speaker.play_music("Shape of You")
# 음악 중지
my_speaker.stop_music()
