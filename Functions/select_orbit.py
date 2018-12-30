from vpython import *


def first():
    for i in buttons:
        if i != first_button:
            i.checked = False


def second():
    for i in buttons:
        if i != second_button:
            i.checked = False


def third():
    for i in buttons:
        if i != third_button:
            i.checked = False


def fourth():
    for i in buttons:
        if i != fourth_button:
            i.checked = False


def fifth():
    for i in buttons:
        if i != fifth_button:
            i.checked = False


def sixth():
    for i in buttons:
        if i != sixth_button:
            i.checked = False


first_button = radio(position=print_anchor, text="1", bind=first)
second_button = radio(position=print_anchor, text="2", bind=second)
third_button = radio(position=print_anchor, text="3", bind=third)
fourth_button = radio(position=print_anchor, text="4", bind=fourth)
fifth_button = radio(position=print_anchor, text="5", bind=fifth)
sixth_button = radio(position=print_anchor, text="6", bind=sixth)


# make a list of the radios to make only selecting one at a time easier
buttons = [first_button, second_button, third_button, fourth_button, fifth_button, sixth_button]











