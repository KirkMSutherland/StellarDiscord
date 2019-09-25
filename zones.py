# zones.py

def cyberfactory():
    return 'Beep boop'

zone_types = {
    'IND': [{'materials': 8, 'cybernetics': 2}, ':factory:', {}, {'materials': 5}],
    'RES': [{'materials': 8, 'food': 2}, ':homes:', {}, {'food': 1}],
    'COM': [{'materials': 8}, ':office:', {}, {'parts': 2}],
    'CYB': [{'materials': 8}, ':control_knobs:', {'materials': 15}, {'parts': 3, 'cybernetics': 2, 'hitek': 1}]
}

class Zone:
    def __init__(self, zone_type):
        self.name = zone_type
        self.icon = zone_types[zone_type][1]
        self.input = zone_types[zone_type][2]
        self.output = zone_types[zone_type][3]
