# resources.py

resource_types = {
    'materials': [1, ':shield:'],
    'cybernetics': [4, ':control_knobs:'],
    'biologicals': [4, ':seedling:'],
    'hitek': [6, ':desktop:'],
    'power': [2,':zap:'],
    'luxuries': [5, ':ring:'],
    'food': [2, ':bread:'],
    'culture': [3, ':performing_arts:'],
    'parts': [3, ':gear:'],
    'crystals': [10, ':gem:'],
    'tools': [4, ':tools:'],
    'weapons': [6, ':gun:'],
    'radioactives': [3, ':radioactive:'],
    'genemods': [5, ':biohazard:']
}

class Resource:
    def __init__(self, name, number=0):
        self.name = name
        self.icon = resource_types[name][1]
        self.nominal_value = resource_types[name][0]
        self.amount = number
