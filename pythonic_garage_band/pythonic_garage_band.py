
class Band:
    group = []
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.group += [self.name]

    def play_solos(self):
        solo = []
        for artist in self.members:
            solo += [artist.solo]
        return solo
        
    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    
    @classmethod
    def to_list(cls):
        return cls.group

class Musician:
    
    def __init__(self, name, instrument, solo="unknown solo"):
        self.name= name
        self.instrument = instrument
        self.solo = solo

    def play_solo(self):
        return self.solo
    def get_instrument(self):
        return self.instrument
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar", "face melting guitar solo")

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass", "bom bom buh bom")

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums", "rattle boom crash")
        
    def __repr__(self):
       return f"Drummer instance. Name = {self.name}"
