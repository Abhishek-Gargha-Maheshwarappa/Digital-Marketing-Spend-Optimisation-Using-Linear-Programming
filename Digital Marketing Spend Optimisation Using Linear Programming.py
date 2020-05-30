'''
Digital Marketing Spend Optimisation Using Linear Programming
Linear programming is a simple technique to solve optimisation problems. 
'''


from __future__ import print_function
from ortools.linear_solver import pywraplp

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('Digital Marketing Spend Optimisation Using Linear Programming')


ad = st.slider('Select Adwords Constraint',50000, 250000, (250000))
fb = st.slider('Select FB Constraint',10000, 200000, (200000))
em = st.slider('Select Email Constraint',5000, 75000, (75000))
ac = st.slider('Select Affiliated Constraint',2000, 50000, (50000))
fb_ad = st.slider('Select FB and Adwords Budget Constraint',30000, 600000, (600000))
Budget = st.slider('Select Total Budget Constraint',50000, 1000000, (1000000))


def LinearProgrammingExample():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver('LinearProgrammingExample',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # Create the 4 variables and let them take on any non-negative value.
    B1 = solver.NumVar(0, solver.infinity(), 'B1')
    B2 = solver.NumVar(0, solver.infinity(), 'B2')
    B3 = solver.NumVar(0, solver.infinity(), 'B3')
    B4 = solver.NumVar(0, solver.infinity(), 'B4')


    # Constraint  | B1/250 >=1000
    st.write("ad",ad)
    constraint0 = solver.Constraint(ad, solver.infinity())
    constraint0.SetCoefficient(B1, 1)

    # Constraint  |  B2/200 >=1000
    constraint1 = solver.Constraint(fb, solver.infinity())
    constraint1.SetCoefficient(B2, 1)

    # Constraint 1: 3x - y >= 0. |  B3/150 >=500
    constraint2 = solver.Constraint(em, solver.infinity())
    constraint2.SetCoefficient(B3, 1)

    # Constraint  |  B4/100>=500
    constraint3 = solver.Constraint(ac, solver.infinity())
    constraint3.SetCoefficient(B4, 1)


    # Constraint  B1+B2<=600000
    constraint4 = solver.Constraint(-solver.infinity(), fb_ad)
    constraint4.SetCoefficient(B1, 1)
    constraint4.SetCoefficient(B2, 1)

    # Constraint  B1+B2+B3+B4 <=1000000
    constraint5 = solver.Constraint(-solver.infinity(), Budget)
    constraint5.SetCoefficient(B1, 1)
    constraint5.SetCoefficient(B2, 1)
    constraint5.SetCoefficient(B3, 1)
    constraint5.SetCoefficient(B4, 1)

    

    # Constraint   LTV: +4 Adword +1.5 Facebook -1.33333333333 Email -4 Affiliated >= 0;
    constraint6 = solver.Constraint(0, solver.infinity())
    constraint6.SetCoefficient(B1,4)
    constraint6.SetCoefficient(B2,1.5)
    constraint6.SetCoefficient(B3,-1.333)
    constraint6.SetCoefficient(B4,-4)    



    

    # B1/250+B2/200+B3/100+B4/150
    #max: +0.004 Adword +0.005 Facebook +0.00666666666666 Email +0.01 Affiliated;
    objective = solver.Objective()
    objective.SetCoefficient(B1, 0.004)
    objective.SetCoefficient(B2, 0.005)
    objective.SetCoefficient(B3, 0.00666666666666)
    objective.SetCoefficient(B4, 0.01)
    objective.SetMaximization()

    # Solve the system.
    solver.Solve()
    opt_solution = (0.004) * B1.solution_value() + (0.005) * B2.solution_value()+(0.006667) * B3.solution_value()+(0.01) * B4.solution_value()
    st.write('Number of variables =', solver.NumVariables())
    st.write('Number of constraints =', solver.NumConstraints())
    # The value of each variable in the solution.
    st.write('Solution:')
    st.write('B1 = ', B1.solution_value())
    st.write('B2 = ', B2.solution_value())
    st.write('B3 = ', B3.solution_value())
    st.write('B4 = ', B4.solution_value())
    # The objective value of the solution.
    st.write('Optimal objective value =', opt_solution)


LinearProgrammingExample()

'''
Copyright 2020 Abhishek Maheshwarappa and Sri Krishnamurthy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
 SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
 '''