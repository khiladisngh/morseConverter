import time
import winsound


def play_morse_sound(morse):
    """
    Plays morse sound to the user.
    """
    for code in morse:
        if code == ".":
            winsound.Beep(frequency=700, duration=100)
        if code == "-":
            winsound.Beep(frequency=700, duration=400)
        if code == " ":
            time.sleep(0.2)
