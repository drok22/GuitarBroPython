from tkinter import *
from tkinter import ttk
from constants import *

#------------------------------------------------------------
#
#------------------------------------------------------------
class GuitarBroView():
    def __init__(self):
        self.window = Tk()
        self.window.title("GuitarBro: Python Edition")
        self.window.config(padx=WINDOW_PAD_X, pady=WINDOW_PAD_X, bg="black")

        self.canvas = Canvas(width=CANVAS_SIZE_X, height=CANVAS_SIZE_Y, bg="black", highlightthickness=0)

        # need to get a fretboard image that will work.. or maybe draw it somehow?
        '''
        fretboard_image = PhotoImage(file="images/fretboard.png")
        #self.canvas.create_image(0,0, image=FRETBOARD_IMG)
        '''

        self.key_label = Label(text="Key", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.tuning_label = Label(text="Tuning", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.key_display_label = Label(text="E Minor", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.number_of_strings_label = Label(text="Number of Strings", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

        self.key_box = ttk.Combobox(self.window, width=21, textvariable=StringVar)
        self.major_minor_box = ttk.Combobox(self.window, width=21, textvariable=StringVar)
        self.tuning_box = ttk.Combobox(self.window, width=21, textvariable=StringVar)
        self.tuning_type_box = ttk.Combobox(self.window, width=21, textvariable=StringVar)
        self.number_of_strings_box = ttk.Combobox(self.window, width=21, textvariable=StringVar)
        self.scale_pattern_display_label = Label(text="EF#GABCD", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

        self.scale_label = Label(text="Scale", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.fretboard_display_type_label = Label(text="Display Frets As", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.guitar_tuning_display_label = Label(text="Tune Guitar To...", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

        self.scale_box = ttk.Combobox(self.window, width=21, textvariable=StringVar)
        self.fretboard_display_type_box = ttk.Combobox(self.window, width=21, textvariable=StringVar)
        self.string_tuning_display_label = Label(text="EADGBE", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.save_to_csv_button = Button(text="Save to CSV", command=self.save_to_csv, highlightthickness=0)

        self.setup_ui()        
    
    #------------------------------------------------------------
    #
    #------------------------------------------------------------
    def setup_ui(self):
        # Grid Setup
        # Row 0
        self.key_label.grid(row=0, column=0, sticky=W)
        self.tuning_label.grid(row=0, column=2, sticky=W)
        self.key_display_label.grid(row=0, column=5, sticky=W)
        # Row 1
        self.key_box.grid(row=1, column=0, sticky=W)
        self.major_minor_box.grid(row=1, column=1, sticky=W)
        self.tuning_box.grid(row=1, column=2, sticky=W)
        self.tuning_type_box.grid(row=1, column=3, sticky=W)
        self.scale_pattern_display_label.grid(row=1, column=5, sticky=W)
        # Row 2
        self.number_of_strings_label.grid(row=2, column=0, sticky=W)
        self.scale_label.grid(row=2, column=1, sticky=W)
        self.fretboard_display_type_label.grid(row=2, column=2, sticky=W)
        self.guitar_tuning_display_label.grid(row=2, column=5, sticky=W)
        # Row 3
        self.number_of_strings_box.grid(row=3, column=0, sticky=W)
        self.scale_box.grid(row=3, column=1, sticky=W)
        self.fretboard_display_type_box.grid(row=3, column=2, sticky=W)
        self.string_tuning_display_label.grid(row=3, column=5, sticky=W)
        self.save_to_csv_button.grid(row=3, column=6, sticky=W)
        # Row 4
        #self.fretboard.grid(row=4, column=0, columnspan=5)

        # Combo Boxes setup
        self.key_box['values'] = ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#")
        self.major_minor_box['values'] = ("Minor", "Major")
        self.tuning_box['values'] = ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#")
        self.tuning_type_box['values'] = ("Standard", "Drop", "Open")
        self.number_of_strings_box['values'] = ("4", "5", "6", "7", "8")
        self.scale_box['values'] = ("Minor", "Major", "Pentatonic", "Blues")
        self.fretboard_display_type_box['values'] = ("Dots", "Fret Number")

        self.window.mainloop()
    #------------------------------------------------------------
    #
    #------------------------------------------------------------
    def restring_guitar():
        pass
    #------------------------------------------------------------
    #
    #------------------------------------------------------------
    def finger_notes():
        pass
    #------------------------------------------------------------
    #
    #------------------------------------------------------------
    def save_to_csv():
        pass