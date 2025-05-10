import os
import psutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


print("""
  M   M   III  TTTTT  I  GGG   AAAAA  TTTTT  III  OOO   N   N
  MM MM    I     T    I  G     A   A    T     I   O   O  NN  N
  M M M    I     T    I  G  GG AAAAA    T     I   O   O  N N N
  M   M    I     T    I  G   G A   A    T     I   O   O  N  NN
  M   M   III     T   I   GGG  A   A    T    III  OOO   N   N
""")


suspicious_processes = [
    "cryptolocker.exe", "wannacry.exe", "locky.exe", "teslacrypt.exe", "notpetya.exe", 
    "ransomware_process.exe", "cureit.exe", "zcryptor.exe", "cerber.exe", "zepto.exe"
]


class RansomwareDetectHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_check_time = time.time()

    def on_modified(self, event):
        if event.is_directory:
            return

        current_time = time.time()

       
        if current_time - self.last_check_time < 5:  
            print(f"Possible ransomware activity detected: {event.src_path}")
        
        self.last_check_time = current_time

        print(f'File modified: {event.src_path}')
        
        
        suspicious_extensions = ['.locked', '.crypt', '.enc']
        if any(event.src_path.endswith(ext) for ext in suspicious_extensions):
            print(f"Suspicious file modification detected: {event.src_path}")
           

        
        if any(event.src_path.startswith(imp_file) for imp_file in important_files):
            print(f"Warning: Important file modified: {event.src_path}")
            

def check_ransomware_processes():
    """ Memeriksa proses yang mencurigakan yang sedang berjalan """
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() in [process.lower() for process in suspicious_processes]:
                print(f"Suspicious process detected: {proc.info['name']} with PID: {proc.info['pid']}")
              
                proc.kill()
                print(f"Ransomware process {proc.info['name']} has been blocked.")
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def check_important_files():
    """ Memeriksa file penting yang tidak boleh dimodifikasi atau hilang """
    for file in important_files:
        if not os.path.exists(file): 
            print(f"Important file {file} has been tampered with!")
           

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
   
    print("""
      MITIGATION SYSTEM ACTIVATED!
      Monitoring your system for ransomware activity...
    """)
    
    
    path_to_monitor = input("Enter the path to monitor (e.g., /home/chunsky): ").strip()
    
    
    print("Please enter the paths to the important files you want to protect:")
    important_files = []
    while True:
        file_path = input("Enter an important file path (or type 'done' to finish): ").strip()
        if file_path.lower() == 'done':
            break
        important_files.append(file_path)

    print(f"Monitoring directory: {path_to_monitor}...")
    print(f"Protecting the following important files: {important_files}")

   
    while True:
        
        if check_ransomware_processes():
            print("Ransomware activity blocked!")

        
        check_important_files()

        
        monitor_file_changes(path_to_monitor)

       
        time.sleep(5)
