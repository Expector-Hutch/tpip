from textual.app import App, ComposeResult
from textual import widgets

from pip._internal.cli.main import main as pip
pip_cli = lambda *args: pip(list(args))

class CFooter(widgets.Input, widgets.Footer):
    ...

class TPip(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("ctrl+q", "exit_app", "Exit")]
    CSS_PATH = "main.css"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield widgets.Header()
        #yield widgets.Footer()
        yield CFooter(id='cmd', placeholder='>_')

    def action_exit_app(self) -> None:
        """Exit the app"""
        self.exit()


if __name__ == "__main__":
    app = TPip()
    app.run()
