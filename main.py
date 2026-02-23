import queue
import socket
import threading

import requests as rq
import ttkbootstrap as tk
from ttkbootstrap import Style


def main():
    q = queue.LifoQueue()

    def UI():
        def sendAuto(
            url: str = "http://172.16.24.60:5678/webhook/ce9a31a3-3ca8-4d03-aaad-2da31e96a93c",
        ):
            # Fetching data from fields
            fieldData: str = dataSend.get("1.0", "end").strip()

            payload = {"prompt": fieldData}
            message = rq.post(url=url, data=payload)
            print(message.json())

        # Starter settings
        window = tk.Tk()
        Style(theme="darkly")

        # Welcoming
        welcome = tk.Label(window, text="Send your body")  # Raw label text
        welcome.pack()

        dataSend = tk.Text(window, height=20, width=70)  # Setting passwords
        dataSend.pack()

        # Button
        loginButton = tk.Button(
            window, text="Send Data!", command=sendAuto, bootstyle="success"
        )
        loginButton.pack()

        # TODO: Add response logic for showing the response as soon as the queue is populated

        window.mainloop()

    def socketServer():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", 2008))

        server.listen(2)

        while True:
            # Setting up the server
            client, _ = server.accept()
            message = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 17\r\n\r\nhello How are you?"
            client.send(message.encode())

            clientMessage = client.recv(1024).decode()  # Printing client message

            q.put(clientMessage)

    serverThread = threading.Thread(target=socketServer, daemon=True)
    uiThread = threading.Thread(target=UI)

    # Starting the threads
    uiThread.start()
    serverThread.start()


if __name__ == "__main__":
    main()
