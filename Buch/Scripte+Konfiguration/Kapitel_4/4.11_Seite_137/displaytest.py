#!/usr/bin/python
import time
 
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
import Image
import ImageDraw
import ImageFont
 
DIN = 17
SCLK = 18
DC = 23
RST = 24
CS = 25

disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
disp.begin(contrast=60)
disp.clear()
disp.display()

# Leeres Bildobjekt erstellen
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
# Zeichenobjekt erstellen
draw = ImageDraw.Draw(image)
# Bildschirm löschen
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
 
# Vektorfiguren zeichnen
draw.ellipse((2,2,22,22), outline=0, fill=255)
draw.rectangle((24,2,44,22), outline=0, fill=255)
draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
draw.line((68,22,81,2), fill=0)
draw.line((68,2,81,22), fill=0)
 
# Schrift hinzufügen
font = ImageFont.load_default()
draw.text((8,30), 'Hallo Welt!', font=font)
 
# Bild anzeigen
disp.image(image)
disp.display()
