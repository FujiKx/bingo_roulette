import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random
import time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

class BingoGame:
    def __init__(self):
        self.numbers = list(range(1, 76))  # 1から75までの数字を用意
        self.called_numbers = []          # 呼び出された数字を記録
        self.last_called = None           # 直近に呼び出された数字を記録

    def spin(self):
        if not self.numbers:
            return None  # 数字がなくなったらNoneを返す
        number = random.choice(self.numbers)
        self.numbers.remove(number)
        self.called_numbers.append(number)
        self.last_called = number
        return number

def start_bingo():
    if game.numbers:
        spin_animation()
        number = game.spin()
        if number is not None:
            result_label.config(text=f"{number}", fg="red")
            update_table(number)
        else:
            result_label.config(text="終了！")
    else:
        result_label.config(text="終了！")

def reset_game():
    global game
    game = BingoGame()
    result_label.config(text="BINGO!", fg="black")
    for label in number_labels:
        label.config(bg="#FFD93F")

def update_table(number):
    for label in number_labels:
        if int(label.cget("text")) == number:
            label.config(bg="red")  # 直近の数字を赤色で強調
        elif int(label.cget("text")) in game.called_numbers:
            label.config(bg="pink") 

def spin_animation():
    for _ in range(10):  
        result_label.config(text=random.randint(1, 75), fg=random.choice(["gray", "blue", "green", "purple", "black", "red", "cyan", "magenta", "orange"]))
        result_label.update()
        time.sleep(0.05)
    for _ in range(5):
        result_label.config(text=random.randint(1, 75), fg=random.choice(["gray", "blue", "green", "purple", "black", "red", "cyan", "magenta", "orange"]))
        result_label.update()
        time.sleep(0.15)

# アプリのセットアップ
root = tk.Tk()
root.title("ビンゴゲーム ルーレット")
root.attributes("-fullscreen", True)

# 背景画像の設定
background_image = Image.open("sozai/haikei.jpg")  
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# ゲームインスタンス
game = BingoGame()

# 結果表示用フレーム
result_frame = tk.Frame(root, bg="#FFCD00")
result_frame.pack(pady=50)

result_label = tk.Label(result_frame, text="BINGO!", font=("Arial", 120, "bold"), fg="black", bg="#FFCD00")
result_label.pack(padx=10)

# ルーレットボタン
button_image = Image.open("sozai/button-image.png")
button_image = button_image.resize((120, 80))
button_photo = ImageTk.PhotoImage(button_image)

spin_button = tk.Button(root, image=button_photo, text="", compound="center", command=start_bingo)
spin_button.image = button_photo  # 参照を保持
spin_button.pack(pady=10)

# 数字の表を表示
number_frame = tk.Frame(root, bg="#FFCD00")
number_frame.pack(pady=20)

number_labels = []
for i in range(1, 76):
    label = tk.Label(number_frame, text=f"{i}", font=("Arial", 30, "bold"), width=4, height=2, bg="#FFD93F", relief="solid", borderwidth=1)
    label.grid(row=(i-1)//15, column=(i-1)%15, padx=5, pady=5)
    number_labels.append(label)

# ボタンを横に配置するフレーム
button_frame = tk.Frame(root, bg="#FFCD00")
button_frame.pack(pady=10)

reset_button = tk.Button(button_frame, text="リセット", font=("Arial", 18), command=reset_game)
reset_button.pack(side="left", padx=10)

exit_button = tk.Button(button_frame, text="終了", font=("Arial", 18), command=root.destroy)
exit_button.pack(side="left", padx=10)

# 余白に画像を追加（右上）
top_right_image = Image.open("sozai/piero2.jpg")   # 追加画像ファイルのパス
top_right_image = top_right_image.resize((300, 300))  # サイズ調整
top_right_photo = ImageTk.PhotoImage(top_right_image)

top_right_image_label = tk.Label(root, image=top_right_photo, bg="white")
top_right_image_label.place(relx=0.7, rely=0.05)  # 画面の右上に配置

# 余白に画像を追加（左上）
top_left_image = Image.open("sozai/piero2.jpg")  
top_left_image = top_left_image.resize((300, 300))  
top_left_photo = ImageTk.PhotoImage(top_left_image)

top_left_image_label = tk.Label(root, image=top_left_photo, bg="white")
top_left_image_label.place(relx=0.1, rely=0.05)  # 画面の左上に配置

# メインループ開始
root.mainloop()
