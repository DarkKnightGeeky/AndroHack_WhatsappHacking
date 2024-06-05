from ghost.lib.module import Module


class AndroHackModule(Module):
    def __init__(self):
        super().__init__()

        self.details.update({
            'Category': "manage",
            'Name': "shell",
            'Authors': [
                'DarkKnightGeeky (cyberlord)- module developer'
            ],
            'Description': "Execute shell command on device.",
            'Usage': "shell <command>",
            'MinArgs': 1,
            'NeedsRoot': False
        })

    def run(self, argc, argv):
        output = self.device.send_command(' '.join(argv[1:]))
        self.print_empty(output)
