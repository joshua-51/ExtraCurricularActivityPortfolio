from dinosay import dinostring, DINO_TYPE
from rich.console import Console
from rich.panel import Panel
import sys

console = Console()

def determiningName():
    try:
        return sys.argv[1] 
    except IndexError:
        return "world"

def printingDinoStuff(name):
    console.print(Panel(f"[bold magenta]HELLO {name}, I AM A VERY SMART DINO WHO WILL MAKE YOU NOTES[/bold magenta]", expand=False))
    t_rex_with_bubble = dinostring(" ", DINO_TYPE['tyrannosaurus'], 'normal')
    lines = t_rex_with_bubble.split('\n')
    global just_the_dino
    just_the_dino = "\n".join(lines[6:])
    print(just_the_dino)

def gettingGeminiTopic():
    console.print(Panel(f"[bold blue]What topic (you can be specific) do you want to make notes for?[/bold blue]", expand=False))
    return input("\n\nEnter TOPIC: ")
