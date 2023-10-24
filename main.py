# Morse Code Convertor
# Converts a text input to morse code, with text and audio output

# Import statements
from pydub import AudioSegment
from pydub.playback import play
from time import sleep

# Dictionary maps characters to morse code
MORSE_DICT = {
    'A': '•—', 'B': '—•••', 'C': '—•—•', 'D': '—••', 'E': '•', 'F': '••—•', 'G': '——•', 'H': '••••', 'I': '••',
    'J': '•———', 'K': '—•—', 'L': '•—••', 'M': '——', 'N': '—•', 'O': '———', 'P': '•——•', 'Q': '——•—', 'R': '•—•',
    'S': '•••', 'T': '—', 'U': '••—', 'V': '•••—', 'W': '•——', 'X': '—••—', 'Y': '—•——', 'Z': '——••',

    '0': '———•••', '1': '•———••', '2': '••——••', '3': '•••——•', '4': '••••—•', '5': '•••••',
    '6': '—••••', '7': '——••••', '8': '———•••', '9': '————••',

    " ": " "
}

# Audio file paths
DOT = AudioSegment.from_wav("MorseAudio/Dot.wav")
DASH = AudioSegment.from_wav("MorseAudio/Dash.wav")

plain_str = input("Enter a string:\n")
morse_str = ""

# Text conversion
for char in plain_str.upper():
    if char in MORSE_DICT:
        morse_str += MORSE_DICT[char] + "   "

morse_str = morse_str.strip()  # Remove additional whitespace
print(morse_str)

# Plays audio
for char in morse_str:
    if char == "•":
        play(DOT)
        sleep(0.1)
    elif char == "—":
        play(DASH)
        sleep(0.3)
    elif char == " ":
        sleep(0.3)
