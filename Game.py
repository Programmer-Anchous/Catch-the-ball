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
    if ball_coords[3] < 800:
        canvas.move(ball, 0, int(ball_speed))
        if 739 < ball_coords[3] < 750 and ball_coords[0] + 10 >= cube_coords[0] and ball_coords[2] - 10 <= cube_coords[
            2]:
            canvas.delete(ball)
            count += 1
            label.config(text=str(count))
            if ball_speed < 16:
                ball_speed += 0.5
                cube_speed_1 += 0.5
            x_coord = random.randrange(100, 1100)
            ball = canvas.create_oval(x_coord, 20, x_coord + 20, 40, fill='#999900')
        elif ball_coords[3] > 740:
            canvas.move(ball, 0, int(ball_speed) - 5)
    else:
        label.config(text=f"You have lost with a score of {count}.")
        master.bind("<KeyPress>", doing_nothing)
        master.bind("<KeyRelease>", doing_nothing)


def main():
    move_ball()
    move_cube()
    master.after(30, main)


def key_release(event):
    global cube_speed
    if event.keysym in "ad":
        cube_speed = 0


def doing_nothing(event):
    pass


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

label = tkinter.Label(text=str(count), font=('Helvetica', 18, 'bold'), bg="#095009", height=1, width=66)

main()
label.pack()
canvas.pack()

master.bind("<KeyPress>", key_pressed)
master.bind("<KeyRelease>", key_release)

master.mainloop()
