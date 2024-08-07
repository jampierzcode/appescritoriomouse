import tkinter as tk
from events import start_event_logging, stop_event_logging, replay_events

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

        self.replay_button = tk.Button(root, text="Reproducir", command=self.replay_events)
        self.replay_button.pack()

        self.is_monitoring = False

    def start_monitoring(self):
        self.is_monitoring = True
        self.label.config(text="Monitoreando eventos...")
        start_event_logging()

    def stop_monitoring(self):
        self.is_monitoring = False
        self.label.config(text="Detenido.")
        stop_event_logging()
        
      # Save events when monitoring stops

    def replay_events(self):
        replay_events()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
