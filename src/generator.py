from abc import ABC, abstractmethod
from math import log, exp, sqrt
from random import random, randint

from scipy.special import erf


def equal_distributed() -> float:
    while True:
        number = random()
        if number != 0:
            return number


class Generator(ABC):
    def generate(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def F(self, x: float) -> float:
        raise NotImplementedError

    def distribution(self, a: float, b: float) -> float:
        return self.F(b) - self.F(a)


class ExponentialGenerator(Generator):
    def __init__(self, lambd: float) -> None:
        super().__init__()
        self.lambd = lambd

    def generate(self) -> float:
        return -log(equal_distributed()) / self.lambd

    def F(self, x: float) -> float:
        return 1 - exp(-self.lambd * x)


class NormalGenerator(Generator):
    def __init__(self, a: float, sigma: float):
        super().__init__()
        self.a = a
        self.sigma = sigma

    @staticmethod
    def __generate_mu() -> float:
        return sum([random() for _ in range(12)]) - 6

    def generate(self) -> float:
        return self.__generate_mu() * self.sigma + self.a

    @staticmethod
    def getPhi(x: float) -> float:
        return (1 + erf(x / sqrt(2))) / 2

    def F(self, x: float) -> float:
        return self.getPhi((x - self.a) / self.sigma)


class EqualDistributionGenerator(Generator):
    def __init__(self, a: int, c: int):
        super().__init__()
        self.a = a
        self.c = c
        self.previous_z = randint(1, c - 1)

    def __get_z(self) -> int:
        self.previous_z = (self.a * self.previous_z) % self.c
        return self.previous_z

    def generate(self) -> float:
        return self.__get_z() / self.c

    def F(self, x: float) -> float:
        return x
