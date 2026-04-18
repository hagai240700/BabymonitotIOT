# BabymonitotIOT# Baby Monitor IoT

מערכת חכמה לניטור סביבת תינוק בזמן אמת באמצעות Raspberry Pi, חיישני טמפרטורה, לחות, אור ורעש, ושליחת התראות דרך Telegram Bot.

## תיאור הפרויקט

הפרויקט פותח במסגרת קורס Internet of Things ומטרתו לנטר את תנאי הסביבה בחדר תינוק בצורה אוטומטית ורציפה.  
המערכת קוראת נתונים מחיישנים המחוברים ל־Raspberry Pi, בודקת האם קיימת חריגה מערכים שהוגדרו מראש, שומרת לוג לקובץ CSV, ושולחת התראות למשתמש דרך Telegram במקרה הצורך.

המערכת מאפשרת להורה או למשתמש לעקוב אחרי תנאי החדר ולקבל התראות מהירות כאשר מזוהה מצב חריג כמו טמפרטורה גבוהה, לחות גבוהה, רעש בחדר או חושך.

## פיצ'רים עיקריים

- קריאת טמפרטורה ולחות מחיישן DHT
- זיהוי רעש באמצעות חיישן קול
- זיהוי אור או חושך באמצעות חיישן אור
- שליחת התראות בזמן אמת דרך Telegram Bot
- שמירת כל המדידות לקובץ CSV
- מניעת שליחת התראות כפולות ברצף על אותו מצב
- מבנה קוד מודולרי ונוח לתחזוקה

## טכנולוגיות וכלים

- Python
- Raspberry Pi
- Adafruit_DHT
- RPi.GPIO
- Telegram Bot API
- CSV Logging

## מבנה הפרויקט

```bash
BabyMonitotIOT/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── sensors/
│   ├── temp_sensor.py
│   ├── sound_sensor.py
│   └── light_sensor.py
│
├── services/
│   ├── telegram_service.py
│   └── logger_service.py
│
├── logic/
│   └── alerts.py
│
└── data/
    └── baby_room_log.csv