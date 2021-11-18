from tkinter import *
import random

colours = ["#ff80a3", "#ff3300", "#ff00ff", "#009933", "#000000", "#ffffff", "#ffcc00", "#333300", "#0066ff", "#00ffff"]


def complement_hex(hex):
    hex = hex[1:]
    hex = int(hex, 16)
    comp_color = 0xFFFFFF ^ hex
    comp_color = ("#%06X" % comp_color).lower()
    return comp_color


def change_colours():
    random_index = random.randrange(len(colours) - 1)
    comp_colour = complement_hex(colours[random_index])
    colourLabel.config(text=colours[random_index], fg=comp_colour, bg=colours[random_index])
    complementary_label.config(text=comp_colour, fg=colours[random_index], bg=comp_colour,)
    window.after(1000, change_colours)


if __name__ == "__main__":
    window = Tk()
    window.wm_title("Complement Colours")
    window.geometry("480x360")
    window.resizable(False, False)
    colourLabel = Label(height=180, width=240, text=colours[4], fg="white", bg=colours[4])
    complementary_label = Label(height=180, width=240, text="#ffffff", fg=colours[4], bg="white")
    colourLabel.place(width=480, height=180)
    complementary_label.place(y=180, width=480, height=180)

    window.after(1000, change_colours)
    window.mainloop()
