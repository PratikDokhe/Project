import math
from tkinter import *
import math

# ------------------------------------------------ CONSTANTS ------------------------------------------------- #
PINK = "#e2979c"
RED = "#3e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
LIGHT_GREEN = "#cff6cf"  # 1
LIGHT_GREY = "#cfe5cf"  # 2
VOILET = "#e5cfe5"  # 3
LIGHT_VOILET = "#f6def6"  # 4
BLUE = "#21094e"  # 5
DARK = "#393232"  # 6
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
i = 0
my_timer = None


# ------------------------------------------------ TIMER RESET ------------------------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(canvastxt, text="00:00")
    timer_label.config(text=" ^Timer^")

    checkmark_label.config(text="")


# ------------------------------------------------ TIMER MECHANISM --------------------------------------------- #

def start_timer():
    global reps, i

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        timer = long_break_sec
        reps = 1
        timer_label.config(text=" Long Break", fg=DARK)
        i = 1
        counter(timer)
    elif reps % 2 == 0:
        timer = short_break_sec
        reps += 1
        timer_label.config(text=" Short Break", fg=PINK)

        counter(timer)
    elif reps % 2 == 1:
        timer = work_sec
        reps += 1
        i += 1
        timer_label.config(text=" Work!", fg=GREEN)

        counter(timer)




# ------------------------------------------------ COUNTDOWN MECHANISM ----------------------------------------- #
def counter(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvastxt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, counter, count - 1)
    else:
        global i
        check = "✔" * i

        checkmark_label.config(text=check)

        start_timer()


# ------------------------------------------------ UI SETUP ---------------------------------------------------- #
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=40, pady=25, bg=LIGHT_VOILET)

canvas = Canvas(width=400, height=400, bg=LIGHT_VOILET, highlightthickness=0)
apple_img = PhotoImage(file="Green-Apple-PNG-Pic.png")
canvas.create_image(210, 190, image=apple_img)
canvastxt = canvas.create_text(210, 238, text="00:00", fill="lavender", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text=" ^Timer^", font=(FONT_NAME, 40, "bold"), bg=LIGHT_VOILET, fg=BLUE)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

checkmark_label = Label(font=(FONT_NAME, 14, "bold"), bg=LIGHT_VOILET, fg=DARK)
checkmark_label.grid(row=3, column=1)

window.mainloop()
