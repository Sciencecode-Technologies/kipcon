import requests


class Bety:
    def __init__(self, x: int = 3, y: int = 1):
        self.v1 = x
        self.v2 = y

        self.r = requests.get(url="https://suhaarslan.com")

    def cross(self, n: int = 2):
        a = 0
        for i in range(n):
            a = a+self.v1
            a = a*self.v2
            a = a**(1/2)
            self.v1 = self.v2 * a/self.v1

        return a

    def stat(self):
        return self.r.status_code
