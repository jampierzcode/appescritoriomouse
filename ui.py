import tkinter as tk
from events import start_event_logging
from chrome_monitor import check_chrome_tabs

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de Eventos")

        self.label = tk.Label(root, text="Esperando eventos...")
        self.label.pack()

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_monitoring)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Detener", command=self.stop_monitoring)
        self.stop_button.pack()

        self.is_monitoring = False

    def start_monitoring(self):
        self.is_monitoring = True
        self.label.config(text="Monitoreando eventos...")

        # Start event logging and Chrome monitoring
        start_event_logging(self.log_event)
        check_chrome_tabs()

    def stop_monitoring(self):
        self.is_monitoring = False
        self.label.config(text="Detenido.")

    def log_event(self, event_message):
        if self.is_monitoring:
            print(event_message)
            self.label.config(text=event_message)
