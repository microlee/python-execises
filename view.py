from tkinter import *
import execise

cell_size = 5
is_running = False


def setup():
    global root, grid_view, cell_size, start_button, clear_button, choice

    root = Tk()
    root.title('The Game of Life')

    grid_view = Canvas(
        root,
        width=execise.width * cell_size,
        height=execise.height * cell_size,
        borderwidth=0,
        highlightthickness=0,
        bg='white')

    start_button = Button(root, text='Start', width=12)
    start_button.bind('<Button-1>', start_handler)
    clear_button = Button(root, text='Clear', width=12)

    choice = StringVar(root)
    choice.set('Choose a Pattern')
    option = OptionMenu(root, choice, 'Choose a Pattern', 'glider',
                        'glider gun', 'random')
    option.config(width=20)

    grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
    start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)


def start_handler(event):
    global is_running, start_button

    if is_running:
        is_running = False
        start_button.configure(text='Start')
    else:
        is_running = True
        start_button.configure(text='Pause')
        update()


def update():
    global grid_view

    grid_view.delete(ALL)

    execise.next_gen()
    for i in range(0, execise.height):
        for j in range(0, execise.width):
            if execise.grid_model[i][j] == 1:
                draw_cell(i, j, 'black')


def draw_cell(row, col, color):
    global grid_view, cell_size

    if color == 'black':
        outline = 'grey'
    else:
        outline = 'white'

    grid_view.create_rectangle(
        row * cell_size,
        col * cell_size,
        row * cell_size + cell_size,
        col * cell_size + cell_size,
        fill=color,
        outline=outline)


if __name__ == '__main__':
    setup()
    execise.randomize(execise.grid_model, execise.width, execise.height)
    update()
    mainloop()
