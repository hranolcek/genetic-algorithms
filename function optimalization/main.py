import random
import numpy as np
import matplotlib.pyplot as plt

# Funkcja tworząca początkową populację o wielkości `pop_size` z wartościami losowymi z przedziału `min_value` i `max-value`


def generate_population(pop_size, min_value, max_value):
    return [random.uniform(min_value, max_value) for i in range(pop_size)]

# Funkcja obliczająca wartość fitness dla danego rozwiązania `solution` na podstawie podanej funkcji


def evaluate_fitness(solution, function):
    return function(solution)

# Funkcja selekcji rodziców na podstawie wartości fitness


def selection(population, fitness_values):
    population_fitness = list(zip(population, fitness_values))
    population_fitness.sort(key=lambda x: x[1], reverse=True)
    population = [x[0] for x in population_fitness]
    # Wybieramy pierwszych dwóch najlepiej dopasowanych jednostek jako rodziców
    parent1 = population[0]
    parent2 = population[1]
    return parent1, parent2

# Funkcja mutacji rodziców z prawdopodobieństwem `mutation_prob`


def mutation(parent1, parent2, mutation_prob):
    if random.random() < mutation_prob:
        parent1 += random.uniform(-1, 1)
    if random.random() < mutation_prob:
        parent2 += random.uniform(-1, 1)
    return parent1, parent2

# Funkcja główna implementująca algorytm genetyczny


def genetic_algorithm(pop_size, num_generations, min_value, max_value, mutation_prob, function):
    # Generujemy początkową populację
    population = generate_population(pop_size, min_value, max_value)
    for i in range(num_generations):
        # Obliczamy wartość fitness dla każdej jednostki w populacji
        fitness_values = [evaluate_fitness(x, function) for x in population]
        # Wybieramy rodziców na podstawie wartości fitness
        parent1, parent2 = selection(population, fitness_values)
        # Mutujemy rodziców
        parent1, parent2 = mutation(parent1, parent2, mutation_prob)
        # Dodajemy rodziców do populacji
        population.append(parent1)
        population.append(parent2)
    fitness_values = [evaluate_fitness(x, function) for x in population]
    best_solution = min(fitness_values)
    return best_solution


def equation(x):
    return x**2 + 5 * x + 4


def visualize(function, min_value, max_value):
    x = np.linspace(min_value, max_value, 1000)
    y = function(x)
    plt.plot(x, y)
    plt.show()


pop_size = 100
num_generations = 100
min_value = -100
max_value = 100
mutation_prob = 0.1

solution = genetic_algorithm(
    pop_size, num_generations, min_value, max_value, mutation_prob, equation)

print("Rozwiązanie równania to: ", solution)
visualize(equation, min_value, max_value)
