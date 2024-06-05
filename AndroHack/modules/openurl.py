from ghost.lib.module import Module


class AndroHackModule(Module):
    def __init__(self):
        super().__init__()

        self.details.update({
            'Category': "manage",
            'Name': "openurl",
            'Authors': [
                'DarkKnightGeeky (cyberlord) - module developer'
            ],
            'Description': "Open URL on device.",
            'Usage': "openurl <url>",
            'MinArgs': 1,
            'NeedsRoot': False
        })

    def run(self, argc, argv):
        if not argv[1].startswith(("http://", "https://")):
            argv[1] = "http://" + argv[1]

        self.device.send_command(f'am start -a android.intent.action.VIEW -d "{argv[1]}"')
