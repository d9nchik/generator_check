from src.generator import ExponentialGenerator, NormalGenerator, EqualDistributionGenerator, Generator
from src.analyzer import Analyzer

if __name__ == "__main__":
    lambdas = [0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100, 500]
    for lambd in lambdas:
        generator = ExponentialGenerator(lambd)

        analyzer = Analyzer(generator)
        chi_square, critical_chi_square = analyzer.get_chi_square()
        row = '\t'.join(map(lambda x: str(round(x, 3)).replace('.', ','),
                            [lambd, analyzer.mean(), analyzer.dispersion(), chi_square, critical_chi_square]))
        print(row)
