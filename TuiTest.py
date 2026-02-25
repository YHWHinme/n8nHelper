from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Static


class HelloWorld(App[str]):
    CSS_PATH = "./styled.css"

    def compose(self) -> ComposeResult:
        yield Static("HelloWorld!")
        yield Label("Boolean Value test")
        yield Button("Yes", id="yes")
        yield Button("No", id="no")

        def on_button_pressed(self, event) -> None:
            self.exit(event.button.id)


if __name__ == "__main__":
    reply = HelloWorld().run()
    print(reply)
