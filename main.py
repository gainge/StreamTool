# Helpful Links
# https://stackoverflow.com/questions/6548837/how-do-i-get-an-event-callback-when-a-tkinter-entry-widget-is-modified

# Methods #







'''
---------------------
-  Main Code Start  -
---------------------
'''

import configuration as config


def config_testing():
    my_config = config.Configuration()

    print(my_config.game_name)
    print(my_config.__doc__)

    print("\n\n")

    my_config.x = 0

    for i in range(10):
        my_config.x = my_config.x + 1

    print(str(my_config.x))

    del my_config.x


# Let's try messing with some cool tkinter things


def setup_gui(root):
    # Do some setup stuff
    print('stub')

def update_character_previews(a, b, c):
    global p1_char_label
    global p2_char_label

    # Remove our widgets from the grid
    p1_char_label.grid_forget()
    p2_char_label.grid_forget()

    # Recreate them I guess, because I don't really know how to get them to persist after root.update()
    load = Image.open(os.path.join(IMG_PATH, 'config_1', 'stock_icons', icons_dict[p1_char.get()]))
    photo = ImageTk.PhotoImage(load)
    p1_char_label = tk.Label(header_frame, image=photo)
    p1_char_label.image = photo
    p1_char_label.grid(row=3, column=0)

    load = Image.open(os.path.join(IMG_PATH, 'config_1', 'stock_icons', icons_dict[p2_char.get()]))
    photo = ImageTk.PhotoImage(load)
    p2_char_label = tk.Label(header_frame, image=photo)
    p2_char_label.image = photo
    p2_char_label.grid(row=3, column=2)

    # Force update
    # root.update()

def potential_change(obj):
    update_button.config(fg='red')
    root.update()

def bind_changed(widgets):
    for i in range(len(widgets)):
        widgets[i].bind('<Key>', potential_change)
        widgets[i].bind('<Button-1>', potential_change)


def save_game_state():
    # Clear the button background
    # Crap I can't figure out how

    print('saving the game state!')
    import os
    import shutil

    dir = os.getcwd()

    # Write stuff really sloppily
    with open(os.path.join(dir, OUT_FILE_PREFIX, _config.p1_tag_outfile), 'w') as out:
        out.write(p1_tag.get())
    with open(os.path.join(dir, OUT_FILE_PREFIX, _config.p2_tag_outfile), 'w') as out:
        out.write(p2_tag.get())
    with open(os.path.join(dir, OUT_FILE_PREFIX, _config.p1_games_outfile), 'w') as out:
        out.write(p1_games.get())
    with open(os.path.join(dir, OUT_FILE_PREFIX, _config.p2_games_outfile), 'w') as out:
        out.write(p2_games.get())

    # Construct the image paths
    p1_source = os.path.join(dir, IMG_PATH, 'config_1', 'p1_chars', p1_chars_dict[p1_char.get()])
    p2_source = os.path.join(dir, IMG_PATH, 'config_1', 'p2_chars', p2_chars_dict[p2_char.get()])
    p1_out = os.path.join(dir, OUT_FILE_PREFIX, 'p1_char.png')
    p2_out = os.path.join(dir, OUT_FILE_PREFIX, 'p2_char.png')
    # Copy the images
    shutil.copy(p1_source, p1_out)
    shutil.copy(p2_source, p2_out)

    update_button.config(fg='black')
    root.update()
    print('Finished!!')


import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
import os

import configuration as cfig



# CONSTANTS #
ROOT_WIDTH = 800
ROOT_HEIGHT = 350

OUT_FILE_PREFIX = os.path.join('output', 'main_out')
IMG_PATH = os.path.join('res', 'img')



# Let's define some variables to hold our game values
# Or... Maybe let's do that later?
# Let's just make a default config right now
_config = cfig.Configuration() # We'll just use the default values for now
input_widgets = []


root = tk.Tk()

# Let's try to get a barebones gui out there in the world

# Initialize the size of the window!
geometry = "{}x{}+{}+{}".format(ROOT_WIDTH, ROOT_HEIGHT, 0, 0)
root.geometry(geometry)

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=1)
# configure the grid so that our main frame is centered
# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)


# Let's make the banner!
banner_frame = tk.Frame(main_frame, pady=20)
banner_frame.pack()

# Create the banner!
load = Image.open(os.path.join(IMG_PATH, 'application', 'BYU_Melee_Logo.png'))
photo = ImageTk.PhotoImage(load)

banner_label = tk.Label(banner_frame, image=photo)
banner_label.image = photo
banner_label.pack()


# Create a grid for the labels and text fields
header_frame = tk.Frame(main_frame)
header_frame.pack()


# Populate our grid with items #
# ---------------------------- #
# Add our player tag labels
p1_label = tk.Label(header_frame, text='Player 1 Tag', fg='white', bg='#002255')
p2_label = tk.Label(header_frame, text='Player 2 Tag', fg='white', bg='#002255')

vs_label = tk.Label(header_frame, text=' vs ', fg='black', bg='#aca7a9')

# Entry fields for player tags
p1_tag = tk.Entry(header_frame)
p1_tag.insert(tk.END, 'p1')
p2_tag = tk.Entry(header_frame)
p2_tag.insert(tk.END, 'p2')


