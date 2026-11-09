import tkinter as tk
from tkinter import scrolledtext
from KJ_eliza import KJ_Eliza

eliza = KJ_Eliza()

window = tk.Tk()
window.title("ELIZA - DOCTOR")
window.geometry("650x500")
window.minsize(450, 350)

chat = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=("Consolas", 11),
    state=tk.DISABLED
)
chat.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

bottom = tk.Frame(window)
bottom.pack(fill=tk.X, padx=12, pady=(0, 12))

message_entry = tk.Entry(bottom, font=("Consolas", 11))
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))


def KJ_display(sender, message):
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, f"{sender}: {message}\n\n")
    chat.config(state=tk.DISABLED)
    chat.see(tk.END)


def KJ_send(event=None):
    message = message_entry.get().strip()

    if not message:
        return

    message_entry.delete(0, tk.END)
    KJ_display("YOU", message)

    if message.lower() == "quit":
        KJ_display("ELIZA", "Goodbye.")
        message_entry.config(state=tk.DISABLED)
        send_button.config(state=tk.DISABLED)
        return

    response = eliza.KJ_respond(message)
    KJ_display("ELIZA", response)


send_button = tk.Button(
    bottom,
    text="Send",
    font=("Consolas", 11),
    width=9,
    command=KJ_send
)
send_button.pack(side=tk.RIGHT)

window.bind("<Return>", KJ_send)

KJ_display("ELIZA", eliza.KJ_greet())
message_entry.focus_set()

window.mainloop()
