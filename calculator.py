import tkinter as tk

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg="#1c1c1e")

        self.current = "0"
        self.prev = None
        self.op = None
        self.just_evaled = False
        self.active_op_btn = None

        self._build_ui()

    def _build_ui(self):
        outer = tk.Frame(self.root, bg="#1c1c1e", padx=16, pady=16)
        outer.pack()

        screen = tk.Frame(outer, bg="#000000", width=268, height=140)
        screen.pack(pady=(0, 12))
        screen.pack_propagate(False)

        self.expr_var = tk.StringVar(value="")
        self.disp_var = tk.StringVar(value="0")

        tk.Label(screen, textvariable=self.expr_var, bg="#000", fg="#888888",
                 font=("Courier New", 13), anchor="e", justify="right",
                 wraplength=248).pack(fill="x", padx=12, pady=(14, 0))

        tk.Label(screen, textvariable=self.disp_var, bg="#000", fg="#ffffff",
                 font=("Helvetica", 44, "bold"), anchor="e", justify="right",
                 wraplength=248).pack(fill="both", expand=True, padx=12, pady=(0, 10))

        btn_frame = tk.Frame(outer, bg="#1c1c1e")
        btn_frame.pack()

        buttons = [
            [("AC", "func"), ("+/-", "func"), ("%", "func"), ("÷", "op")],
            [("7",  "num"),  ("8",  "num"),   ("9", "num"),  ("×", "op")],
            [("4",  "num"),  ("5",  "num"),   ("6", "num"),  ("−", "op")],
            [("1",  "num"),  ("2",  "num"),   ("3", "num"),  ("+", "op")],
            [("0",  "zero"), (".",  "num"),   ("=", "eq")],
        ]

        self.op_buttons = {}

        for r, row in enumerate(buttons):
            col_offset = 0
            for btn_text, btn_type in row:
                if btn_type == "func":
                    bg, fg, hover = "#a5a5a5", "#000000", "#c0c0c0"
                elif btn_type == "op":
                    bg, fg, hover = "#ff9f0a", "#ffffff", "#ffb833"
                elif btn_type == "eq":
                    bg, fg, hover = "#ff9f0a", "#ffffff", "#ffb833"
                else:
                    bg, fg, hover = "#333335", "#ffffff", "#4a4a4c"

                width = 4 if btn_type == "zero" else 2
                colspan = 2 if btn_type == "zero" else 1

                btn = tk.Button(
                    btn_frame, text=btn_text,
                    bg=bg, fg=fg, activebackground=hover, activeforeground=fg,
                    font=("Helvetica", 18, "bold"),
                    width=width, height=1,
                    relief="flat", bd=0, cursor="hand2",
                    command=lambda t=btn_text, tp=btn_type: self._press(t, tp)
                )
                btn.grid(row=r, column=col_offset, columnspan=colspan,
                         padx=5, pady=5, ipadx=10, ipady=12, sticky="nsew")

                if btn_type == "op":
                    self.op_buttons[btn_text] = btn

                col_offset += colspan

    def _format(self, val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        if len(s) > 10:
            s = f"{float(val):.4e}"
        return s

    def _set_display(self, val):
        self.disp_var.set(self._format(val))

    def _highlight_op(self, symbol):
        for sym, btn in self.op_buttons.items():
            if sym == symbol:
                btn.configure(bg="#ffffff", fg="#ff9f0a")
            else:
                btn.configure(bg="#ff9f0a", fg="#ffffff")

    def _clear_op_highlight(self):
        for btn in self.op_buttons.values():
            btn.configure(bg="#ff9f0a", fg="#ffffff")

    def _press(self, text, kind):
        if kind == "num":
            self._press_num(text)
        elif kind == "zero":
            self._press_num("0")
        elif kind == "op":
            sym_map = {"÷": "/", "×": "*", "−": "-", "+": "+"}
            self._press_op(sym_map[text], text)
        elif kind == "eq":
            self._evaluate(final=True)
        elif kind == "func":
            self._press_func(text)

    def _press_num(self, n):
        if self.just_evaled:
            self.current = "0"
            self.just_evaled = False
        if n == "." and "." in self.current:
            return
        self.current = n if (self.current == "0" and n != ".") else self.current + n
        self._set_display(self.current)

    def _press_op(self, op_char, symbol):
        self.just_evaled = False
        if self.prev is not None and self.op:
            self._evaluate(final=False)
        self.prev = float(self.current)
        self.op = op_char
        self.current = "0"
        self.expr_var.set(f"{self._format(self.prev)} {symbol}")
        self._highlight_op(symbol)

    def _evaluate(self, final):
        if self.prev is None or self.op is None:
            return
        a, b = self.prev, float(self.current)
        sym_map = {"+": "+", "-": "−", "*": "×", "/": "÷"}
        sym = sym_map.get(self.op, self.op)

        if self.op == "+":   res = add(a, b)
        elif self.op == "-": res = subtract(a, b)
        elif self.op == "*": res = multiply(a, b)
        elif self.op == "/": res = divide(a, b)

        if res == "Error":
            self.disp_var.set("Error")
            self.expr_var.set("")
            self.current, self.prev, self.op = "0", None, None
            return

        rounded = round(res, 10)
        if final:
            self.expr_var.set(f"{self._format(a)} {sym} {self._format(b)} =")
            self.current = str(rounded)
            self._set_display(rounded)
            self.prev = None
            self.op = None
            self.just_evaled = True
            self._clear_op_highlight()
        else:
            self.current = str(rounded)
            self._set_display(rounded)

    def _press_func(self, f):
        if f == "AC":
            self.current = "0"
            self.prev = None
            self.op = None
            self.just_evaled = False
            self.disp_var.set("0")
            self.expr_var.set("")
            self._clear_op_highlight()
        elif f == "+/-":
            self.current = str(float(self.current) * -1)
            self._set_display(self.current)
        elif f == "%":
            self.current = str(float(self.current) / 100)
            self._set_display(self.current)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
