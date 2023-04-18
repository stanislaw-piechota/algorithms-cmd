import curses
import processing
from curses import wrapper
from importlib import import_module
from os import listdir


def main(stdscr):
    menu_name = "Main menu"
    menu = package_names
    object = None
    object_menu = None
    
    stdscr.nodelay(True)
    stdscr.keypad(True)
    curses.echo()

    y = 1
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == "\x1b":
            break
        elif key in ["s", "KEY_DOWN", "KEY_C2"]:
            y += 1
            if y > len(menu):
                y = 1
        elif key in ["w", "KEY_UP", "KEY_A2"]:
            y -= 1
            if y <= 0:
                y = len(menu)
        elif key == "\n":
            if menu_name == "Main menu":
                menu_name = package_names[y-1]
                object = packages[y-1]
                menu = [func for func in dir(object) if not func.startswith('_')]+["back"]
                y = 1
            elif not menu_name.startswith("Options for") and y < len(menu):
                object_menu = processing.menu(object, menu_name.lower(), menu[y-1], stdscr)
                menu_name = "Options for "+menu_name
                menu = object_menu.options
            elif not menu_name.startswith("Options for") and y == len(menu):
                menu_name = "Main menu"
                menu = package_names
                y = 1
            elif menu_name.startswith("Options for") and y < len(menu):
                object_menu.execute(menu[y-1])
            elif menu_name.startswith("Options for") and y == len(menu):
                menu_name, menu = object_menu.back()
                y = 1

        stdscr.clear()
        stdscr.addstr(menu_name)
        for i, name in enumerate(menu):
            stdscr.addstr(i+1, 0, f'    {name}')
        stdscr.addstr(y, 0, ">")
        stdscr.refresh()


if __name__ == "__main__":
    package_names = [file.split('.')[0].capitalize() for file in listdir('algorithms') if not file.startswith('_')]
    packages = [getattr(import_module(f"algorithms.{pkg.lower()}"), pkg) for pkg in package_names]
    
    wrapper(main)
