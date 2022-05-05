

from random import randint


def populate(families):
    """
    0: For a boy
    1: For a girl
    """
    population = []
    for fam in range(0, families):
        child = randint(0, 1)
        population.append(child)
        while child == 0:
            child = randint(0, 1)
            population.append(child)

    print(sum(population) / len(population))

def main():
    populate(9999)


if __name__ == '__main__':
    main()

