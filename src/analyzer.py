from typing import Tuple

from src.generator import Generator
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter
from scipy.stats import chi2


def get_chi_square_critical(bins: int) -> float:
    return chi2.ppf(0.95, bins)


class Analyzer:
    def __init__(self, generator: Generator) -> None:
        self.generator = generator
        self.size = 10_000
        self.data = np.array([generator.generate() for _ in range(self.size)])

    def show_frequency_histogram(self) -> None:
        # create relative frequency histogram with percentages on y-axis
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.hist(self.data, edgecolor='black', weights=np.ones_like(self.data) * 100 / len(self.data))
        ax.yaxis.set_major_formatter(PercentFormatter())
        plt.show()

    def mean(self) -> float:
        return self.data.mean()

    def dispersion(self) -> float:
        return self.data.var()

    def get_chi_square(self) -> Tuple[float, float]:
        histogram, buckets = np.histogram(self.data)

        previous_bucket = buckets[0]
        buckets_pairs = []
        for bucket in buckets[1:]:
            buckets_pairs.append((previous_bucket, bucket))
            previous_bucket = bucket

        expected_values = [self.generator.distribution(a, b) * self.size for a, b in buckets_pairs]

        chi_square = 0
        for expected, actual in zip(expected_values, histogram):
            chi_square += (actual - expected) ** 2 / expected

        return chi_square, get_chi_square_critical(len(buckets_pairs) - 1)
