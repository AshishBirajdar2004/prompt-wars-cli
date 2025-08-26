import pyfiglet
from rich.console import Console
from rich.text import Text

# Initialize Rich console once
console = Console()

def show_banner(title: str = "MY PROJECT"):
    ascii_banner = pyfiglet.figlet_format(title, font="slant")  # <-- use a safe font
    text = Text(ascii_banner)
    text.stylize("bold magenta", 0, len(ascii_banner)//2)
    text.stylize("bold cyan", len(ascii_banner)//2)
    console.print(text)
