from textual.widget import *
from textual.widgets import Footer


class TFooter(Widget):
    def __init__(self) -> None:
        super().__init__()
        self.keys_footer = Footer()

    def render(self) -> RenderableType:
        return self.keys_footer