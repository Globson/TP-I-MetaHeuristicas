from numpy.random import seed, rand, randn
from numpy import pi, e, sin, sqrt, exp, asarray
from HC import hillclimbing, in_bounds

def ils():
    return


# iterated local search of the ackley objective function

# objective function

def objective(v):
	x, y = v
	return (sin(x+y) + pow(x-y, 2) - 1.5*x + 2.5*y + 1)

# iterated local search algorithm

def iterated_local_search(objective, bounds, n_iter, step_size, n_restarts, p_size):
	# define starting point
	best = None
	while best is None or not in_bounds(best, bounds):
		best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	# evaluate current best point
	best_eval = objective(best)
	# enumerate restarts
	for n in range(n_restarts):
		# generate an initial point as a perturbed version of the last best
		start_pt = None
		while start_pt is None or not in_bounds(start_pt, bounds):
			start_pt = best + randn(len(bounds)) * p_size
		# perform a stochastic hill climbing search
		solution, solution_eval = hillclimbing(
		    objective, bounds, n_iter, step_size, start_pt)
		# check for new best
		if solution_eval < best_eval:
			best, best_eval = solution, solution_eval
			print('Restart %d, best: f(%s) = %.5f' % (n, best, best_eval))
	return [best, best_eval]



