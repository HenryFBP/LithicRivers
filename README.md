# LithicRivers

rocks and shit

ascii dwarf mine game, very wip...

## play it

<https://github.com/HenryFBP/LithicRivers/releases>

## what is this

![](https://memestatic.fjcdn.com/pictures/Dwarf_834ec5_6504028.jpg)

god help me

## running

    pipenv install
    pipenv shell
    python -m lithicrivers

## notes
- https://github.com/peterbrittain/asciimatics/blob/v1.13/samples/tab_demo.py
- https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way/50465583#50465583

## TODO
- add procedurally generated catgirls
- do perf testing to fix lag on startup...thanks numpy...
- auto-scale the viewport based off of viewable area
  - determine from screen size
  - determine from "blank space" in asciimatics (if this is even doable)
- don't use numpy, its a bloated big ass chungoid that adds to the pyinstaller exe size
