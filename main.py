from datetime import datetime
import time

DIGITS = {
    '0': ['#####','#   #','#   #','#   #','#####'],
    '1': ['  #  ',' ##  ','  #  ','  #  ','#####'],
    '2': ['#####','    #','#####','#    ','#####'],
    '3': ['#####','    #','#####','    #','#####'],
    '4': ['#   #','#   #','#####','    #','    #'],
    '5': ['#####','#    ','#####','    #','#####'],
    '6': ['#####','#    ','#####','#   #','#####'],
    '7': ['#####','    #','    #','    #','    #'],
    '8': ['#####','#   #','#####','#   #','#####'],
    '9': ['#####','#   #','#####','    #','    #'],
    ':': ['     ','  #  ','     ','  #  ','     ']
}

def convert_to_number_art(text: str):
    rows = ["\t"] * 5
    for char in text:
        pattern = DIGITS.get(char, ['?????']*5)
        for i in range(5):
            rows[i] += pattern[i] + '  '
    clear_terminal()
    return "\n".join(rows)

def clear_terminal():
     print("\033c",end="")

def main():
    while True:
        stamp = datetime.now().strftime("%H:%M:%S")
        art = convert_to_number_art(stamp)
        print(art)
        time.sleep(1)


if __name__ == "__main__":
    main()
