# trade.py

class Trade:
    def __init__(self, proposer, partner, offers, wants):
        self.proposer = proposer
        self.partner = partner
        self.offers = offers
        self.wants = wants
        self.msgid = 0