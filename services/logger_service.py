import csv
from config import CSV_FILE

def init_csv():
    try:
        with open(CSV_FILE, "x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "temperature",
                "humidity",
                "sound",
                "light",
                "alerts"
            ])
    except FileExistsError:
        pass


def save_row(timestamp, h, t, sound, light, alerts):
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp,
            f"{t:.1f}" if t else "N/A",
            f"{h:.1f}" if h else "N/A",
            "Sound" if sound else "No Sound",
            "Light" if light else "Dark",
            " | ".join(alerts) if alerts else "None"
        ])