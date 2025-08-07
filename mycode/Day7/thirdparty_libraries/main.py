from PIL import Image, ImageDraw

img = Image.new('RGB', (200, 200), color = 'skyblue')
img.save('skyblue_image.png')



# my_img = Image.open('skyblue_image.png')
# my_img.show()

# my_img = my_img.resize((100, 100))
# my_img.save('resized_skyblue_image.png')


draw = ImageDraw.Draw(img)

draw.text((10, 10), "Hello World", fill="black")
img.save('hello_world_image.png')


draw.rectangle([50, 50, 150, 150], fill="yellow", outline="black")
img.save('rectangle_image.png')

from PIL import Image, ImageDraw

img = Image.new('RGB', (200, 200), color = 'skyblue')
img.save('skyblue_image.png')



# my_img = Image.open('skyblue_image.png')
# my_img.show()

# my_img = my_img.resize((100, 100))
# my_img.save('resized_skyblue_image.png')


draw = ImageDraw.Draw(img)

draw.text((10, 10), "Hello World", fill="black")
img.save('hello_world_image.png')


draw.rectangle([50, 50, 150, 150], fill="yellow", outline="black")
img.save('rectangle_image.png')

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.image("skyblue_image.png", x=10, y=10, w=50, h=50)

pdf.output("image_in_pdf.pdf")


from rich.console import Console
# print(rich)

console = Console()
console.print("hello, we are a party", style="bold red on white")


console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].", style="bold green")

# from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Production Budget", justify="right")
table.add_column("Box Office", justify="right")
table.add_row(
    "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
    "May 25, 2018",
    "[red]Solo[/red]: A Star Wars Story",
    "$275,000,000",
    "$393,151,347",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VIII: The Last Jedi",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)

console.print(table)