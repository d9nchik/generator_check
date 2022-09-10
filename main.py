from math import log

from src.analyzer import Analyzer
from src.generator import EqualDistributionGenerator

if __name__ == "__main__":
    a_array = [5 ** 13, 5 ** 11, 5 ** 9, 5 ** 5, 5 ** 1]
    c_array = [2 ** 31, 2 ** 21, 2 ** 15, 2 ** 7, 2 ** 3]

    a_c_array_combinations = [(a, c) for a in a_array for c in c_array]

    for a, c in a_c_array_combinations:
        generator = EqualDistributionGenerator(a, c)

        analyzer = Analyzer(generator)
        chi_square, critical_chi_square = analyzer.get_chi_square()
        row = '\t'.join(map(lambda x: str(round(x, 3)).replace('.', ','),
                            [log(a, 5), log(c, 2), analyzer.mean(), analyzer.dispersion(), chi_square,
                             critical_chi_square]))
        print(row)
