from tkinter import *
from tkinter.ttk import *
import sv_ttk
from processcodes import process_codes
from utility import *

games, game_codes, code_names, void = load_games()
current_game_index = 0


class Options:
    def __init__(self, root, games):
        self.options = Frame(root)
        self.options.pack(side=LEFT, fill=BOTH, expand=True)
        self.game = StringVar()
        self.select_game = OptionMenu(
            self.options, self.game, games[0], *games, command=self.switch_game
        )
        self.select_game.config(width=len(max(games, key=len)))
        vcmd = self.options.register(self.check_delay)
        self.delay_time = Entry(
            self.options, validate="all", validatecommand=(vcmd, "%P")
        )
        self.delay_time.insert(0, 5)
        self.start_btn = Button(
            self.options, text="Start", command=self.start_processing
        )
        self.select_game.pack(anchor=W, side=TOP, padx=10, pady=10)
        Label(self.options, text="Enter the start delay in seconds:").pack(padx=10)
        self.delay_time.pack(anchor=W, padx=10, pady=10)
        self.start_btn.pack(anchor=W, side=BOTTOM, padx=10, pady=10)

    def set_codes(self, codes):
        self.codes = codes

    def switch_game(self, event):
        global current_game_index
        index = games.index(event)
        self.codes.destroy_contents()
        self.codes.populate_with_list(code_names[index])
        current_game_index = index

    def start_processing(self):
        process_codes(getdouble(self.delay_time.get()), game_codes[current_game_index])

    def check_delay(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False


class ScrollableFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.canvas = Canvas(self, borderwidth=0)
        self.frame = Frame(self.canvas)
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas["yscrollcommand"] = self.vsb.set

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window(
            (4, 4), window=self.frame, anchor="nw", tags="self.frame"
        )

        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def populate_with_list(self, list):
        self.checkboxes = []
        for index, item in enumerate(list):
            checked = IntVar()
            self.checkboxes.append([checked])
            self.checkboxes[index].append(
                Checkbutton(self.frame, text=item, variable=self.checkboxes[index][0])
            )
            self.checkboxes[index][0].set(1)
            self.checkboxes[index][1].pack(anchor=W)
        return self.checkboxes

    def destroy_contents(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


root = Tk()
sv_ttk.use_dark_theme()
root.geometry("500x400")
root.minsize(550, 300)
options = Options(root, games)

codes = ScrollableFrame(root)
options.set_codes(codes)
codes.pack(side=RIGHT, fill=BOTH, expand=True)
checkboxes = codes.populate_with_list(code_names[0])

root.mainloop()
