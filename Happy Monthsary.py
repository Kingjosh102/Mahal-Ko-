import time
import os

def print_heart_with_message():
    heart = [
        "       *****       *****       ",
        "    ***********************    ",
        "  ***************************  ",
        " ***************************** ",
        " ***************************** ",
        "  ***************************  ",
        "   *************************   ",
        "    ***********************    ",
        "      *******************      ",
        "        ***************        ",
        "          ***********          ",
        "            *******            ",
        "              ***              ",
        "               *               ",
    ]
    
    man_and_woman = [
        "    O   O    ",
        "   /|\\ /|\\  ",
        "   / \\ / \\  ",
        "  (   ) (   )",
    ]

    flower = [
        "      @     ",
        "     /|\\   ",
        "    / | \\  ",
        "     / \\   ",
        "    (   )  "
    ]

    message = "Happy Monthsary, mahal ko. I love you so much."
    kiss = "    *\n   * *\n  *   *\n *     *\n*******\n  ***\n   *"

    colors = [
        "\033[91m",  # Red
        "\033[95m",  # Magenta
        "\033[94m",  # Blue
        "\033[96m",  # Cyan
        "\033[92m",  # Green
        "\033[93m",  # Yellow
    ]

    try:
        while True:
            for color in colors:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(color)
                
                # Center the heart
                for line in heart:
                    print(" " * 20 + line)

                # Print the message below the heart
                print("\n" + " " * 15 + message)
                
                # Print the man and woman with a flower in the middle
                for i in range(len(man_and_woman)):
                    print(" " * 20 + man_and_woman[i] + "   " + flower[i])

                # Simulate a flying kiss
                print("\n" + " " * 35 + kiss)
                
                time.sleep(1)
        print("\033[0m")  # Reset color

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[0m")  # Reset color
        print("Goodbye!")

# Run the function
print_heart_with_message()
