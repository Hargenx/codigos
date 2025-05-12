from controllers.main_controller import MainController
import tkinter as tk


def main():
    root = tk.Tk()
    _ = MainController(root)
    root.mainloop()


if __name__ == "__main__":
    main()
