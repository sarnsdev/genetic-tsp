import random

class EvolutionarySolver(object):
    """docstring for EvolutionarySolver."""
    def __init__(self, data):
        super(EvolutionarySolver, self).__init__()
        # From input data
        self.distance_matrix =          data["distance_matrix"]
        self.depot =                    data["depot"]
        self.num_vehicles =             data["num_vehicles"]
        self.starting_population_size = data["starting_population_size"]
        self.children_per_gen =         10
        self.max_population_size =      20
        self.muation_chance =           0.01
        self.max_generations =          100
        self.seed =                     data["seed"]
        # Initalized values
        self.rand =                     random.Random(self.seed)
        self.population = []
        self.current_generation = 0

    """ Solves the problem using the information given """
    def solve(self):
        self.build_population()
        running = True
        while running:
            self.run_generation()
            if self.current_generation >= self.max_generations :
                break
            self.current_generation += 1
        self.print_population()


    """ Runs a single generation of our optimizer """
    def run_generation(self):
        # make a new number of children based on the number given in internal variable children_per_gen
        for new_children in range(self.children_per_gen):
            self.mate()
        self.survival_selection()

    """ Builds the initial population by iterating over a range of the starting pop size """
    def build_population(self):
        for starting_children in range(self.starting_population_size):
            self.population.append(self.random_valid_solution())

    """ Builds a valid soluion based on the problem set """
    def random_valid_solution(self):
        # Instantiate a creature
        creature = {}
        # Instantiate the genome inside
        creature['genome'] = []
        # Add your depot to the front of the genome array since you have to start and finish there
        creature['genome'].append(self.depot)
        # make a holding list to store all locations that have not been vistied and remove the depot from that list
        not_visited = list(range(len(self.distance_matrix[0])))
        not_visited.remove(self.depot)
        # While we still have not visited every node
        while len(not_visited) > 0:
            # Choose a random unvisited node and append it to the genome
            creature['genome'].append(self.rand.choice(not_visited))
            # remove the newly visited node from the unvisited list
            not_visited.remove(creature['genome'][-1])
        creature['fitness'] = self.get_fitness(creature)
        return creature

    """ Get the fitness score for the child """
    def get_fitness(self, creature):
        # initialize score at zero
        fitness_score = 0
        # Iterate over the entire genome starting with index 0 and finishing at last element
        for node_index in range(len(creature['genome']) - 1):
            # add the distance between this node and the next one to the current fitness score
            fitness_score += self.distance_matrix[creature['genome'][node_index]][creature['genome'][node_index + 1]]
        # Finish the loop
        fitness_score += self.distance_matrix[creature['genome'][-1]][creature['genome'][0]]
        return fitness_score

    """ Return the entire poulation """
    def print_population(self):
        for creature in self.population:
            print(creature)

    """ Mate two creatures together """
    def mate(self):
        # select one parent from the list
        # select another parent from the list
        # use another function here to generate a child based on one of the multiary breeding methods
        # feed it through the mutate function
        pass

    def survival_selection(self):
        # sort based on fitness
        # truncate the best amount equal to max_population_size
        pass

    def mutate(self, creature):
        # generate a random number between 0 and 1 using the rand instantiated in the solver
        # if that is less than the mutation chance swap two value random values based on an integer chosen via rand range
        pass
