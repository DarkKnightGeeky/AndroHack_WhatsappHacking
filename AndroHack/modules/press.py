from ghost.lib.module import Module


class AndroHackModule(Module):
    def __init__(self):
        super().__init__()

        self.details.update({
            'Category': "manage",
            'Name': "press",
            'Authors': [
                'DarkKnightGeeky (cyberlord)- module developer'
            ],
            'Description': "Press device button by keycode.",
            'Usage': "press <keycode>",
            'MinArgs': 1,
            'NeedsRoot': False
        })

    def run(self, argc, argv):
        if int(argv[1]) < 124:
            self.device.send_command(f"input keyevent {argv[1]}")
        else:
            self.print_error("Invalid keycode!")
