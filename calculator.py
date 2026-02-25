import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.display = tk.Entry(root, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        buttons = [
            'C', '←', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', ''
        ]
        
        row = 1
        col = 0
        for button in buttons:
            if button:
                tk.Button(root, text=button, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configure grid weights for resizing
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        
        self.expression = ""
    
    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif char == 'C':
            self.expression = ""
        elif char == '←':
            self.expression = self.expression[:-1]
        else:
            self.expression += char
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()