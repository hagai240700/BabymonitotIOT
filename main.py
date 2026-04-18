import time
from datetime import datetime
import RPi.GPIO as GPIO

from sensors.temp_sensor import read_temp_humidity
from sensors.sound_sensor import setup as sound_setup, read_sound
from sensors.light_sensor import setup as light_setup, read_light

from services.telegram_service import send_message
from services.logger_service import init_csv, save_row
from logic.alerts import build_alerts

GPIO.setmode(GPIO.BCM)
sound_setup()
light_setup()

last_alert_message = ""

def main():
    global last_alert_message
    init_csv()

    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            h, t = read_temp_humidity()
            light = read_light()
            sound = read_sound()

            alerts = build_alerts(h, t, sound, light)

            save_row(timestamp, h, t, sound, light, alerts)

            if alerts:
                message = "ALERT!\n" + "\n".join(alerts)
                if message != last_alert_message:
                    send_message(message)
                    last_alert_message = message
            else:
                last_alert_message = ""

            time.sleep(2)

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()