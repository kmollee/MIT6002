##A Hierarchy of Open-source Python Libraries

-	`NumPy` adds vectors, matrices, and many high-level mathematical functions
-	`Scipy` adds mathematical classes and functions useful to scientists
-	`MatPlotLib` adds an object-oriented `API` for plotting
-	`PyLab` combines the other libraries to provide a MATLAB-like interface

LINKS FROM LECTURE
------------------

[pyplot summary](http://matplotlib.org/api/pyplot_summary.html)

[scipy getting-started](http://scipy.org/getting-started.html)

[matplotlib customizing](http://matplotlib.sourceforge.net/users/customizing.html)

pylab.plot
----------

The first two arguments to `pylab.plot` must be sequences of the same length

First argument gives x-coordinates

Second argument gives y-coordinates

Points plotted in order. As each point is plotted, a line is drawn connecting it to the previous point.

Example: Mortgage calculation
-----------------------------

-	Problem:
	-	Amount to borrow: $200,000
	-	Term: 30 years
	-	Bank has offered three options
		-	30 year fixed rate of 7%
		-	Pay 3.5 % up front "points", get 30 year fixed rate of 5%
		-	48 months with rate of 5%, then rate increases to 9.5%
-	Which is the best deal?

Simulation Models
-----------------

-	Simulation attempts to build an experimental device call a model(descriptive not prescriptive)
-	Simulation models can be classified along three way
	1.	Deterministic vs Stochastic
	2.	Static vs Dynamic
	3.	Discrete vs Continuous
-	Deterministic(Rerunning the simulation will not change the result)
-	Stochastic simulations include randomness(Different runs can generate different result)
-	In a discrete model, value of variables of enumerable(e.g., integers). In a continuous model, they are not enumerable(e.g., real numbers).

