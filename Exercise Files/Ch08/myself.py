from tkinter import *
from tkinter import messagebox, ttk


class Feedback:
    def __init__(self, root):
        root.title("Explore California Feedback")
        root.resizable(False, False)
        root.configure(background="#e1d8b9")

        self.style = ttk.Style()
        self.style.configure("TButton", background="#e1d8b9")
        self.style.configure(
            "TLabel", background="#e1d8b9", font=("Arial", 11)
        )
        self.style.configure("TFrame", background="#e1d8b9")
        self.style.configure("TEntry", font=("Arial", 10))

        # Frame 1
        self.frame1 = ttk.Frame(master=root)
        self.frame1.pack()

        self.label_image = ttk.Label(master=self.frame1)
        self.label_image.image = PhotoImage(file="tour_logo.gif")
        self.label_image.configure(
            image=self.label_image.image, anchor="center"
        )
        self.label_image.grid(row=0, column=0, rowspan=2)

        self.label_header = ttk.Label(master=self.frame1)
        self.label_header.configure(
            text="Thanks for Exploring!", font=("Arial", 18, "bold")
        )
        self.label_header.grid(row=0, column=1)

        self.label_info = ttk.Label(master=self.frame1)
        self.label_info.configure(
            text="We're glad you chose Explore California for your recent adventure. Please tell us what you thought about the 'Desert to Sea' tour.",
            wraplength=300,
        )
        self.label_info.grid(row=1, column=1)

        # Frame 2
        self.frame2 = ttk.Frame(master=root)
        self.frame2.pack()

        self.label_name = ttk.Label(master=self.frame2)
        self.label_name.configure(text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, sticky="sw")

        self.entry_name = ttk.Entry(master=self.frame2)
        self.entry_name.configure(width=24)
        self.entry_name.focus_set()
        self.entry_name.grid(row=1, column=0, padx=5, sticky="se")

        self.label_email = ttk.Label(master=self.frame2)
        self.label_email.configure(text="Email:")
        self.label_email.grid(row=0, column=1, padx=5, sticky="sw")

        self.entry_email = ttk.Entry(master=self.frame2)
        self.entry_email.configure(width=24)
        self.entry_email.grid(row=1, column=1, padx=5, sticky="sw")

        self.label_comments = ttk.Label(master=self.frame2)
        self.label_comments.configure(text="Comments:")
        self.label_comments.grid(row=2, column=0, padx=5, sticky="sw")

        self.text_comments = Text(master=self.frame2)
        self.text_comments.configure(
            font=("Arial", 10), height=10, width=50, wrap="word"
        )
        self.text_comments.grid(row=3, column=0, columnspan=2)

        self.btn_submit = ttk.Button(master=self.frame2, text="Submit")
        self.btn_submit.grid(row=4, column=0, padx=5, pady=5, sticky="se")

        self.btn_clear = ttk.Button(master=self.frame2, text="Clear")
        self.btn_clear.grid(row=4, column=1, padx=5, pady=5, sticky="sw")

        # Event Handling
        self.btn_submit.configure(command=lambda: self.submit())
        self.btn_clear.configure(command=lambda: self.clear())
        entries = [
            child
            for child in self.frame2.winfo_children()
            if isinstance(child, Entry)
        ]
        for idx, entry in enumerate(entries):
            entry.bind(
                "<Return>", lambda e, idx=idx: self.enter_hit(e, entries, idx)
            )

    def submit(self):
        messagebox.showinfo(
            title="Explore California Feedback", message="Comment Submitted!"
        )
        print("Name:", self.entry_name.get())
        print("Email:", self.entry_email.get())
        print("Comments:", self.text_comments.get("1.0", "end"))

    def clear(self):
        self.entry_name.delete(first=0, last=END)
        self.entry_email.delete(first=0, last=END)
        self.text_comments.delete("1.0", "end")

    def enter_hit(self, event, entry_list, this_index):
        if this_index == (len(entry_list) - 1):
            self.text_comments.focus_set()
        else:
            next_index = this_index + 1
            entry_list[next_index].focus_set()


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__":
    main()
