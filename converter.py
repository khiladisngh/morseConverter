import json
import time
import winsound
import textwrap as tw


class MorseConverter:
    """
    Converts morse code to text and vice-versa.
    It even plays the sound of morse.
    """
    def __init__(self):
        self.text = None
        self.morse = None
        self.morse_dictionary = None

        self.read_morse_codes()

    def read_morse_codes(self):
        """
        Read codes from the json file.
        """
        with open("morse_dictionary.json") as f:
            self.morse_dictionary = json.load(f)

    def read_text(self):
        """
        Read text input from the user.
        """
        self.text = input(tw.dedent("""
        Enter text to convert:
        > """))

    def read_morse(self):
        """
        Read morse input from the user.
        """
        self.morse = input(tw.dedent("""
        Enter morse code to convert:
        > Leave 1 space between letters.
        > Leave 5 spaces between words.
        > """))

    def convert_to_morse(self):
        """
        Converts text input to morse code and display it to the user.
        """
        self.morse = ""
        for char in self.text:
            if char.upper() in self.morse_dictionary:
                self.morse += f"{self.morse_dictionary[char.upper()]} "

        print(f"\nMorse code version: \n{self.morse}")

    def convert_to_text(self):
        """
        Converts morse input to text and display it to the user.
        """
        self.text = ""
        morse_words = self.morse.split("    ")
        for word in morse_words:
            morse_letters = word.split(" ")
            for morse_letter in morse_letters:
                for letter, code in self.morse_dictionary.items():
                    if code == morse_letter:
                        self.text += letter
            self.text += " "

        print(f"\nText version: \n{self.text}")

    def play_morse_sound(self):
        """
        Plays morse sound to the user.
        """
        for code in self.morse:
            if code == ".":
                winsound.Beep(frequency=700, duration=100)
            if code == "-":
                winsound.Beep(frequency=700, duration=400)
            if code == " ":
                time.sleep(0.2)

