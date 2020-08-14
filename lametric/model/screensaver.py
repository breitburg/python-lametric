class Screensaver:
    def __init__(self, mode: str, mode_parameters: dict, enabled: bool = True):
        self.mode = mode
        self.mode_parameters = mode_parameters
        self.enabled = enabled

    def to_json(self) -> dict:
        return {'enabled': self.enabled, 'mode': self.mode, 'mode_params': self.mode_parameters}
