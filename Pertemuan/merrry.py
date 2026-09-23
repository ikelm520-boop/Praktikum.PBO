import tkinter as tk

# Konstanta ukuran box/jendela lirik
BOX_W = 400
BOX_H = 100

class LyricCard:
    def __init__(self, root, text, x, y):
        # Membuat jendela khusus tanpa border (overrideredirect) agar terlihat melayang
        self.win = tk.Toplevel(root)
        self.win.overrideredirect(True)
        self.win.attributes("-topmost", True)  # Selalu di depan aplikasi lain
        self.win.configure(bg="black")

        self.full_text = text
        self.typewriter_index = 0
        self.x = x
        self.y = y

        # Label untuk menampilkan teks
        self.label = tk.Label(self.win, text="", font=("Helvetica", 16, "bold"), fg="white", bg="black", wraplength=BOX_W-20)
        self.label.pack(expand=True, fill="both", padx=10, pady=10)

        # Mengatur posisi awal jendela
        self.win.geometry(f"{BOX_W}x{BOX_H}+{int(self.x)}+{int(self.y)}")

        # Memulai efek mengetik dan pergerakan naik
        self.typewriter()
        self.rise()

    def rise(self):
        # Mengurangi koordinat Y agar teks bergerak ke atas
        self.y -= 1  
        self.win.geometry(f"{BOX_W}x{BOX_H}+{int(self.x)}+{int(self.y)}")
        
        # Jika belum keluar dari batas atas layar, terus jalankan fungsi rise
        if not self.is_offscreen():
            self.win.after(20, self.rise)
        else:
            self.win.destroy()  # Hapus jendela jika sudah keluar layar

    def is_offscreen(self):
        # Memeriksa apakah jendela sudah lewat dari batas atas layar
        return self.y + BOX_H < -50

    def typewriter(self):
        # Efek mengetik huruf demi huruf
        if self.typewriter_index <= len(self.full_text):
            self.label.config(text=self.full_text[:self.typewriter_index])
            self.typewriter_index += 1
            self.win.after(80, self.typewriter)


class LyricFloatApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()  # Sembunyikan jendela utama tkinter

        # Mengambil resolusi layar komputer Anda
        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()

        # DISESUAIKAN: Lirik lagu "Sweet Boy" - Malcolm Todd
        self.lyrics = [
            "Can we go home now?",
            "It's getting later, baby",
            "Can we go home now?",
            "You think it's time to give up",
            "We're on our own now",
            "No place to drive you crazy",
            "Don't share a home now",
            "I'm okay 'til tonight..."
        ]
        
        self.next_lyric_idx = 0
        self.current_side = "left"

        self.start()

    def random_safe_x(self):
        # Menentukan posisi X secara bergantian kiri dan kanan
        center_x = self.screen_w // 2
        spacing = BOX_W + 60

        if self.current_side == "left":
            x = center_x - spacing
            self.current_side = "right"
        else:
            x = center_x + 60
            self.current_side = "left"
        return x

    def show_next_lyric(self):
        # Memeriksa apakah lirik masih ada
        if self.next_lyric_idx < len(self.lyrics):
            text = self.lyrics[self.next_lyric_idx]
            x_pos = self.random_safe_x()
            y_pos = self.screen_h - 150  # Muncul dari area bawah layar

            # Membuat objek LyricCard baru
            LyricCard(self.root, text, x_pos, y_pos)
            
            self.next_lyric_idx += 1
            # Menampilkan lirik berikutnya setiap 3.5 detik
            self.root.after(2500, self.show_next_lyric)
        else:
            # Jika lirik habis, tutup aplikasi setelah beberapa saat
            self.root.after(5000, self.root.quit)

    def start(self):
        self.show_next_lyric()


# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = LyricFloatApp(root)
    root.mainloop()