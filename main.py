from machine import Pin
from utime import sleep

print("hello, world!")

led_verde = Pin(15, Pin.OUT)
led_amarelo = Pin(2, Pin.OUT)
led_vermelho = Pin(0, Pin.OUT)

while True:
  led_verde.on()
  print("ABERTO")
  sleep(20)
  led_verde.off()
  led_amarelo.on()
  print("ATENÇÃO")
  sleep(10)
  led_amarelo.off()
  led_vermelho.on()
  print("VERMELHO")
  sleep(7)
  led_vermelho.off()
  
  