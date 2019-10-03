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
        self.seed =                     data["seed"]
        # Initalized values
        self.rand =                     random.Random(self.seed)
        self.population = []

    """ Solves the problem using the information given """
    def solve(self):
        self.build_population()

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
        for nodeIndex in range(len(creature['genome']) - 1):
            fitness_score += self.distance_matrix[creature['genome'][nodeIndex]][creature['genome'][nodeIndex + 1]]
        # Finish the loop
        fitness_score += self.distance_matrix[creature['genome'][-1]][creature['genome'][0]]
        return fitness_score

    """ Return the entire poulation """
    def print_population(self):
        for creature in self.population:
            print(creature)
