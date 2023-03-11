import random

class KarmaError(Exception):
    pass

class KillError(KarmaError):
    pass

class DrunkError(KarmaError):
    pass

class CarCrashError(KarmaError):
    pass

class GluttonyError(KarmaError):
    pass

class DepressionError(KarmaError):
    pass

class KarmaSimulator:
    def __init__(self):
        self._karma = 0
        self._log = []

    def get_karma(self):
        return self._karma

    def set_karma(self, karma):
        self._karma = karma

    def get_log(self):
        return self._log

    def add_log(self, message):
        self._log.append(message)

    def one_day(self):
        try:
            karma_gain = random.randint(1, 7)
            self.add_log(f"Karma gained: {karma_gain}")
            if random.random() < 0.1:
                raise random.choice([
                    KillError("Killed someone"),
                    DrunkError("Got drunk"),
                    CarCrashError("Had a car crash"),
                    GluttonyError("Ate too much"),
                    DepressionError("Felt into depression")
                ])
            self.set_karma(self.get_karma() + karma_gain)
        except KarmaError as e:
            self.add_log(str(e))

if __name__ == "__main__":
    simulator = KarmaSimulator()
    while simulator.get_karma() < 500:
        simulator.one_day()
    print(f"Enlightenment achieved with {simulator.get_karma()} karma!")
    with open("karma.log", "w") as f:
        f.write("\n".join(simulator.get_log()))
