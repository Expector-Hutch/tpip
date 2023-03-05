from textual.app import App, ComposeResult
from textual import widgets

from pip._internal.cli.main import main as pip
pip_cli = lambda *args: pip(list(args))


class TPip(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("ctrl+q", "quit_app", "Quit"),
                ("ctrl+p", "open_cmd", "Command")]
    CSS_PATH = "main.css"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield widgets.Header()
        yield widgets.Footer()
        yield widgets.Input(id='cmd')

    def action_quit_app(self) -> None:
        """Exit the app"""
        self.exit()

    def action_open_cmd(self) -> None:
        self.query_one("Footer").display, self.query_one("#cmd").display = self.query_one("#cmd").display, self.query_one("Footer").display


if __name__ == "__main__":
    app = TPip()
    app.run()
