import time
import pickle
import pyautogui
from pynput import mouse, keyboard
import threading

# Listas para guardar los eventos
events = []
start_time = None
is_recording = False

def record_event(event_type, *args):
    if is_recording:
        timestamp = time.time() - start_time
        events.append((event_type, timestamp, args))

def on_move(x, y):
    record_event('move', x, y)

def on_click(x, y, button, pressed):
    if pressed:
        record_event('click', x, y, button)

def on_scroll(x, y, dx, dy):
    record_event('scroll', x, y, dx, dy)

def on_key_press(key):
    try:
        record_event('key_press', key.char)
    except AttributeError:
        record_event('key_press', str(key))

def on_key_release(key):
    # Optional: handle key release if necessary
    pass

def event_logging_thread():
    global start_time, is_recording
    start_time = time.time()
    is_recording = True
    with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener, \
         keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()

def start_event_logging():
    global is_recording
    if not is_recording:
        thread = threading.Thread(target=event_logging_thread)
        thread.start()

def stop_event_logging():
    global is_recording
    is_recording = False

def save_events(filename="events.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(events, file)

# def load_events(filename="events.pkl"):
#     global events
#     with open(filename, 'rb') as file:
#         events = pickle.load(file)

def replay_events():
    # global events
    start_time = time.time()
    for event_type, timestamp, args in events:
        time.sleep(timestamp)  # Wait for the event time
        if event_type == 'move':
            pyautogui.moveTo(*args)
        elif event_type == 'click':
            pyautogui.click(*args)
        elif event_type == 'scroll':
            pyautogui.scroll(args[2], x=args[0], y=args[1])
        elif event_type == 'key_press':
            keyboard.press(args[0])
            keyboard.release(args[0])
