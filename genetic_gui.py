import random
import tkinter as tk
from tkinter import messagebox

# Define the problem and fitness function
def fitness_function(individual):
    # Modify the fitness function according to your requirements
    fitness = sum(individual) + random.uniform(0, 1)
    return fitness

# Create an initial population
def create_population(population_size, genome_length):
    population = []
    for i in range(population_size):
        individual = [random.randint(0, 1) for j in range(genome_length)]
        population.append(individual)
    return population

# Select the fittest individuals from the population
def natural_selection(population, fitness_function, num_parents):
    fitness_scores = [fitness_function(individual) for individual in population]
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
    return sorted_population[:num_parents]

# Perform crossover on the selected parents
def crossover(parents, offspring_size):
    offspring = []
    while len(offspring) < offspring_size:
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        crossover_point = random.randint(0, len(parent1)-1)
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
        offspring.append(offspring1)
        offspring.append(offspring2)
    return offspring[:offspring_size]

# Perform mutation on the offspring
def mutation(offspring, mutation_rate):
    for individual in offspring:
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                individual[i] = 1 - individual[i]
    return offspring

# Define the genetic algorithm
def genetic_algorithm(population_size, genome_length, fitness_function, num_parents, offspring_size, mutation_rate, num_generations):
    population = create_population(population_size, genome_length)
    for i in range(num_generations):
        parents = natural_selection(population, fitness_function, num_parents)
        offspring = crossover(parents, offspring_size)
        offspring = mutation(offspring, mutation_rate)
        population = parents + offspring
        
        # Display the top 3 individuals in the current generation
        print("Generation:", i+1)
        sorted_population = sorted(population, key=fitness_function, reverse=True)
        for j in range(3):
            print("Individual", j+1, ":", sorted_population[j])
        
    best_individual = max(population, key=fitness_function)
    fitness_score = fitness_function(best_individual)
    
    return best_individual, fitness_score

# Function to handle the button click event
def run_genetic_algorithm():
    # Get parameter values from user input
    population_size = int(population_size_entry.get())
    genome_length = int(genome_length_entry.get())
    num_parents = int(num_parents_entry.get())
    offspring_size = int(offspring_size_entry.get())
    mutation_rate = float(mutation_rate_entry.get())
    num_generations = int(num_generations_entry.get())
    
    # Run the genetic algorithm
    best_individual, fitness_score = genetic_algorithm(population_size, genome_length, fitness_function,
                                                      num_parents, offspring_size, mutation_rate,
                                                      num_generations)
    
    # Display the results in a message box
    messagebox.showinfo("Genetic Algorithm Results", f"Best individual: {best_individual}\nFitness score: {fitness_score}")

# Create the main window
window = tk.Tk()
window.title("Genetic Algorithm")
window.geometry("300x300")

# Create labels and entry fields for parameter input
population_size_label = tk.Label(window, text="Population Size:")
population_size_label.pack()
population_size_entry = tk.Entry(window)
population_size_entry.pack()

genome_length_label = tk.Label(window, text="Genome Length:")
genome_length_label.pack()
genome_length_entry = tk.Entry(window)
genome_length_entry.pack()

num_parents_label = tk.Label(window, text="Number of Parents:")
num_parents_label.pack()
num_parents_entry = tk.Entry(window)
num_parents_entry.pack()

offspring_size_label = tk.Label(window, text="Offspring Size:")
offspring_size_label.pack()
offspring_size_entry = tk.Entry(window)
offspring_size_entry.pack()

mutation_rate_label = tk.Label(window, text="Mutation Rate:")
mutation_rate_label.pack()
mutation_rate_entry = tk.Entry(window)
mutation_rate_entry.pack()

num_generations_label = tk.Label(window, text="Number of Generations:")
num_generations_label.pack()
num_generations_entry = tk.Entry(window)
num_generations_entry.pack()

# Create the button to run the genetic algorithm
run_button = tk.Button(window, text="Run", command=run_genetic_algorithm)
run_button.pack()

# Start the main event loop
window.mainloop()
