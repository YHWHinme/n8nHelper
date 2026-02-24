from textual.app import App
from textual.widgets import Static

class HelloWorld(App):
    def compose(self):
        yield Static("HelloWorld")
if __name__ == "__main__":
    HelloWorld().run()
