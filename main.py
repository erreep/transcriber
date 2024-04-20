import tkinter as tk
from tkinter import filedialog, ttk, Text
import threading
from transcriber import transcriber  # Make sure the transcriber module is correctly imported

def transcribe_audio(file_path, progress_bar, text_area, style):
    if file_path:
        app.after(0, progress_bar.start)
        result = transcriber(file_path)
        app.after(0, lambda: update_text_area(text_area, result))
        app.after(0, progress_bar.stop)
        app.after(0, lambda: progress_bar.config(value=0))
        app.after(0, lambda: style.configure('TProgressbar', troughcolor='#D0D0D0'))


def on_submit():
    file_path = entry.get()
    if file_path:
        text_area.delete(1.0, tk.END)
        threading.Thread(target=transcribe_audio, args=(file_path,), daemon=True).start()

def update_text_area(result):
    text_area.insert(tk.END, result)

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    style = ttk.Style()
    style.theme_use('clam')  
    style.configure('TButton', font=('Helvetica', 12), background='#E1E1E1')
    style.configure('TLabel', font=('Helvetica', 12), background='#E1E1E1')
    style.configure('TEntry', font=('Helvetica', 12), background='#FFFFFF')
    style.configure('TProgressbar', troughcolor='#D0D0D0')


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Transcriber App")
    app.configure(background='#F0F0F0')

    frame = ttk.Frame(app, style='TFrame')
    frame.pack(padx=10, pady=10, expand=True, fill="both")

    label = ttk.Label(frame, text="Enter path to MP3 file:", background='#F0F0F0')
    label.pack(pady=10)

    entry = ttk.Entry(frame, width=50)
    entry.pack(pady=5)

    browse_button = ttk.Button(frame, text="Browse", command=lambda: open_file_dialog(entry))
    browse_button.pack(pady=5)

    submit_button = ttk.Button(frame, text="Transcribe", command=lambda: on_submit(entry.get(), progress_bar, text_area, style))
    submit_button.pack(pady=20)

    progress_bar = ttk.Progressbar(frame, style='TProgressbar', mode='indeterminate', length=300)
    progress_bar.pack(pady=10)

    text_area = tk.Text(frame, wrap="word", height=15, width=60)
    text_area.pack(pady=15, padx=15, expand=True, fill="both")

    app.mainloop()