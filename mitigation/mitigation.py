import os
import psutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ASCII Art - MITIGATION
print("""
  M   M   III  TTTTT  I  GGG   AAAAA  TTTTT  III  OOO   N   N
  MM MM    I     T    I  G     A   A    T     I   O   O  NN  N
  M M M    I     T    I  G  GG AAAAA    T     I   O   O  N N N
  M   M    I     T    I  G   G A   A    T     I   O   O  N  NN
  M   M   III     T   I   GGG  A   A    T    III  OOO   N   N
""")

# Daftar nama proses ransomware yang dicurigai
suspicious_processes = ["ransomware_name_1", "ransomware_name_2"]  # Ganti dengan nama proses ransomware yang Anda ketahui

# Daftar file penting yang harus dilindungi
important_files = ["/path/to/important/file1", "/path/to/important/file2"]  # Ganti dengan path file penting Anda

# Class untuk mendeteksi perubahan file
class RansomwareDetectHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'File modified: {event.src_path}')
        
        # Cek apakah file yang dimodifikasi berada di direktori penting
        if any(event.src_path.startswith(imp_file) for imp_file in important_files):
            print(f"Warning: Important file modified: {event.src_path}")
            # Dapat menambahkan tindakan pencegahan di sini

def check_ransomware_processes():
    """ Memeriksa proses yang mencurigakan yang sedang berjalan """
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() in suspicious_processes:
                print(f"Suspicious process detected: {proc.info['name']} with PID: {proc.info['pid']}")
                # Menghentikan proses yang mencurigakan
                proc.kill()
                print(f"Ransomware process {proc.info['name']} has been blocked.")
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def check_important_files():
    """ Memeriksa file penting yang tidak boleh dimodifikasi atau hilang """
    for file in important_files:
        if not os.path.exists(file):  # File hilang atau dimodifikasi
            print(f"Important file {file} has been tampered with!")
            # Tindakan pencegahan, misalnya memulihkan file dari cadangan atau menghentikan proses

def monitor_file_changes(path_to_monitor):
    """ Memantau perubahan pada file di direktori tertentu """
    event_handler = RansomwareDetectHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_monitor, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    # Menampilkan teks ASCII di awal program
    print("""
      MITIGATION SYSTEM ACTIVATED!
      Monitoring your system for ransomware activity...
    """)
    
    # Meminta input path yang ingin dipantau
    path_to_monitor = input("Enter the path to monitor (e.g., /path/to/monitor): ").strip()

    print(f"Monitoring directory: {path_to_monitor}...")

    # Memulai pemantauan secara real-time
    while True:
        # Cek dan hentikan proses ransomware jika ditemukan
        if check_ransomware_processes():
            print("Ransomware activity blocked!")

        # Memeriksa perubahan pada file penting
        check_important_files()

        # Memantau perubahan file di folder tertentu
        monitor_file_changes(path_to_monitor)

        # Tunggu sebentar sebelum memulai pengecekan berikutnya
        time.sleep(5)
