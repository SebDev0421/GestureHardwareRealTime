import os
import psutil
import time
import json
import websocket
try:
    import thread
except ImportError:
    import _thread as thread

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        while (True):
          pid = os.getpid()
          py = psutil.Process(pid)
          interfaces = {}
          wifiDates = psutil.net_if_addrs()
          i = 0
          ipAddress = ''
          for out in wifiDates['Wi-Fi']:
              if(i == 1):
                ipAddress = out.address  
              i += 1
          memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
          disk_usage = psutil.disk_usage("/")
          sendDates = json.dumps({"cpu_percent":psutil.cpu_percent(interval=1),"ram":psutil.virtual_memory()[2],"memory":disk_usage.percent,"ipAddress":ipAddress})
          ws.send(sendDates)
          time.sleep(1)
    thread.start_new_thread(run, ())


websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://181.54.182.7:8999/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
ws.on_open = on_open
ws.run_forever()



