import tkinter as tk
import os

mode = "auto"


def switch_mode(newMode):

    global mode
    mode = newMode
    print(mode)
    update()

def update():
    file = open("mode.txt", "w")

    val = str(speedScale.get())
    print(val)
    if mode == "auto":
        file.write(mode)
    else:
        file.write(mode+" "+val)
    file.close()

app = tk.Tk()
tk.Label(app, text="Fan Controls").pack()

tk.Button(app, text="Auto", width=25, command=lambda: switch_mode("auto")).pack()
tk.Button(app, text="Manual", width=25, command=lambda: switch_mode("manual")).pack()
speedScale = tk.Scale(app, from_=0, to=100, orient="horizontal")

speedScale.pack()
app.mainloop()





