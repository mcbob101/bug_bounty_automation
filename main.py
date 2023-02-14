import requests
import tkinter as tk

class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack()
        self.target_label = tk.Label(self.frame, text="Enter target:")
        self.target_label.pack()
        self.target_entry = tk.Entry(self.frame)
        self.target_entry.pack()
        self.check_button = tk.Button(self.frame, text="Check", command=self.check_target)
        self.check_button.pack()
        self.output_label = tk.Label(self.frame, text="")
        self.output_label.pack()

    def check_target(self):
        target = self.target_entry.get()
        try:
            response = requests.get(target)
            if response.status_code == 200:
                self.output_label.config(text="Target found!")
            else:
                self.output_label.config(text="Error: Target not found")
        except:
            self.output_label.config(text="Error: Invalid target URL")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
