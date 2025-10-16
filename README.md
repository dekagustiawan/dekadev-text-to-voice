# 🎙️ Simple TTS Apps by DekaDev

**Simple TTS Apps** is a lightweight desktop application written in Python that converts text into natural-sounding **Indonesian speech** using Google Text-to-Speech (gTTS).  
Built to be **simple, reliable, and educational**, this project is open for collaboration and improvement by anyone interested in text-to-speech or beginner-friendly Python apps.

---

## ✨ Features

✅ Convert any text into spoken Indonesian voice  
✅ Change language English, Indonesia, Japan, Korea 
✅ Auto-save all generated audio files to `/output` folder  
✅ Display file list 
✅ Simple and clean desktop UI built with **Tkinter**  
✅ No API key or token required — just an internet connection  
✅ 100% Free & Open for collaboration under **DekaDev**

---

## 🧩 Tech Stack

| Component  | Description |
|-------------|-------------|
| **Python 3.8+** | Core programming language |
| **Tkinter** | GUI framework (bundled with Python) |
| **gTTS (Google Text-to-Speech)** | Text-to-speech conversion engine |
| **datetime, os, time** | For file management and timestamps |

---

## 🧠 How It Works

1. User enters text in the input box.  
2. When **Generate Voice** is clicked, the app:
   - Converts text to speech using `gTTS(lang='id')`
   - Saves the file as `output/<timestamp>_output.mp3`
   - Refreshes the table with the new entry  
3. The most recent file appears **at the top** of the list.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dekadev/simple-tts-apps.git
cd simple-tts-apps
```

### 2️⃣ Install Dependencies

Make sure you have Python 3.8 or newer.

```bash
pip install -r requirements.txt
```

If you're on **Linux**, you may also need:
```bash
sudo apt install python3-tk
```

### 3️⃣ Run the App

```bash
python main.py
```

The app window will open.  
Type your text, click **🎤 Generate Voice**, and check the `/output` folder for your `.mp3` file.

---

## 📁 Folder Structure

```
Simple-TTS-Apps/
│
├── main.py                # Main application file
├── requirements.txt       # Python dependencies
├── README.md              # Documentation (this file)
└── output/                # Generated voice files (auto-created)
```

---

## 🪄 Example Usage

Type this in the app:
```
Halo, ini adalah suara buatan Simple TTS Apps dari DekaDev!
```

Then click **🎤 Generate Voice**  
➡ A file like `20251015_142233_output.mp3` will appear in your `output` folder.  
Double-click to play and listen!

---

## 🎨 UI Preview (placeholder)

> Screenshot will be added soon — maybe from DekaDev’s video demo!  
> The interface includes:
> - Text area for input  
> - Generate button  
> - Scrollable table showing saved files  

---

## 🤝 Contributing

Want to collaborate?  
I’d love to connect and grow this project together.

## 🧑‍💻 About DekaDev

**DekaDev** is a small personal brand dedicated to building practical, creative, and educational apps for learning and fun.  
This app was inspired by a simple idea — _“make something my kids can learn from.”_

> 💬 *"Simple TTS Apps is a small start — but small projects can spark big learning."*

📽️ If you make a **video demo**, please mention **DekaDev** in the credits!  
Collaboration inquiries: (add your email, GitHub, or YouTube link here)

---

## ⚖️ License

This project is **open-source** and free to use under the MIT License.  
You’re free to modify and share, just keep credit to **DekaDev**.

```
Keep it simple. Keep it open. 💚
```

---

## 🧾 Requirements

See [`requirements.txt`](./requirements.txt)

```txt
gtts==2.5.1
tkintertable==1.3.3
```

---

Made with 💚 by **DekaDev**
