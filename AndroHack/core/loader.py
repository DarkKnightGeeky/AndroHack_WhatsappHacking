import importlib.util
import os

from typing import Any


class Loader(object):
    """ Subclass of ghost.core module.

    This subclass of ghost.core module is intended for providing
    AndroHack loader.
    """

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def import_modules(path: str, device: Any) -> dict:
        """ Import modules for the specified device.

        :param str path: path to import modules from
        :param Any device: device to import modules for
        :return dict: dict of modules
        """

        modules = {}

        for mod in os.listdir(path):
            if mod == '__init__.py' or mod[-3:] != '.py':
                continue
            else:
                try:
                    spec = importlib.util.spec_from_file_location(path + '/' + mod, path + '/' + mod)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    module = module.GhostModule()

                    module.device = device
                    modules[module.details['Name']] = module
                except Exception:
                    pass

        return modules

    def load_modules(self, device) -> dict:
        """ Load modules for the specified device and get their commands.

        :param Device device: device to load modules for
        :return dict: dict of modules commands
        """

        return self.import_modules(f'{os.path.dirname(os.path.dirname(__file__))}/modules', device)
