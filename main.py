import converter
import textwrap as tw

morse_converter = converter.MorseConverter()

title_text = tw.dedent(f"""
    {50 * '*'}
    Morse Converter
    {50 * '*'}""")

welcome_text = tw.dedent(f"""
    You may convert your sentence to morse code or vice versa.
    Press any other key to exit the tool.
    Kindly choose an option below (A or B). 
    A: Convert Text to Morse Code.
    B: Convert Morse Code to Text.
    
    Enter your option: """)

running = True

if __name__ == '__main__':
    """
    Command-line tool to convert morse to text and vice versa.
    """
    while running:
        print(title_text)
        while True:
            user_input = input(welcome_text)
            if user_input.upper() == "A":
                morse_converter.read_text()
                morse_converter.convert_to_morse()
                morse_converter.play_morse_sound()
            elif user_input.upper() == "B":
                morse_converter.read_morse()
                morse_converter.convert_to_text()
            else:
                running = False
                break

    print(f"\nThanks for using this tool.\n{50 * '*'}")
