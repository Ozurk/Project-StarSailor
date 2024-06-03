import tkinter as tk
import configure_gui as main
from PIL import Image, ImageTk


class Starsailor(main.MainWindow):
    def __init__(self):
        super().__init__()
        self.heavens_forge_frame = None
        self.tunnel_frame = None
        self.new_game_frame = None
        self.walkthrough_frame = None
        self.intro_frame = None
        self.create_start_menu_frame()
        self.create_main_menu()

    def configure_frame_grid(self, frame, number_of_columns, number_of_rows):
        index = 0
        for column in range(number_of_columns):
            frame.columnconfigure(index, weight=1)
            index += 1

        index = 0
        for row in range(number_of_rows):
            frame.columnconfigure(index, weight=1)
            index += 1

        frame.pack(fill='x')

    def create_start_menu_frame(self):
        self.start_menu_frame = tk.Frame(self.root, background="#001E24")
        self.configure_frame_grid(self.start_menu_frame, 9, 9)

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

    def create_walkthrough_frame(self):
        self.new_game_frame.destroy()
        self.walkthrough_frame = tk.Frame(self.root)
        self.configure_frame_grid(self.walkthrough_frame, 3, 3)

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
        button6.grid(row=2, column=4)

        continue_button = tk.Button(self.walkthrough_frame, text="Continue", bg="green", command=self.create_tunnel)
        continue_button.grid(row=3, column=4)

    def create_tunnel_frame(self):
        self.walkthrough_frame.destroy()
        self.tunnel_frame = tk.Frame(self.root)
        self.configure_frame_grid(self.tunnel_frame, 1, 4)

    def create_tunnel(self):
        self.create_tunnel_frame()
        # todo make this not an absolute mess

        continue_button = tk.Button(self.tunnel_frame, text="Continue", command=self.create_heavens_forge)
        continue_button.grid(row=4)

    def create_heavens_forge_frame(self):
        self.tunnel_frame.destroy()
        self.heavens_forge_frame = tk.Frame(self.root)
        self.configure_frame_grid(self.heavens_forge_frame, 1, 4)

    def create_heavens_forge(self):
        self.create_heavens_forge_frame()
        # todo make this not an absolute mess
        heavens_forge_text = tk.Text(self.heavens_forge_frame, height=200, width=200)
        heavens_forge_text.grid(row=3)
        heavens_forge_text.insert(tk.END, "A rich orange sun bobs upon a starry sea of violet, flanked by the "
                                          "remnants of an"
                                  "abandoned dyson sphere. An edifice of ancient and ingenious artifice, the crumbling"
                                  "construct cast a shadow upon the star's light that allows for safe approach. Thirtee"
                                  "n ringed mirrors of burnished gold encircle the sun, a clockwork cage of gilded "
                                          "glass"
                                  " drinking up the bronze, buttery glow. Even though the incomplete structure covers"
                                  " only a quarter of the star, this station produces an endless supply of coveted har"
                                  "dlight. This rare resource is treasured universally for its lightweight durability "
                                  "andflexibility, particularly for building spacefaring vessels. The Shipyards of "
                                  "Heaven's Forge are renowned among all theSeven Suns, and it is held in belief that "
                                  "this place was the beginning of Captain Kip's legendary voyage. It has since become"
                                  "a point of pilgrimage for both builders and explorers.\n\nDiligent robots attend to"
                                  "the foundry floor before you.")

        continue_button = tk.Button(self.heavens_forge_frame, text="Continue")
        continue_button.grid(row=4)


test = Starsailor()
test.run_mainloop()
print(test.game_name, test.player_name)
