import datetime

from ghost.lib.module import Module


class AndroHackModule(Module):
    def __init__(self):
        super().__init__()

        self.details.update({
            'Category': "manage",
            'Name': "list",
            'Authors': [
                'DarkKnightGeeky (cyberlord) - module developer'
            ],
            'Description': "List directory contents.",
            'Usage': "list <remote_path>",
            'MinArgs': 1,
            'NeedsRoot': False
        })

    def run(self, argc, argv):
        output = self.device.list(argv[1])

        if output:
            headers = ('Name', 'Mode', 'Size', 'Modification Time')
            data = list()

            for entry in sorted(output):
                timestamp = datetime.datetime.fromtimestamp(entry[3])
                data.append((entry[0].decode(), str(entry[1]), str(entry[2]), timestamp))

            self.print_table(f"Directory {argv[1]}", headers, *data)
