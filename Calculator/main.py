import tkinter as tk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("420x600")
        self.root.config(bg="#282828")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.input_frame = self.create_input_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.input_frame.pack(expand=True, fill="both")
        self.buttons_frame.pack(expand=True, fill="both")

        self.create_input_field()
        self.create_buttons()

    def create_input_frame(self):
        frame = tk.Frame(self.root, bg="#282828")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root, bg="#282828")
        return frame

    def create_input_field(self):
        input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=(
            'Arial', 24), bg="#E0E0E0", fg="#000000", bd=10, justify="right")
        input_field.grid(row=0, column=0, ipadx=8, ipady=20,
                         padx=10, pady=10, sticky="ew")

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            'C', '0', '=', '+', 'log',
            'sqrt', 'pow', '(', ')'
        ]

        row = 1
        col = 0
        
        for button in buttons:
            def button_command(x=button): return self.on_button_click(x)
            tk.Button(self.buttons_frame, text=button, width=5, height=2, bg="#505050", fg="#FFFFFF", font=(
                'Arial', 18), command=button_command, bd=0, highlightbackground="#282828").grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            col += 1
            if col > 4:
                col = 0
                row += 1

        for i in range(5):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(row+1):
            self.buttons_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
            self.input_text.set(self.expression)
        elif button == '=':
            try:
                self.expression = self.expression.replace(
                    'sin', 'math.sin(math.radians')
                self.expression = self.expression.replace(
                    'cos', 'math.cos(math.radians')
                self.expression = self.expression.replace(
                    'tan', 'math.tan(math.radians')
                self.expression = self.expression.replace('log', 'math.log10')
                self.expression = self.expression.replace('sqrt', 'math.sqrt')
                self.expression = self.expression.replace('pow', 'math.pow')

                if 'math.sin(' in self.expression or 'math.cos(' in self.expression or 'math.tan(' in self.expression:
                    self.expression = self.expression.replace(')', '))')

                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(button)
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
