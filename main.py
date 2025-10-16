import os
from datetime import datetime
from gtts import gTTS
import tkinter as tk
from tkinter import ttk, messagebox

OUTPUT_DIR = "output"

# === Fungsi Utama ===
def generate_voice():
    text = text_box.get("1.0", tk.END).strip()
    lang = lang_var.get()

    if not text:
        messagebox.showwarning("Peringatan", "Teks tidak boleh kosong!")
        return

    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Nama file + timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{OUTPUT_DIR}/{timestamp}_output.mp3"

        # Buat audio
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(filename)

        add_to_table(filename)
        messagebox.showinfo("Sukses", f"Audio disimpan di:\n{filename}")

    except Exception as e:
        messagebox.showerror("Error", f"Gagal membuat audio:\n{e}")

def add_to_table(filepath):
    name = os.path.basename(filepath)
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tree.insert("", "end", values=(name, date_str))

def load_existing_files():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    files = sorted(os.listdir(OUTPUT_DIR))
    for f in files:
        if f.endswith(".mp3"):
            path = os.path.join(OUTPUT_DIR, f)
            mtime = datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M:%S")
            tree.insert("", "end", values=(f, mtime))

    files.sort(key=lambda x: x[2], reverse=True)

def play_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih file dulu!")
        return
    filename = tree.item(selected[0], "values")[0]
    filepath = os.path.join(OUTPUT_DIR, filename)

    if os.path.exists(filepath):
        if os.name == 'nt':
            os.system(f'start {filepath}')
        elif os.name == 'posix':
            os.system(f'open {filepath}' if os.uname().sysname == 'Darwin' else f'xdg-open {filepath}')
    else:
        messagebox.showerror("Error", "File tidak ditemukan!")

def delete_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih file yang ingin dihapus!")
        return

    filename = tree.item(selected[0], "values")[0]
    filepath = os.path.join(OUTPUT_DIR, filename)

    confirm = messagebox.askyesno("Konfirmasi", f"Hapus file '{filename}'?")
    if confirm:
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
            tree.delete(selected[0])
            messagebox.showinfo("Info", f"File '{filename}' dihapus.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menghapus file:\n{e}")

# === GUI ===
root = tk.Tk()
root.title("🎙️ Simple TTS Apps - Tritronik")
root.geometry("650x550")
root.resizable(False, False)

# Label dan input teks
label = tk.Label(root, text="Masukkan teks yang ingin diubah jadi suara:")
label.pack(pady=8)

text_box = tk.Text(root, height=6, width=75)
text_box.pack(pady=5)

# Pilih bahasa
lang_frame = tk.Frame(root)
lang_frame.pack(pady=5)

tk.Label(lang_frame, text="Pilih Bahasa:").pack(side="left", padx=5)

lang_var = tk.StringVar(value="id")
lang_menu = ttk.Combobox(lang_frame, textvariable=lang_var, values=[
    "id",  # Indonesia
    "en",  # English
    "ja",  # Japanese
    "ko"   # Korean
], width=10, state="readonly")
lang_menu.pack(side="left")

# Tombol Generate
button = tk.Button(root, text="🎤 Generate Voice", command=generate_voice,
                   bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
button.pack(pady=10)

# Label tabel
tk.Label(root, text="Daftar File Output:").pack()

# Frame tabel
frame = tk.Frame(root, padx=10, pady=5)
frame.pack(pady=5, fill="both", expand=True)

columns = ("Nama File", "Tanggal Dibuat")
tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
tree.heading("Nama File", text="Nama File")
tree.heading("Tanggal Dibuat", text="Tanggal Dibuat")
tree.column("Nama File", width=350)
tree.column("Tanggal Dibuat", width=250)

# Scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# Tombol kontrol
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

btn_play = tk.Button(control_frame, text="▶️ Play", command=play_selected, bg="#2196F3", fg="white", width=10)
btn_play.pack(side="left", padx=5)

btn_delete = tk.Button(control_frame, text="🗑️ Delete", command=delete_selected, bg="#F44336", fg="white", width=10)
btn_delete.pack(side="left", padx=5)

# Muat file lama
load_existing_files()

root.mainloop()
