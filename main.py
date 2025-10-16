from gtts import gTTS
import os
from datetime import datetime

def text_to_speech(text):
    try:
        # Pastikan folder output ada
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        # Buat nama file dengan timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/{timestamp}_output.mp3"

        # Konversi teks ke suara bahasa Indonesia
        tts = gTTS(text=text, lang='id', slow=False)
        tts.save(filename)
        print(f"✅ Audio disimpan sebagai: {filename}")

        # Putar file (opsional)
        if os.name == 'nt':  # Windows
            os.system(f'start {filename}')
        elif os.name == 'posix':  # macOS / Linux
            os.system(f'open {filename}' if os.uname().sysname == 'Darwin' else f'xdg-open {filename}')

    except Exception as e:
        print(f"❌ Terjadi error: {e}")

if __name__ == "__main__":
    text = input("Masukkan teks yang ingin diubah jadi suara: ")
    text_to_speech(text)
