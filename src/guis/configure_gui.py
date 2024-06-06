import tkinter as tk
import os
import shelve
import time
from PIL import Image, ImageTk


def get_file(file_path):
    try:
        file = open(file_path, "r")
        text = file.read()
        text = text.strip()
        file.close()
        return text
    except UnicodeDecodeError:
        file = open(file_path, "r", encoding="utf-8")
        text = file.read()
        text = text.strip()
        file.close()
        return text


# todo player stats class
# todo player stats as a csv
food = 100
money = 1000
sanity = 75


class MainWindow:
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    stats = {"food": 100,
             "money": 0,
             "sanity": 0,
             "Inventory": {},
             "Planets Visited": {"Heaven's Forge": False, "Twilight Isles": False,
                                 "Acropolis": False, "Loamstone": False, "Ch'tak": False,
                                 "Valdsafar": False, "Titiana": False, "B-IRS": False},
             "Critical Events": {"Talashandra": False, "Talashandra 2": False,
                                 "Talashandra 3": False,
                                 "Gas-Beings": False, "Turtles": False}}
    x = (screen_width // 2) - (1000 // 2)

    def __init__(self):
        self.food_label = None
        self.money_label = None
        self.sanity_label = None
        self.bottom_bar = None
        self.start_menu_frame = None
        # self.root.resizable(width=False, height=False)
        self.game_shelve = None
        self.game_name_entry = None
        self.player_name_entry = None
        self.player_name = None
        self.game_name = None
        self.original_image = None
        self.picture_as_label = None
        self.starsailor_img = None
        self.starsailor_picture = None
        self.create_window()

    def create_window(self):
        self.root.geometry(f'1000x750+{self.x}+0')
        self.root.title("Starsailor")
        self.tool_bar_widgets()
        self.start_menu_frame = tk.Frame()

    def tool_bar_widgets(self):
        tool_bar = tk.Frame(self.root)
        tool_bar.columnconfigure(0, weight=2)
        tool_bar.columnconfigure(1, weight=1)
        tool_bar.columnconfigure(2, weight=1)
        tool_bar.columnconfigure(3, weight=1)
        tool_bar.columnconfigure(4, weight=2)

        banner = tk.Label(tool_bar, text="Starsailor", bg='#2E294E', font=("Times New Roman", 30), fg='#B0C4DE')
        banner.grid(row=0, column=1, columnspan=3, sticky=tk.N + tk.EW)

        menu_button = tk.Menubutton(tool_bar, text="Menu", font=("Times New Roman", 15), relief="raised", borderwidth=5,
                                    activebackground="#2E294E", bg="#B0C4DE",
                                    activeforeground="#B0C4DE")
        menu_button.grid(column=4, row=0, sticky=tk.NSEW)

        menu = tk.Menu(menu_button, tearoff=0, borderwidth=2)
        menu_button["menu"] = menu
        menu.add_command(label="Save Game", activebackground="#1F262A", command=self.save_game)
        menu.add_command(label="Restart Game", activebackground="#1F262A")
        menu.add_command(label="Load Game", activebackground="#1F262A")

        def show_help():
            help_window = tk.Tk()
            help_message = tk.Message(help_window, text=get_file("../storyline/setup/Setup and Help"), fg="black")
            help_message.pack()
            help_window.geometry(f'500x500+{75 + self.x}+0')

            def close_help():
                help_window.destroy()

            close_button = tk.Button(help_window, text="close", bg="red", command=close_help)
            close_button.pack(anchor=tk.SE, side=tk.BOTTOM)

        help_button = tk.Button(tool_bar, bitmap="question", activebackground="#1F262A", bg="#B0C4DE", relief="raised",
                                borderwidth=5, command=show_help)
        help_button.grid(column=0, row=0, sticky=tk.NSEW)

        inventory_button = tk.Button(tool_bar, text="Inventory", borderwidth=3, relief='raised', bg="#BC4842")
        inventory_button.grid(column=0, row=1, sticky=tk.N + tk.EW)

        self.food_label = tk.Button(tool_bar, text=f"Food: {self.stats['food']}", justify="center",
                                    background="#469BAB")
        self.food_label.grid(column=1, row=1, sticky=tk.NSEW)

        self.money_label = tk.Button(tool_bar, text=f"Money: {self.stats['money']}", justify="center",
                                     background="#469BAB")
        self.money_label.grid(column=2, row=1, sticky=tk.NSEW)

        self.sanity_label = tk.Button(tool_bar, text=f"Sanity: {self.stats['sanity']}", justify="center",
                                      background="#469BAB")
        self.sanity_label.grid(column=3, row=1, sticky=tk.NSEW)

        passenger_button = tk.Button(tool_bar, text="Passengers", borderwidth=3, relief='raised', bg="#BC4842")
        passenger_button.grid(column=4, row=1, sticky=tk.N + tk.EW)
        tool_bar.pack(fill="x")

        self.bottom_bar = tk.Frame(self.root)
        self.bottom_bar.columnconfigure(0, weight=1)
        self.bottom_bar.columnconfigure(1, weight=1)
        return_to_ship_button = tk.Button(self.bottom_bar, text="Return to Ship", height=8, bg="#BC4842")
        return_to_ship_button.grid(column=0, row=0, sticky=tk.NSEW)

        return_to_chtak_button = tk.Button(self.bottom_bar, text="Return to Ch'tak", height=8, bg="#B0C4DE",
                                           font=("Times New Roman", 10))
        return_to_chtak_button.grid(column=1, row=0, sticky=tk.NSEW)

        self.bottom_bar.pack(fill="x", side=tk.BOTTOM)

    def initialise_new_game(self):
        self.player_name = self.player_name_entry.get()
        self.game_name = self.game_name_entry.get()
        print(os.getcwd())
        if not os.getcwd().endswith("Saved States"):
            os.chdir("..\\tables\\Saved States")
        os.mkdir(self.game_name)
        time.sleep(.5)
        os.chdir(f"{self.game_name}")
        self.game_shelve = shelve.open(self.game_name)
        self.game_shelve["player name"] = self.player_name
        self.stats = {"food": 100,
                      "money": 1000,
                      "sanity": 80,
                      "Inventory": {},
                      "Planets Visited": {"Heaven's Forge": False, "Twilight Isles": False,
                                          "Acropolis": False, "Loamstone": False, "Ch'tak": False,
                                          "Valdsafar": False, "Titiana": False, "B-IRS": False},
                      "Critical Events": {"Talashandra": False, "Talashandra 2": False, "Talashandra 3": False,
                                          "Gas-Beings": False, "Turtles": False}}
        os.chdir("../")
        # todo investigate the shelving system
        self.sanity_label.update_idletasks()
        self.food_label.update_idletasks()
        self.money_label.update_idletasks()

    def save_game(self):
        self.game_shelve["stats"] = self.stats

    def load_game(self):
        pass

    def run_mainloop(self):
        self.root.mainloop()

    def resize_image(self, event):

        og_width, og_height = self.original_image.size
        aspect_ratio = og_width / og_height
        new_height = event.height
        new_width = event.width * (new_height / og_height)
        if (new_width / new_height) > aspect_ratio:
            new_width = int(new_height * aspect_ratio)
        else:
            new_height = int(new_width / aspect_ratio)
        resized_image = self.original_image.resize((new_width, new_height),
                                                   Image.Resampling.LANCZOS)
        self.starsailor_img = ImageTk.PhotoImage(resized_image)
        self.picture_as_label.config(image=self.starsailor_img)


def configure_frame_grid(frame, number_of_columns, number_of_rows):
    index = 0
    for column in range(number_of_columns):
        frame.columnconfigure(index, weight=1)
        index += 1

    index = 0
    for row in range(number_of_rows):
        frame.columnconfigure(index, weight=1)
        index += 1

    frame.pack(fill='x')


class StarsailorWindow(MainWindow):
    def __init__(self):
        super().__init__()
        self.heavens_forge_info_window = None
        self.heavens_forge_frame = None
        self.tunnel_frame = None
        self.new_game_frame = None
        self.walkthrough_frame = None
        self.intro_frame = None
        self.create_start_menu_frame()
        self.create_main_menu()

    def create_start_menu_frame(self):
        self.start_menu_frame = tk.Frame(self.root, background="#001E24")
        configure_frame_grid(self.start_menu_frame, 9, 9)

    def create_main_menu(self):
        new_game_button = tk.Button(self.start_menu_frame, text="New Game", command=self.create_new_game)
        new_game_button.grid(column=0, columnspan=10, row=0, rowspan=2, sticky=tk.NSEW)

        load_button = tk.Button(self.start_menu_frame, text="Load_Game")
        load_button.grid(column=0, columnspan=10, row=2, sticky=tk.NSEW)

        instructions_button = tk.Button(self.start_menu_frame, text="Instructions")
        instructions_button.grid(column=0, columnspan=10, row=3, sticky=tk.NSEW)

        help_button = tk.Button(self.start_menu_frame, text="Help")
        help_button.grid(column=0, columnspan=10, row=4, sticky=tk.NSEW)

        credits_button = tk.Button(self.start_menu_frame, text="Credits")
        credits_button.grid(column=0, columnspan=10, row=5, sticky=tk.NSEW)

        self.original_image = Image.open("../../pictures/coverphoto.gif")
        self.starsailor_img = self.original_image
        self.starsailor_picture = ImageTk.PhotoImage(self.starsailor_img)
        self.picture_as_label = tk.Label(self.start_menu_frame, image=self.starsailor_picture)
        self.picture_as_label.grid(column=10, row=0, rowspan=9, sticky=tk.NSEW)
        self.start_menu_frame.bind("<Configure>", self.resize_image)

    def create_new_game(self):
        self.start_menu_frame.destroy()
        self.new_game_frame = tk.Frame(self.root)
        self.new_game_frame.columnconfigure(0, weight=1)
        self.new_game_frame.columnconfigure(1, weight=1)
        self.new_game_frame.columnconfigure(2, weight=1)
        self.new_game_frame.columnconfigure(3, weight=1)
        self.new_game_frame.columnconfigure(4, weight=1)
        new_game_label = tk.Label(self.new_game_frame, text="New Game", background="#1F262A", foreground="#B0C4DE")
        new_game_label.grid(column=0, columnspan=5, row=0, sticky=tk.NSEW)
        player_name_entry_label = tk.Label(self.new_game_frame, text="Player Name")
        player_name_entry_label.grid(column=0, row=1)
        game_name_entry_label = tk.Label(self.new_game_frame, text="Game Name")
        game_name_entry_label.grid(column=0, row=2)
        self.player_name_entry = tk.Entry(self.new_game_frame)
        self.player_name_entry.grid(column=1, columnspan=3, row=1, sticky=tk.NSEW)
        self.game_name_entry = tk.Entry(self.new_game_frame)
        self.game_name_entry.grid(column=1, columnspan=3, row=2, sticky=tk.NSEW)
        save_nominal_data = tk.Button(self.new_game_frame, text="Save", bg='green', command=self.initialise_new_game)
        # todo need some validation to make sure this has not been already used, and it works as a folder name
        save_nominal_data.grid(column=2, row=4, sticky=tk.NSEW)
        start_game = tk.Button(self.new_game_frame, text="START", bg="red", command=self.create_walkthrough)
        start_game.grid(column=2, row=5)
        self.new_game_frame.pack(fill="x")

    class TempWindow:
        def __init__(self):
            super().__init__()
            self.window = None
            self.text = None
            self.window_height = MainWindow.screen_height

        def create_window(self, text):
            self.text = text
            self.window = tk.Tk()
            self.window.geometry(f'500x900')
            self.center_window()
            message = tk.Message(self.window, text=self.text)
            message.pack(fill="x")

        def destroy_window(self):
            self.window.destroy()

        def center_window(self):
            self.window.update_idletasks()
            width = self.window.winfo_width()
            frm_width = self.window.winfo_rootx() - self.window.winfo_x()
            win_width = width + 2 * frm_width
            x = (self.window.winfo_screenwidth() // 2) - (win_width // 2)
            y = 0
            self.window.geometry(f'{width}x{700}+{x}+{y}')

    def create_walkthrough_frame(self):
        self.new_game_frame.destroy()
        self.walkthrough_frame = tk.Frame(self.root)
        configure_frame_grid(self.walkthrough_frame, 3, 3)

    def create_walkthrough(self):
        self.create_walkthrough_frame()
        heading = tk.Label(self.walkthrough_frame, text="A quick walkthrough on how to play.")
        heading.grid(row=0, column=0, columnspan=3)

        button1 = tk.Button(self.walkthrough_frame, text="button1")
        button1.grid(row=1, column=0)

        button2 = tk.Button(self.walkthrough_frame, text="button2")
        button2.grid(row=1, column=1)

        button3 = tk.Button(self.walkthrough_frame, text="button3")
        button3.grid(row=1, column=2)

        button4 = tk.Button(self.walkthrough_frame, text="button4")
        button4.grid(row=1, column=3)

        button5 = tk.Button(self.walkthrough_frame, text="button5")
        button5.grid(row=2, column=0)

        button6 = tk.Button(self.walkthrough_frame, text="button6")
        button6.grid(row=2, column=1)

        button6 = tk.Button(self.walkthrough_frame, text="button7")
        button6.grid(row=2, column=2)

        button6 = tk.Button(self.walkthrough_frame, text="button8")
        button6.grid(row=2, column=3)

        button6 = tk.Button(self.walkthrough_frame, text="button9")
        button6.grid(row=3, column=0)

        continue_button = tk.Button(self.walkthrough_frame, text="Continue", bg="green", command=self.create_tunnel)
        continue_button.grid(row=4, column=5)

    def create_tunnel_frame(self):
        self.walkthrough_frame.destroy()
        self.tunnel_frame = tk.Frame(self.root)
        configure_frame_grid(self.tunnel_frame, 1, 4)

    def create_tunnel(self):
        self.create_tunnel_frame()
        # todo make this not an absolute mess

        continue_button = tk.Button(self.tunnel_frame, text="Continue", command=self.create_heavens_forge)
        continue_button.grid(row=4)

    def create_heavens_forge_frame(self):
        self.tunnel_frame.destroy()
        self.heavens_forge_frame = tk.Frame(self.root)
        configure_frame_grid(self.heavens_forge_frame, 4, 4)

    def create_heavens_forge(self):
        self.create_heavens_forge_frame()
        info_button = tk.Button(self.heavens_forge_frame, text="Info", bg="green",
                                command=self.create_heavens_forge_info_window)
        info_button.grid(row=1, column=0, sticky=tk.NSEW)

    def create_heavens_forge_info_window(self):
        text = """
A rich orange sun bobs upon a starry sea of violet, flanked by the remnants of an abandoned dyson sphere. An edifice of
ancient and ingenious artifice, the crumbling construct cast a shadow upon the star's light that allows for safe
approach. Thirteen ringed mirrors of burnished gold encircle the sun, a clockwork cage of gilded glass drinking up the
bronze, buttery glow. Even though the incomplete structure covers only a quarter of the star, this station produces an
endless supply of coveted hardlight.

This rare resource is treasured universally for its lightweight durability and
flexibility, particularly for building spacefaring vessels. The Shipyards of Heaven's Forge are renowned among all the
Seven Suns, and it is held in belief that this place was the beginning of Captain Kip's legendary voyage. It has since
become a point of pilgrimage for both builders and explorers.

Diligent robots attend to the foundry floor before you.\n"""
        self.heavens_forge_info_window = self.TempWindow()
        self.heavens_forge_info_window.create_window(text)
        continue_button = tk.Button(self.heavens_forge_info_window.window, text="Close", bg="red",
                                    command=self.destroy_heavens_forge_info_window)
        continue_button.pack(side="bottom")

    def destroy_heavens_forge_info_window(self):
        self.heavens_forge_info_window.destroy_window()


if __name__ == "__main__":
    main_window = StarsailorWindow()
    main_window.run_mainloop()