# Let's do an OptionMenu instaead of spinboxes
# This is going to be gross and hard-coded for now
p1_chars_dict = {
        "Bowser": "bowser_L.png",
        "Donkey Kong": "dk_L.png",
        "Dr. Mario": "doc_L.png",
        "Falco": "falco_L.png",
        "Falcon": "falcon_L.png",
        "Fox": "fox_L.png",
        "Ganon": "ganon_L.png",
        "Mr. Game and Watch": "gnw_L.png",
        "Ice Climbers": "ics_L.png",
        "Kirby": "kirby_L.png",
        "Link": "link_L.png",
        "Luigi": "luigi_L.png",
        "Mario": "mario_L.png",
        "Marth": "marth_L.png",
        "Mewtwo": "mewtwo_L.png",
        "Ness": "ness_L.png",
        "Peach": "peach_L.png",
        "Pichu": "pichu_L.png",
        "Pikachu": "pikachu_L.png",
        "Puff": "puff_L.png",
        "Roy": "roy_L.png",
        "Samus": "samus_L.png",
        "Sheik": "sheik_L.png",
        "Young Link": "ylink_L.png",
        "Yoshi": "yoshi_L.png",
        "Zelda": "zelda_L.png"
        }

p2_chars_dict = {
        "Bowser": "bowser_R.png",
        "Donkey Kong": "dk_R.png",
        "Dr. Mario": "doc_R.png",
        "Falco": "falco_R.png",
        "Falcon": "falcon_R.png",
        "Fox": "fox_R.png",
        "Ganon": "ganon_R.png",
        "Mr. Game and Watch": "gnw_R.png",
        "Ice Climbers": "ics_R.png",
        "Kirby": "kirby_R.png",
        "Link": "link_R.png",
        "Luigi": "luigi_R.png",
        "Mario": "mario_R.png",
        "Marth": "marth_R.png",
        "Mewtwo": "mewtwo_R.png",
        "Ness": "ness_R.png",
        "Peach": "peach_R.png",
        "Pichu": "pichu_R.png",
        "Pikachu": "pikachu_R.png",
        "Puff": "puff_R.png",
        "Roy": "roy_R.png",
        "Samus": "samus_R.png",
        "Sheik": "sheik_R.png",
        "Young Link": "ylink_R.png",
        "Yoshi": "yoshi_R.png",
        "Zelda": "zelda_R.png"
        }

icons_dict = {
        "Bowser": "BowserOriginal.png",
        "Donkey Kong": "DonkeyKongOriginal.png",
        "Dr. Mario": "DrMarioBlack.png",
        "Falco": "FalcoOriginal.png",
        "Falcon": "CaptainFalconOriginal.png",
        "Fox": "FoxOriginal.png",
        "Ganon": "GanondorfOriginal.png",
        "Mr. Game and Watch": "Game & Watch Original.png",
        "Ice Climbers": "IceClimbersOriginal.png",
        "Kirby": "KirbyOriginal.png",
        "Link": "LinkGreen.png",
        "Luigi": "LuigiOriginal.png",
        "Mario": "MarioOriginal.png",
        "Marth": "MarthOriginal.png",
        "Mewtwo": "MewtwoOriginal.png",
        "Ness": "NessOriginal.png",
        "Peach": "PeachOriginal.png",
        "Pichu": "PichuOriginal.png",
        "Pikachu": "PikachuOriginal.png",
        "Puff": "JigglyPuffOriginal.png",
        "Roy": "RoyOriginal.png",
        "Samus": "SamusOriginal.png",
        "Sheik": "SheikOriginal.png",
        "Young Link": "YoungLinkGreen.png",
        "Yoshi": "YoshiOriginal.png",
        "Zelda": "ZeldaOriginal.png"
        }


p1_chars = list(p1_chars_dict.keys())

p1_char = tk.StringVar(header_frame)
p1_char.set(p1_chars[0])
p1_char.trace('w', update_character_previews)
# TODO add trace here and on p2

p1_char_select = tk.OptionMenu(header_frame, p1_char, *tuple(p1_chars))

p2_chars = list(p2_chars_dict.keys())


p2_char = tk.StringVar(header_frame)
p2_char.set(p2_chars[0])
p2_char.trace('w', update_character_previews)


p2_char_select = tk.OptionMenu(header_frame, p2_char, *tuple(p2_chars))



# Let's also have like, an image preview ready for this ish
load = Image.open(os.path.join(IMG_PATH, 'config_1', 'stock_icons', icons_dict[p1_chars[0]]))
photo = ImageTk.PhotoImage(load)
p1_char_label = tk.Label(header_frame, image=photo)
p1_char_label.image = photo

p2_char_label = tk.Label(header_frame, image=photo)
p2_char_label.image = photo


# Spinboxes!
p1_games = tk.Spinbox(header_frame, from_=0, to=9, width=5,
                      font=Font(family='Helvetica', size=13, weight='bold'))
p2_games = tk.Spinbox(header_frame, from_=0, to=9, width=5,
                      font=Font(family='Helvetica', size=13, weight='bold'))

# The big kahuna button
update_button = tk.Button(header_frame, command=save_game_state, text='Update!')



# Bind our widgets to the changed listener
input_widgets.append(p1_tag)
input_widgets.append(p2_tag)
input_widgets.append(p1_games)
input_widgets.append(p2_games)
input_widgets.append(p1_char_select)
input_widgets.append(p2_char_select)

bind_changed(input_widgets)

# Grid everything up!
p1_label.grid(row=0, column=0)
p2_label.grid(row=0, column=2)

vs_label.grid(row=1, column=1)


p1_tag.grid(row=1, column=0)
p2_tag.grid(row=1, column=2)

# p1_games.grid(row=2, column=0)
p1_char_select.grid(row=2, column=0)
# p2_games.grid(row=2, column=2)
p2_char_select.grid(row=2, column=2)


p1_char_label.grid(row=3, column=0)
p2_char_label.grid(row=3, column=2)


update_button.grid(row=3, column=1)


# Display the window
root.mainloop()


