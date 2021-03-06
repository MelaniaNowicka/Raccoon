import random
import eval

random.seed(1)


# one parent selection function
def select_parent(population, tournament_size, first_parent_id):

    """

    Selects single parent.

    Parameters
    ----------
    population : list
        list of Classifier objects
    tournament_size : float
        size of tournament
    first_parent_id : int
        if first parent id is selected block the id, otherwise pass -1

    Returns
    -------
    best_candidate : int
        id of the best candidate

    """

    # create empty tournament
    tournament = []

    # drawing parents from a population without replacement
    for i in range(0, int(tournament_size*len(population))):
        candidate = random.randrange(0, len(population))  # randomly choose a candidate
        while candidate == first_parent_id:  # check if ids of parent are unique
            candidate = random.randrange(0, len(population))
        else:
            tournament.append(candidate)  # add candidate to the tournament

    # choosing the best parent for crossover
    best_candidate = tournament[0]  # assign first in tournament as the best candidate
    for candidate in tournament:  # compare the best candidate to others
        if eval.is_higher(population[best_candidate].score, population[candidate].score):
            best_candidate = candidate  # assign to the best candidate

    return best_candidate


# tournament selection of parents for crossover
def select(population, tournament_size):

    """

    Performs tournament selection of two parents from a population of classifiers.

    Parameters
    ----------
    population : list
        list of Classifier objects
    tournament_size : float
        tournament size

    Returns
    -------
    first_parent_id : int
        id of the first selected parent
    second_parent_id : int
        id of the second selected parent

    """

    # select first parent, parents must have different ids (-1 - no id is blocked)
    first_parent_id = select_parent(population, tournament_size, -1)
    # select second parent (parents must have different ids)
    second_parent_id = select_parent(population, tournament_size, first_parent_id)

    return first_parent_id, second_parent_id
