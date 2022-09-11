from src.analyzer import Analyzer
from src.generator import NormalGenerator

if __name__ == "__main__":
    a_array = [0.01, 0.1, 1, 10, 100]
    sigma_array = [0.01, 0.1, 1, 10, 100]

    a_sigma_array_combinations = [(a, sigma) for a in a_array for sigma in sigma_array]

    for a, sigma in a_sigma_array_combinations:
        generator = NormalGenerator(a, sigma)

        analyzer = Analyzer(generator)
        analyzer.show_frequency_histogram()
        chi_square, critical_chi_square = analyzer.get_chi_square()
        row = '\t'.join(map(lambda x: str(round(x, 3)).replace('.', ','),
                            [a, sigma, analyzer.mean(), analyzer.dispersion(), chi_square,
                             critical_chi_square]))
        print(row)
