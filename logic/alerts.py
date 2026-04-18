from config import MAX_TEMP, MAX_HUMIDITY

def build_alerts(h, t, sound, light):
    alerts = []

    if t and t > MAX_TEMP:
        alerts.append(f"Temperature high: {t:.1f}C")

    if h and h > MAX_HUMIDITY:
        alerts.append(f"Humidity high: {h:.1f}%")

    if sound:
        alerts.append("Sound detected")

    if not light:
        alerts.append("Dark room")

    return alerts