"""Centralized style configuration for Tkinter app."""

# Base coulors and font
FONT_PRIMARY = ("Segoe UI", 14)
FONT_SECONDARY = ("Segoe UI", 14, "bold")
SECONDARY_COLOUR = "#B1D8B7"
PRIMARY_COLOUR = "#ffffff"
BG_COLOUR = "#00674F"
FG_COLOUR = "#1A5653"
DANGER_COLOUR = "#9B1313"
DANGER_LIGHT = "#FFA896"
LIGHT_GRAY = "#C9C5B1"
DARK_BLUE = "#375062"
LIGHT_BLUE = "#9DB5C9"

TAGS_STYLE = {
    "bg" : PRIMARY_COLOUR,
    "fg" : FG_COLOUR,
}

FONT_LABEL = {
    "font" : FONT_SECONDARY,
}

INPUT_FIELD = {
    "font": FONT_PRIMARY,
    "highlightthickness": 1,
    "highlightbackground": LIGHT_GRAY,
    "bd": 0,
}

BUTTON_DISPLAY = {
    "bg": DARK_BLUE,
    "activebackground": LIGHT_BLUE,
    "activeforeground": DARK_BLUE,
    "fg": PRIMARY_COLOUR,
    "font": FONT_SECONDARY,
    "padx": 20,
    "pady": 8,
    "bd": 2,
    "highlightthickness" :3,
    "cursor":"hand2"  
}

BUTTON_CREAT = {
    "bg": BG_COLOUR,
    "activebackground": SECONDARY_COLOUR,
    "activeforeground": BG_COLOUR,
    "fg": PRIMARY_COLOUR,
    "font": FONT_SECONDARY,
    "padx": 20,
    "pady": 8,
    "bd": 2,
    "highlightthickness" :3,
    "cursor":"hand2"  
}

BUTTON_EXIT ={
    "font": FONT_SECONDARY,
    "bg": DANGER_COLOUR,
    "activebackground": DANGER_LIGHT,
    "activeforeground": DANGER_COLOUR,
    "fg": PRIMARY_COLOUR,
    "padx": 20,
    "pady": 8,
    "bd": 2,
    "highlightthickness" :3,
    "cursor":"hand2" 
}










