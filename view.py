from tkinter import *
import execise

cell_size = 5


def setup():
    global root, grid_view, cell_size, start_button, clear_button, choice

    root = Tk()
    root.title('The game of life')

    grid_view = Canvas(
        root,
        width=execise.width * cell_size,
        height=execise.height * cell_size,
        borderwidth=0,
        highlightthickness=0,
        bg='white')

    start_button = Button(root, text='Start', width=12)
    clear_button = Button(root, text='Clear', width=12)

    choice = StringVar(root)
    choice.set('Choice a Pattern')
    option = OptionMenu(root, choice, 'Choose a Pattern', 'glider',
                        'glider gun', 'random')
    option.config(width=20)

    grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
    start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)


if __name__ == '__main__':
    setup()
    mainloop()
