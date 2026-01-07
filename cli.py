# Digit of life - Həyat rəqəmi
import re 
from termcolor import colored, cprint

def get_birthday() -> int:
    bd_pattern = r"\d{2}\.\d{2}\.\d{4}"
    while True: 
        colored_text = colored("dd.mm.yyyy", "red")
        text = f"Doğum tarixinizi -> {colored_text} <- bu formada daxil edin :"
        cprint(text)
        bd = input(": ")

        result = bool(re.match(bd_pattern, bd))
        if result: break
        else: continue
    
    return int(bd.replace(".", "")) 

def calculate_dofl(bd: int) -> None:
    while bd >= 10:
        total = 0 
        for ch in str(bd):
            total += int(ch)
        bd = total
    
    print(
        "Sizin həyat rəqəminiz : {dofl}".format(dofl=bd)
    )


calculate_dofl(
    get_birthday()
)

# Bunun üçün termcolor paketini yükləməliyik - pip install termcolor
    
