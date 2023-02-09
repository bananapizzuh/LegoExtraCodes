from tkinter import *
from tkinter.ttk import *
import time
from controller import controller
import processcodes, sv_ttk

gamepad = controller()

lego_star_wars_codes = ['Chewbacca carrying C-3PO', 'Silhouettes', 'Fertilizer', 'Tractor Beam', 'Super Slap', 'Regenerate Hearts', 'Zam Wesell (27500 Studs)', 'Droid Trifighter, (28000 Studs)', 'Admiral Ackbar (33000 Studs)', 'Battle Droid (6500 Studs)', 'TIE Fighter Pilot (21000 Studs)', 'Vulture Droid, (30000 Studs)', 'Clone (13000 Studs)', 'Ben Kenobi (Ghost) (1100000 Studs)', 'Beach Trooper (20000 Studs)', 'Bounty Hunter Rockets (switch character to use)', 'Imperial Shuttle Pilot (25000 Studs)', 'Rebel Pilot (15000 Studs)', 'Deflect Bolts', 'Boba Fett (100000 Studs)', 'Disguises', 'Lobot (11000 Studs)', 'TIE Fighter (Darth Vader), (50000 Studs)', 'Wookiee (16000 Studs)', 'Skiff Guard (12000 Studs)', 'Fast Force', 'Sandtrooper (14000 Studs)', 'Disguised Clone (12000 Studs)', 'Bespin Guard (15000 Studs)', 'Ugnaught (36000 Studs)', 'Force Zipline', 'TIE Fighter, (35000 Studs)', 'Count Dooku (100000 Studs)', 'Super Zapper', 'Rebel Trooper (10000 Studs)', 'Character Studs', 'Score x4', 'Dark Side', 'Self Destruct', '4-LOM (45000 Studs)', 'Aayla Secura (37000 Studs)', 'The Emperor (275000 Studs)', 'Super Ewok Catapult', 'Darth Maul (60000 Studs)', 'R2-Q5 (100000 Studs)', 'Ewok (34000 Studs)', 'Exploding Blaster Bolts', 'Minikit Detector', 'Power Brick Detector', 'Dengar (70000 Studs)', 'Boba Fett (Boy) (5500 Studs)', 'Super Lightsabers', 'Rebel Trooper (Hoth) (16000 Studs)', 'IG-88 (100000 Studs)', 'Imperial Guard (45000 Studs)', 'Score x2', 'Super Battle Droid (25000 Studs)', 'Super Blasters', 'Boss Nass (15000 Studs)', 'TIE Bomber, (60000 Studs)', 'Anakin Skywalker (Ghost) (1000000 Studs)', 'Disarm Troopers', 'Geonosian (20000 Studs)', 'Invincibility', 'Imperial Shuttle, (25000 Studs)', 'Snowtrooper (16000 Studs)', 'Battle Droid (Security) (8500 Studs)', 'Bossk (75000 Studs)', 'TIE Interceptor, (40000 Studs)', "Grievous' Bodyguard (42000 Studs)", 'Dexter Jettster (10000 Studs)', 'Mace Windu (Episode III) (38000 Studs)', 'Walkie Talkie', 'Tow Death Star', 'Daisychains', 'Shaak Ti (36000 Studs)', 'Fast Build', 'Han Solo (Hood) (20000 Studs)', 'Lama Su (9000 Studs)', 'Jango Fett (70000 Studs)', 'Imperial Officer (28000 Studs)', 'Battle Droid (Commander) (10000 Studs)', 'Luminara (28000 Studs)', 'Bib Fortuna (16000 Studs)', 'Ki-Adi Mundi (30000 Studs)', 'Extra Toggle', 'Stormtrooper (10000 Studs)', 'Clone (Episode III, Walker) (12000 Studs)', 'Death Star Trooper (19000 Studs)', 'Battle Droid (Geonosis) (8500 Studs)', 'Score x6', 'Clone Arcfighter, (33000 Studs)', 'Gamorrean Guard (40000 Studs)', 'Infinite Torpedos', 'Jawa (24000 Studs)', 'Perfect Deflect', 'Plo Koon (39000 Studs)', 'Watto (16000 Studs)', 'General Grievous (70000 Studs)', 'Poo Money', 'Palace Guard (14000 Studs)', 'Taun We (9000 Studs)', 'Force Pull', 'Princess Leia (Prisoner) (22000 Studs)', 'Captain Tarpals (17500 Studs)', 'Clone (Episode III, Swamp) (12000 Studs)', 'Super Astromech', 'Pit Droid (4000 Studs)', 'Super Jedi Slam', 'Vehicle Smart Bomb', 'Super Gonk', 'Kit Fisto (35000 Studs)', 'Super Thermal Detonators', 
"Sebulba's Pod, (20000 Studs)", 'Luke Skywalker (Hoth) (14000 Studs)', "Zam's Speeder (24000 Studs)", 'Padmé (20000 Studs)', 'Clone (Episode III) (10000 Studs)', 'Yoda (Ghost) (1200000 Studs)', 'Beep beep', 'Score x10', 'Stud Magnet', 'Grand Moff Tarkin (38000 Studs)', 'Droideka (40000 Studs)', 'Clone (Episode III, Pilot) (11000 Studs)', 'Score x8', 'Royal Guard (10000 Studs)', 'Tusken Raider (23000 Studs)', 'Imperial Spy (13500 Studs)', 'Greedo (60000 Studs)']

games = ['Lego Star Wars: TCS ', 'Lego Batman ']

def start_processing():
    time.sleep(10)
    processcodes.process_codes(gamepad)

root = Tk()
sv_ttk.use_dark_theme()
root.geometry("500x400")
root.minsize(550, 300)

game = StringVar()
game.set(games[0])

options = Frame(root)
options.pack(side=LEFT, fill=BOTH, expand=True)
select_game = OptionMenu(options, game, games[0], *games)
select_game.config(width=len(max(games, key=len)))
select_game.pack(anchor=NW, padx=10, pady=10)
start_btn = Button(options, text="Start", command=start_processing)
start_btn.pack(anchor=SW, padx=10, pady=5)


    

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

codes = ScrollableFrame(root)
codes.pack(side=RIGHT, fill=BOTH, expand=True)
checkboxes = []
for index, item in enumerate(lego_star_wars_codes):
    checked = IntVar()
    checkboxes.append([checked])
    checkboxes[index].append(Checkbutton(codes.frame, text=item, variable=checkboxes[index][0]))
    checkboxes[index][0].set(1)
    checkboxes[index][1].pack(anchor=W)
    
root.after(20)
root.mainloop()