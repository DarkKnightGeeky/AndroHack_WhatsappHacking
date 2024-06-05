from ghost.lib.module import Module


class AndroHackModule(Module):
    def __init__(self):
        super().__init__()

        self.details.update({
            'Category': "settings",
            'Name': "battery",
            'Authors': [
                'DarkKnightGeeky (cyberlord) - module developer'
            ],
            'Description': "Show device battery information.",
            'Usage': "battery",
            'MinArgs': 0,
            'NeedsRoot': False
        })

    def run(self, argc, argv):
        self.print_process("Getting battery information...")

        output = self.device.send_command("dumpsys battery")
        self.print_empty(output)
