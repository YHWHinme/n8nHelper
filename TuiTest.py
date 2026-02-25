from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, VerticalScroll
from textual.widgets import Input, Static


class HelloWorld(App[str]):
    CSS_PATH = "./styled.css"

    def compose(self) -> ComposeResult:
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                for id in range(20):
                    yield Static(f"Element {id + 1}")
            with Vertical(id="sidebar"):
                yield Static("[bold yellow]Hello[/]! What is your name?")
                yield Input(placeholder="Put your name here!")
            yield Static("[yellow bold]Top of the morning[/] to ya!", id="output")


if __name__ == "__main__":
    HelloWorld().run()
