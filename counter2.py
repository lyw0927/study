'''
2024=12=12

'''
from tkinter import *

def count_up():
    global click_count
    click_count += 1  # 클릭 횟수 증가
    
    # 카운트 레이블 업데이트
    num = int(label_count.cget("text"))
    label_count.config(text=f"{num+1}")

    # 처음 클릭 시 타이머 시작
    if remaining_time == 5.00:
        start_timer()

def start_timer():
    global remaining_time
    if remaining_time == 5.00:  # 처음 시작할 때만 타이머 시작
        update_timer()

def disable_button():
    button.config(state=DISABLED)
    calculate_avg_speed()  # 버튼 비활성화 후 평균 클릭 속도 계산

def calculate_avg_speed():
    # 평균 클릭 속도 계산 (초당 클릭 수)
    avg_speed = click_count / 5.0  # 총 시간은 5초
    label_avg_speed.config(text=f"평균 클릭 속도: {avg_speed:.2f} 클릭/초")

def update_timer():
    global remaining_time
    if remaining_time > 0:
        label_timer.config(text=f"남은 시간: {remaining_time:.2f}초")  # 0.01초 단위로 표시
        remaining_time -= 0.01  # 0.01초씩 감소
        app.after(10, update_timer)  # 10ms 후에 호출하여 0.01초 단위로 감소
    else:
        label_timer.config(text="남은 시간: 0.00초")
        disable_button()

app = Tk()
app.title("계수기 예제")
app.geometry("500x350")

# 타이머 변수 초기화 (5초)
remaining_time = 5.00
click_count = 0  # 클릭 횟수 초기화

# 카운트 레이블
label_count = Label(app, text="0", font="Arial 20")
label_count.pack(pady=10)

# 타이머 레이블
label_timer = Label(app, text=f"남은 시간: {remaining_time:.2f}초", font="Arial 20")
label_timer.pack(pady=10)

# 평균 클릭 속도 레이블
label_avg_speed = Label(app, text="평균 클릭 속도: 0.00 클릭/초", font="Arial 20")
label_avg_speed.pack(pady=10)

# 클릭 버튼
button = Button(app, text="클릭하세요", font="Arial 20", command=count_up)
button.pack(pady=20)

app.mainloop()
