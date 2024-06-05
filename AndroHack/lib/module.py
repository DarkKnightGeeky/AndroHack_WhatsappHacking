from badges import Badges, Tables


class Module(Badges, Tables):
    """ Subclass of ghost.lib module.

    This subclass of ghost.lib module is intended for providing
    wrapper for a module.
    """

    def __init__(self) -> None:
        super().__init__()

        self.device = None

        self.details = {
            'Category': "",
            'Name': "",
            'Authors': [
                ''
            ],
            'Description': "",
            'Usage': "",
            'MinArgs': 0,
            'NeedsRoot': False
        }

    def run(self, argc: int, argv: list) -> None:
        """ Run this module.

        :param int argc: number of arguments
        :param list argv: arguments
        :return None: None
        """

        pass
