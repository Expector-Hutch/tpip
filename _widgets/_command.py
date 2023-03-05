from textual.widget import *
from textual.widgets import Input

from pip._internal.cli.main import main as pip_run


class Command(Input):
    async def action_submit(self) -> None:
        """Handle a submit action (normally the user hitting Enter in the input)."""
        await self.post_message(self.Submitted(self, self.value))
        pip_run(self.value.split())
        self.value = ''