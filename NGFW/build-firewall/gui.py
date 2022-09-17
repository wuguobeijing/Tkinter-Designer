# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1317x855")
window.configure(bg="#282B2D")

canvas = Canvas(
    window,
    bg="#282B2D",
    height=855,
    width=1317,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    345.7995910644531,
    855.3531494140625,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=70.5535888671875,
    y=736.8928833007812,
    width=193.36904907226562,
    height=64.45635986328125
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=68.8115234375,
    y=555.71826171875,
    width=196.85317993164062,
    height=64.45635986328125
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=101.91070556640625,
    y=481.6805419921875,
    width=166.3670654296875,
    height=32.228179931640625
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=102.78173828125,
    y=437.2579345703125,
    width=166.3670654296875,
    height=32.22817611694336
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=101.91070556640625,
    y=398.0614929199219,
    width=166.3670654296875,
    height=32.22817611694336
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=68.8115234375,
    y=314.4424743652344,
    width=202.079345703125,
    height=64.45635223388672
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=73.16668701171875,
    y=216.88690185546875,
    width=193.36904907226562,
    height=64.45635986328125
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=87.1031494140625,
    y=112.36309814453125,
    width=166.3670654296875,
    height=64.45635986328125
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    158.1329345703125,
    42.130950927734375,
    image=image_image_1
)

canvas.create_text(
    825.0,
    257.0,
    anchor="nw",
    text="下一代防火墙V1.0，感谢使用",
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    697.3829345703125,
    159.297607421875,
    image=image_image_2
)

canvas.create_text(
    382.3829345703125,
    249.11508178710938,
    anchor="nw",
    text="防火墙管理",
    fill="#D9D9D9",
    font=("Roboto Regular", 27 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    457.3829345703125,
    403.3452453613281,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    622.8789672851562,
    403.3452453613281,
    image=image_image_4
)

canvas.create_rectangle(
    382.0,
    528.0,
    1271.0,
    819.0,
    fill="#958F93",
    outline="")

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=458.0,
    y=767.0,
    width=66.0,
    height=27.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=405.0,
    y=767.0,
    width=47.0,
    height=26.1309814453125
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=467.0,
    y=725.0,
    width=47.0,
    height=26.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=405.0,
    y=725.0,
    width=47.0,
    height=26.1309814453125
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=1140.0,
    y=623.0,
    width=88.84521484375,
    height=23.517852783203125
)

canvas.create_text(
    405.0,
    686.0,
    anchor="nw",
    text="查看规则列表",
    fill="#000000",
    font=("Roboto Regular", 15 * -1)
)

canvas.create_text(
    405.0,
    617.0,
    anchor="nw",
    text="添加指定规则",
    fill="#000000",
    font=("Roboto Regular", 15 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    832.5,
    635.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#F8F8F8",
    highlightthickness=0
)
entry_1.place(
    x=547.0,
    y=604.0,
    width=571.0,
    height=61.0
)

canvas.create_text(
    400.6745910644531,
    548.75,
    anchor="nw",
    text="防火墙规则管理",
    fill="#000000",
    font=("Roboto Regular", 27 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    658.0,
    427.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()
