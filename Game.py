import tkinter
import random


def key_pressed(event):
    global cube_speed, cube_speed_1
    if event.keysym == "a":
        cube_speed = -cube_speed_1
    elif event.keysym == "d":
        cube_speed = cube_speed_1


def move_cube():
    cube_coords = canvas.coords(cube)
    if cube_speed < 0:
        if cube_coords[0] > 9:
            canvas.move(cube, int(cube_speed), 0)
    elif cube_speed > 0:
        if cube_coords[2] < 1191:
            canvas.move(cube, int(cube_speed), 0)


def move_ball():
    global ball, cube, count, ball_speed, cube_speed_1
    ball_coords = canvas.coords(ball)
    cube_coords = canvas.coords(cube)
    flag = True
    if ball_coords[3] < 740:
        canvas.move(ball, 0, int(ball_speed))
    else:
        if flag and ball_coords[0] + 10 >= cube_coords[0] and ball_coords[2] - 10 <= cube_coords[2]:
            canvas.delete(ball)
            count += 1
            label.config(text=str(count))
            ball_speed += 0.5
            cube_speed_1 += 0.5

            x_coord = random.randrange(100, 1100)
            ball = canvas.create_oval(x_coord, 20, x_coord + 20, 40, fill='#999900')
            flag = False
        elif ball_coords[3] < 800:
            canvas.move(ball, 0, int(ball_speed))
        else:
            canvas.delete(ball)
            x_coord = random.randrange(100, 1100)
            ball = canvas.create_oval(x_coord, 20, x_coord + 20, 40, fill='#999900')


def main():
    move_ball()
    move_cube()
    master.after(30, main)


def key_release(event):
    global cube_speed
    if event.keysym in "ad":
        cube_speed = 0


cube_speed = 0
cube_speed_1 = 13
master = tkinter.Tk()
master.title("Falling Balls")
canvas = tkinter.Canvas(master, bg='#095009', height=800, width=1200)
canvas.create_line(0, 60, 1200, 60)

cube = canvas.create_rectangle(530, 740, 670, 760, fill='#191990')

x = random.randrange(0, 1180)
ball = canvas.create_oval(x, 20, x + 20, 40, fill='#999900')
ball_speed = 5

count = 0

label = tkinter.Label(master, text=str(count))

main()
label.pack()
canvas.pack()

master.bind("<KeyPress>", key_pressed)
master.bind("<KeyRelease>", key_release)

master.mainloop()
