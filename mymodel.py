# import the pysb module and all its methods and functions
from pysb import *

# instantiate a model
Model()

# basis for model: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7376536/

# declare monomers
Monomer('S') # susceptible individuals 
Monomer('E') # exposed 
Monomer('IA') # asymptomatic infectious 
Monomer('IS') # symptomatic infectious 
Monomer('R') # recovered

# observables
Observable('obsS', S())
Observable('obsE', E())
Observable('obsIA', IA())
Observable('obsIS', IS())
Observable('obsR', R())

# parameter values
Parameter('b', 0.00018) # birth rate
Parameter('mu', 4.563E-5) # natural death rate
Parameter('alpha2', 0.1) # proportion of interaction with infectious individual
Parameter('beta2', 0.0115) # rate of transmission from S to E due to contact with infectious individuals
Parameter('delta', 0.7) # proportion of symptomatic infectious people
Parameter('psi', 0.0051) # progression rate from E back to S (due to robust immune system)
Parameter('omega', 0.09) # progression rate from E to infectious population 
Parameter('sigma', 0.0018) # COVID-19 death rate
Parameter('gams', 0.05) # symptomatic rate of recovery
Parameter('gama', 0.0714) # asymptomatic rate of recovery 

# expressions 
Expression('kf_SE', (beta2*(obsIA+obsIS))/(1+alpha2*(obsIA+obsIS)))
Expression('kf_EIS', delta*omega)
Expression('kf_EIA', (1-delta)*omega)
Expression('out_I', mu+sigma)

# rules
Rule('io_S', None | S(), b, mu)
Rule('StoE', S() | E(), kf_SE, psi)
Rule('EtoIS', E() >> IS(), kf_EIS)
Rule('EtoIA', E() >> IA(), kf_EIA)
Rule('IStoR', IS() >>  R(), gams)
Rule('IAtoR', IA() >> R(), gama)
Rule('o_E', E() >> None, mu)
Rule('o_IA', IS() >> None, out_I) 
Rule('o_IS', IA() >> None, out_I)
Rule('o_R', R() >> None, mu)

# initial conditions 
Initial(S(), Parameter('S_0', 93000))
Initial(E(), Parameter('E_0', 1000))
Initial(IA(), Parameter('IA_0', 50))
Initial(IS(), Parameter('IS_0', 50))
Initial(R(), Parameter('R_0', 0))
