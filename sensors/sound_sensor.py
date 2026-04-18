import RPi.GPIO as GPIO
from config import SOUND_PIN

def setup():
    GPIO.setup(SOUND_PIN, GPIO.IN)

def read_sound():
    return GPIO.input(SOUND_PIN) == 1