from textual.widget import *
from textual.widgets import Input

import os

class Command(Input):
    async def action_submit(self) -> None:
        """Handle a submit action (normally the user hitting Enter in the input)."""
        await self.post_message(self.Submitted(self, self.value))
        os.system(self.value)
        self.value = ''