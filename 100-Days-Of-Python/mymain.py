import time
import os
import math

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

rose_frames = [
"""
        ,--./,-.
       / #      \\
      |           |
       \\  __   /
    .--./ /  \\.--.
   /  /  | o  |  \\
  |  |   |    |  |
   \\  \\       /  /
    `--`\\   /`--`
         \\_/
          |
          |
          |
     ~~~~~|~~~~~
""",
"""
         ,-./,-.
        / ##     \\
       |    *     |
        \\ __    /
     .--./ /  \\.--.
    /  /  |    |  \\
   |  |   |    |  |
    \\  \\       /  /
     `--`\\   /`--`
          \\_/
           |
           |
           |
      ~~~~~|~~~~~
""",
"""
        ,--./,-.
       / ###     \\
      |   ***     |
       \\ ___    /
    .--./ /  \\.--.
   /  /  |    |  \\
  |  |   |    |  |
   \\  \\       /  /
    `--`\\   /`--`
         \\_/
          |
          |
          |
     ~~~~~|~~~~~
"""
]

big_rose = """
                             _
                           _(_)_                          wWWWw   _
               @@@@       (_)@(_)   vVVVv     _     @@@@  (___) _(_)_
              @@()@@ wWWWw  (_)\\    (___)  _(_)_  @@()@@   Y  (_)@(_)
               @@@@  (___)     `|/    Y   (_)@(_)  @@@@   \\|/   (_)\\
                /      Y       \\|    \\|/   /(_)    \\|      |/      |
             \\ |      \\|/      | /  \\  | /  |      |/    \\|      \\|/
             \\\\|//   \\\\|///  \\\\|//  \\\\|//   |//  \\\\|///  \\\\|//  \\\\|//
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

lyrics = [
    "तुम दिल की धड़कन में रहते हो, रहते हो...",
    "मेरी इन साँसों से कहते हो, कहते हो...",
    "बाहों में आ जाओ, सपनों में खो जाओ...",
    "तुम दिल की धड़कन में रहते हो, रहते हो...",
]

messages = [
    "  💻  Anu, you are my favorite function()  💻",
    "  ❤️   My heart runs an infinite loop for you  ❤️ ",
    "  🌹  This rose has no bugs — just like you  🌹 ",
    "  💕  while(alive): love(Anu)  💕",
]

colors = {
    'red'    : '\033[91m',
    'green'  : '\033[92m',
    'yellow' : '\033[93m',
    'pink'   : '\033[95m',
    'cyan'   : '\033[96m',
    'white'  : '\033[97m',
    'reset'  : '\033[0m',
    'bold'   : '\033[1m',
}

def colored(text, color):
    return f"{colors.get(color,'')}{text}{colors['reset']}"

def center(text, width=70):
    return text.center(width)

def draw_rose(frame, tick):
    c = colors
    rose = rose_frames[frame % len(rose_frames)]
    lines = rose.split('\n')
    result = []
    for line in lines:
        colored_line = (
            line
            .replace('@', c['red'] + '@' + c['reset'])
            .replace('#', c['red'] + '#' + c['reset'])
            .replace('*', c['yellow'] + '*' + c['reset'])
            .replace('|', c['green'] + '|' + c['reset'])
            .replace('~', c['green'] + '~' + c['reset'])
            .replace('_', c['green'] + '_' + c['reset'])
        )
        result.append(center(colored_line))
    return '\n'.join(result)

def heart_beat(tick):
    beats = ['♥', '❤', '♥', '❤']
    h = beats[tick % len(beats)]
    size = ['  ', '   ', '    ', '   '][tick % 4]
    return colored(f"{size}{h}  Anu  {h}{size}", 'red')

def run():
    tick = 0
    lyric_idx = 0
    msg_idx = 0

    print(colored("\n  🌹 Compiling love.py ...", 'pink'))
    time.sleep(0.5)
    print(colored("  ✓  No errors found", 'green'))
    time.sleep(0.4)
    print(colored("  ▶  Running rose_for_anu.py ...\n", 'cyan'))
    time.sleep(0.8)

    while True:
        clear()

        print()
        print(colored(center("🌹  R O S E   F O R   A N U  🌹"), 'red') + colors['bold'])
        print(colored(center("─" * 50), 'pink'))
        print()

        print(draw_rose(tick, tick))

        print()
        print(colored(center(heart_beat(tick)), 'red'))
        print()

        print(colored(center("─" * 50), 'pink'))

        lyric = lyrics[lyric_idx % len(lyrics)]
        print(colored(center(lyric), 'yellow'))
        print()

        msg = messages[msg_idx % len(messages)]
        print(colored(center(msg), 'cyan'))

        print()
        print(colored(center("─" * 50), 'pink'))
        print(colored(center("[ Press Ctrl+C to stop — but love never stops ]"), 'pink'))

        tick += 1
        if tick % 3 == 0:
            lyric_idx += 1
        if tick % 5 == 0:
            msg_idx += 1

        time.sleep(0.4)

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        clear()
        print()
        print(colored(center("🌹  Thank you, Anu  🌹"), 'red'))
        print(colored(center("तुम दिल की धड़कन में रहते हो..."), 'yellow'))
        print(colored(center("while(alive): love(Anu)  ❤️"), 'cyan'))
        print()