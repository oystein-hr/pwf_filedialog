import webbrowser
import websockets
import pathlib
import asyncio
import tkinter
from tkinter import filedialog


async def dialogwindow(websocket, path):
    while True:
        try:
            data = await websocket.recv()
            if data == 'click':
#                print("Click!")
                response = await fd()
                await websocket.send(response)
            else:
                print(data)

        except websockets.ConnectionClosed:
            break

    asyncio.get_event_loop().stop()


async def fd():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    file_path = filedialog.askopenfile()
#    print(file_path.name)

    return file_path.name


def main():
    start_server = websockets.serve(dialogwindow, "127.0.0.1", 5001)
    gui_path = pathlib.Path.cwd() / 'front-end' / 'gui.html'

    webbrowser.open_new_tab(gui_path.as_uri())

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()
