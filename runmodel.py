import mymodel as m
from pysb.simulator import ScipyOdeSimulator
import pylab as pl
from __future__ import print_function
from pysb.bng import generate_network, generate_equations
import re

# generate ODEs
bng_code = generate_network(m.model)
generate_equations(m.model)
for species, ode in zip(m.model.species, m.model.odes):
	print("%s: %s" % (species, ode))

# simulation
t = pl.linspace(0, 90)
simres = ScipyOdeSimulator(m.model, tspan=t).run()
yout = simres.all
pl.ion()
pl.figure()
pl.plot(t, yout['obsS'], label="Susceptible")
pl.plot(t, yout['obsE'], label="Exposed")
pl.plot(t, yout['obsIA'], label="Infectious Asymptomatic")
pl.plot(t, yout['obsIS'], label="Infectious Symptomatic")
pl.plot(t, yout['obsR'], label="Recovered")
pl.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
pl.legend()
pl.xlabel("Time (days)")
pl.ylabel("Number of individuals")
pl.show()
