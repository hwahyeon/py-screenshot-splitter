import tkinter as tk
from tkinter import IntVar
import mss
import os
import datetime
from PIL import Image
import time

def take_screenshots():
    root.withdraw()
    time.sleep(0.5)

    with mss.mss() as sct:
        monitors = sct.monitors[1:]  # 첫 번째 항목(전체 화면)은 제외

        for monitor_number, monitor in enumerate(monitors, start=1):
            # 체크박스 설정에 따라 적절한 모니터의 스크린샷을 촬영
            if (monitor_number == 1 and left_monitor.get()) or (monitor_number == 2 and right_monitor.get()):
                shot = sct.grab(monitor)
                img = Image.frombytes('RGB', (shot.width, shot.height), shot.rgb)

                filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_Monitor_{monitor_number}.png"
                img.save(os.path.join('screenshots', filename))

    root.deiconify()
    label.config(text="Screenshots Saved")

# GUI 설정
root = tk.Tk()
root.title("Screenshot App")
root.geometry("200x130")

if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# 체크박스 상태를 저장할 변수
left_monitor = IntVar()
right_monitor = IntVar()

# 체크박스 생성
left_monitor_check = tk.Checkbutton(root, text="Left Monitor (L)", variable=left_monitor)
left_monitor_check.pack()
right_monitor_check = tk.Checkbutton(root, text="Right Monitor (R)", variable=right_monitor)
right_monitor_check.pack()

button = tk.Button(root, text="Take Screenshots", command=take_screenshots)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
