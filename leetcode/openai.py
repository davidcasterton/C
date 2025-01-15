import copy

class GPU:
    def __init__(self):
        self._grant = {}
        self._subtract = {}
        self._expire = {}

    def grant(self, amount, start, end):
        self._grant[start] = amount
        self._expire[end] = amount

    def subtract(self, amount, time):
        self._subtract[time] = amount

    def get_balance(self, time):
        balance = 0
        times = sorted(list(self._grant.keys()) + list(self._expire.keys()) + list(self._subtract.keys()))

        expirations = copy.deepcopy(self._expire)

        for i in range(len(times)):
            t = times[i]

            if t in self._grant:
                balance += self._grant[t]
            if t in expirations:
                balance -= expirations[t]
            if t in self._subtract:
                balance -= self._subtract[t]

                exp_to_remove = self._subtract[t]
                for k in range(i, len(times)):
                    _t = times[k]
                    if _t in expirations:
                        if expirations[_t] <= exp_to_remove:
                            exp_to_remove -= expirations[_t]
                            del expirations[_t]
                        else:
                            expirations[_t] -= exp_to_remove
                            exp_to_remove = 0
                            break

            if t >= time:
                break
        print(balance)
        return balance


g = GPU()
g.get_balance(1)
g.subtract(1, 5)
g.grant(2, 2, 10)
g.get_balance(2)
g.get_balance(9)
g.get_balance(10)
