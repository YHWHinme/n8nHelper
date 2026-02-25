import asyncio
import queue
import socket
import threading

# Dev packages
import time

import requests as rq

# Textual Imports
from textual import log
from textual.app import App
from textual.widgets import Button, Label

responseQueue = queue.LifoQueue()  # Defining queue


class TuiApp(App):
    def compose(self):
        yield Label("Test String [bold red]![/]")
        yield Button("Print Callback")

    async def on_button_pressed(self, event):
        async def callback():
            self.log(f"Starting event {time.strftime} ")
            await asyncio.sleep(3)
            self.log(f"Finishing event {time.strftime}")

        await callback()


def main():
    async def postReq(
        SendingMessage: str,
        url: str = "http://172.16.24.60:5678/webhook/ce9a31a3-3ca8-4d03-aaad-2da31e96a93c",
    ):
        # Fetching data from fields
        fieldData: str = SendingMessage

        payload = {"prompt": fieldData}
        response = rq.post(url=url, data=payload)
        print(response.json())

    def socketServer():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", 2008))

        server.listen(2)

        while True:
            # Setting up the server
            client, _ = server.accept()
            message = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 17\r\n\r\Return message successful How are you?"
            client.send(message.encode())

            clientMessage = client.recv(1024).decode()  # Printing client message
            # TODO: Find out where to put client message

    serverThread = threading.Thread(target=socketServer, daemon=True)

    # Starting the threads
    serverThread.start()


if __name__ == "__main__":
    main()
    TuiApp().run()
