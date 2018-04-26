#!/usr/bin/python
#Written by Imperdin
import socket
from time import sleep
import os
from datetime import datetime
socket.setdefaulttimeout(5)

def main():
    Strikes = 0
    while True:
      try:
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         sock.connect(('127.0.0.1',80))
         sock.send("GET /h HTTP/1.1\n\n")
         buff = sock.recv(4096)
         if ("Totals:</th><td></td>" in buff):
                 Strikes = 3
                 raise Exception('Invalid Totals') # Also restart rigs when connection is out to minimize down-time
         sock.close()
         sleep(30)
         Strikes = 0
      except Exception as e:
         Strikes += 1
         if (Strikes > 2):
            with open("Log.txt","a+") as f:
               f.write("Miner Crashed at %s Due To %s Rebooting...\n"%((datetime.now().strftime('%Y-%m-%d %H:%M:%S')),e))
            os.popen("shutdown -r -f -t 0")
         else:
            sleep(5)


if __name__ == "__main__":
   main()
