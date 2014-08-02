import os
from lutris import settings
from lutris.runners.runner import Runner


class pcsx2(Runner):
    """Playstation 2 emulator"""
    platform = "Playstation 2"
    executable = "pcsx2.sh"
    game_options = [{
        "option": "iso",
        "type": "file",
        "label": "ISO disc image"
    }]
    runner_options = [
        {
            "option": "nogui",
            "type": "bool",
            "label": "Show GUI",
            "default": False
        },
        {
            "option": "fullscreen",
            "type": "bool",
            "label": "Fullscreen",
            "default": True
        }
    ]

    def get_executable(self):
        return os.path.join(settings.RUNNER_DIR, 'pcsx2/pcsx2.sh')

    def play(self):
        command = [self.get_executable()]

        if self.runner_config.get('nogui'):
            command.append('--nogui')

        if self.runner_config.get('fullscreen'):
            command.append('--fullscreen')
        else:
            command.append('--windowed')

        iso = self.settings['game']['iso']
        # current version of pcsx2 is broken for names with spaces
        command.append("\"%s\"" % iso)
        return {'command': command}
