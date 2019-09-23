# zones.py

def cyberfactory():
    return 'Beep boop'

zone_types = {
    'IND': [{'materials': 8, 'cybernetics': 2}, ':factory:', 0],
    'RES': [{'materials': 8, 'food': 2}, ':homes:', 0],
    'COM': [{'materials': 8}, ':office:', 0],
    'CYB': [{'materials': 8}, ':control_knobs:', cyberfactory]
}

class Zone:
    def __init__(self, zone_type):
        self.name = zone_type
        self.icon = zone_types[zone_type][1]
        self.production = zone_types[zone_type][2]