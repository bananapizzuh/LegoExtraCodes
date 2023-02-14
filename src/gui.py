from tkinter import *
from tkinter.ttk import *
import yaml
import time, sv_ttk
#from src.controller import controller
#import processcodes
games = []
codes = []
code_names = []
current_game_index = 0

def load_codes():
    with open('codes.yaml', 'r') as openfile:
        config = yaml.safe_load(openfile)
        for game in config:
            try:  
                games.append(config[game]['name'])
                codes.append(config[game]['codes'])
                code_names.append(config[game]['code_names'])
            except:
                print(f'Failed to load {game} from config.')

class Options():
    def __init__(self, root, games):
        self.options = Frame(root)
        self.options.pack(side=LEFT, fill=BOTH, expand=True)
        self.game = StringVar()
        self.game.set(games[0])
        self.select_game = OptionMenu(self.options, self.game, games[0], *games, command=self.switch_game)
        self.select_game.config(width=len(max(games, key=len)))
        self.select_game.pack(anchor=NW, padx=10, pady=10)
        self.start_btn = Button(self.options, text="Start")
        self.start_btn.pack(anchor=W, side = "bottom", padx=10, pady=5) 
    
    def set_codes(self, codes):
        self.codes = codes

    def switch_game(self, event):
        index = games.index(event)
        self.codes.destroy_contents()
        self.codes.populate_with_list(code_names[index])
        current_game_index = index
        


class ScrollableFrame(Frame):
    def __init__(self, parent):

        Frame.__init__(self, parent)
        self.canvas = Canvas(self, borderwidth=0)
        self.frame = Frame(self.canvas)
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas["yscrollcommand"] = self.vsb.set

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def on_frame_configure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def populate_with_list(self, list):
        self.checkboxes = []
        for index, item in enumerate(list):
            checked = IntVar()
            self.checkboxes.append([checked])
            self.checkboxes[index].append(Checkbutton(self.frame, text=item, variable=self.checkboxes[index][0]))
            self.checkboxes[index][0].set(1)
            self.checkboxes[index][1].pack(anchor=W)
        return self.checkboxes
    
    def destroy_contents(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


root = Tk()
load_codes()
sv_ttk.use_dark_theme()
root.geometry("500x400")
root.minsize(550, 300)
options = Options(root, games)    

codes = ScrollableFrame(root)
options.set_codes(codes)
codes.pack(side=RIGHT, fill=BOTH, expand=True)
checkboxes = codes.populate_with_list(code_names[0])

root.mainloop()