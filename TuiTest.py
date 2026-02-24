from textual.app import App
from textual.widgets import Label, Static


class HelloWorld(App):
    CSS_PATH = "./styled.css"

    def compose(self):
        yield Static("HelloWorld!", classes="helloStyle1")
        yield Label("What is your[red bold] name?[red/] Child?", classes="style1")

    def on_key(self, event):
        match event.on_key:
            case "q":
                exit()


if __name__ == "__main__":
    HelloWorld().run()
