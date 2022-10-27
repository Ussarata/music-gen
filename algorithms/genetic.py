from random import *
from typing import *

Genome = List[int]


def create_genome(len):
    genome = choices([0, 1], k=len)
    return genome


def create_population(population_size, genome_len):
    population = [create_genome(genome_len) for i in range(population_size)]
    return population


def single_point_crossover(genome_a, genome_b):
    if len(genome_a) != len(genome_b):
        raise ValueError("Both genomes must have the same length")

    length = len(genome_a)
    if length < 2:
        return genome_a, genome_b

    point = randint(1, length - 1)
    return genome_a[0:point] + genome_b[point:], genome_b[0:point] + genome_a[point:]


def mutate(genome, num, probability):
    for i in range(num):
        index = randrange(len(genome))
        if random() <= probability:
            genome[index] = abs(genome[index] - 1) 
    return genome


def population_fitness(population, fitness_func):
    fitness_array = [fitness_func(genome) for genome in population]
    fitness_sum = sum(fitness_array)
    return fitness_sum


def select_pair(population, fitness_func):
    return sample(
        population=create_weighted_distribution(population, fitness_func),
        k=2
    )


def create_weighted_distribution(population, fitness_func):
    result = []

    for genome in population:
        result += [genome] * int(fitness_func(genome)+1)

    return result


def sort_population(population, fitness_func):
    return sorted(population, key=fitness_func, reverse=True)
