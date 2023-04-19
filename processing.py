from abc import ABC, abstractmethod
from curses import color_pair as cl

class menu():
    def __init__(self, object, file_name, func_name, stdscr):
        self.object = object
        self.stdscr = stdscr
        self.file_name = file_name
        self.func_name = func_name
        self.input = {}
        self.options = [
            "change_input",
            "run_code",
            "provide_code",
            "provide_description",
            "back"
        ]


    def back(self):
        menu_name = self.file_name.split('.')[0].capitalize()
        menu = [func for func in dir(self.object) if not func.startswith('_')]+["back"]
        return menu_name, menu


    def run_code(self):
        if self.input == {}:
            return "No input provided. Change your input first", cl(1)
        
        instance = self.object(**self.input)
        try:
            result = getattr(instance, self.func_name)()
        except Exception as e:
            print(e)
            return "Something went wrong while executing algorithm - "+e, cl(1)

        return "The result is:\n"+repr(result)


    def change_input(self):
        try:
            self.input.clear()
            for name, opt in self.object._get_requirements().items():
                self.stdscr.addstr(opt["prompt"]+": ")
                if opt["type"] == int:
                    self.input[name] = opt["type"](self.stdscr.getstr())
            return
        except (TypeError, ValueError):
            return "Incorrect input, try again", cl(1)


    def provide_code(self):
        with open(f"algorithms/{self.file_name}.py") as file:
            code = file.read().split(self.func_name+'(self):\n')[1].split('# BEGIN\n')[1].split('# END')[0]
            code = '\n'.join([line[2:] if line.startswith('\t') else line[8:] for line in code.split('\n')])
            code += "\n\nPress any key to kontinue..."
        return code


    def execute(self, func_name):
        self.stdscr.nodelay(False)
        try:
            self.stdscr.clear()
            self.stdscr.refresh()
            result = getattr(self, func_name)()
            if type(result) == str:
                self.stdscr.addstr(result)
            else:
                self.stdscr.addstr(result[0], result[1])
            self.stdscr.refresh()
        except (TypeError, ValueError) as e:
            return
        except Exception as e:
            print(e)

        self.stdscr.getch()
        self.stdscr.nodelay(True)


    def provide_description(self):
        description = "Input:\n"
        for name, opt in self.object._get_requirements().items():
            description += f"    {name} ({opt['type']}): {opt['prompt']}\n"
        description += "\nOutput:\n"
        for name, opt in self.object._get_output_type().items():
            description += f"    {name} ({opt['type']}): {opt['prompt']}\n"
        description += "\n\nPress any key to continue..."

        return description
        

class Module(ABC):
    @abstractmethod
    def _get_requirements(self):
        pass

    @abstractmethod
    def _get_output_type(self):
        pass
    