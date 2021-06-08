#!/usr/bin/env python3

import converter
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class ConverterGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Morse converter")
        self.window.resizable(False, False)
        font = ("sans", 10)
        title_font = ("sans", 14)

        # region Text input and output
        self.text_input = ScrolledText(self.window, width=30, height=10)
        self.text_output = ScrolledText(self.window, width=30, height=10)
        text_input_label = tk.Label(self.window, text="Input", font=title_font)
        text_output_label = tk.Label(self.window, text="Output", font=title_font)

        text_input_label.grid(row=0, column=0, pady=10, padx=10)
        text_output_label.grid(row=0, column=2, pady=10, padx=10)
        self.text_input.grid(row=1, column=0, pady=10, padx=10)
        self.text_output.grid(row=1, column=2, pady=10, padx=10)
        # endregion

        # region Exit and convert buttons
        exit_button = tk.Button(
            self.window,
            command=self.close,
            text="Close",
            font=font
        )
        convert_button = tk.Button(
            self.window,
            command=self.convert,
            text="Convert",
            font=font
        )

        convert_button.grid(row=1, column=1, pady=10, padx=10)
        exit_button.grid(row=2, column=0, columnspan=3, pady=10, padx=10)
        # endregion

    def convert(self):
        self.text_output.delete(0.0, tk.END)

        in_text = self.text_input.get(0.0, tk.END)
        out_text = ""
        if converter.is_morse(in_text):
            out_text = converter.to_plaintext(in_text)
        else:
            out_text = converter.to_morse(in_text)
        self.text_output.insert(tk.END, out_text)

    def open(self):
        self.window.mainloop()

    def close(self):
        self.window.destroy()


def main():
    gui = ConverterGUI()
    gui.open()


if __name__ == '__main__':
    main()
