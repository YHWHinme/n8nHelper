import os
import queue
import socket
import threading

from streamlit_desktop_app import start_desktop_app


def socket_server():
    """TCP server that listens for incoming messages."""
    answer_queue: queue.LifoQueue = queue.LifoQueue()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 2008))
    server.listen(3)

    while True:
        client, _ = server.accept()
        # message = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 17\r\n\r\nhello How are you?"
        # client.send(message.encode())

        client_message = client.recv(1024).decode()
        answer_queue.put(client_message)


if __name__ == "__main__":
    # Ensuring only using qt, no gtk
    os.environ["WEBVIEW_GUI"] = "qt"
    # Start socket server as daemon thread
    server_thread = threading.Thread(target=socket_server, daemon=True)
    server_thread.start()

    # Launch Streamlit in desktop window
    start_desktop_app(
        "app.py",
        title="n8nHelper",
        options={
            "server.enableCORS": "False",
            "server.enableXsrfProtection": "False",
        },
    )
