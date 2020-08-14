class Text:
    def __init__(self, text: str, icon: int = None):
        self.icon = icon
        self.text = text

    def to_json(self) -> dict:
        result = {'text': self.text}

        if self.icon:
            result['icon'] = self.icon

        return result


class Goal:
    def __init__(self, start: int, current: int, end: int, unit: str = '%', icon: int = None):
        self.icon = icon
        self.start = start
        self.current = current
        self.end = end
        self.unit = unit

    def to_json(self) -> dict:
        result = {'goalData': {'start': self.start, 'current': self.current, 'end': self.end, 'unit': self.unit}}

        if self.icon:
            result['icon'] = self.icon

        return result


class Chart:
    def __init__(self, points: list):
        self.points = points

    def to_json(self) -> dict:
        return {'chartData': self.points}
