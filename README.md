# 2D Orbital Simulation

This project simulates a two dimensional orbit using Newton’s law of gravity. I wanted to see how orbital motion behaves when you actually compute it step by step instead of solving it analytically. The program updates position and velocity over time using a simple numerical method and tracks the system’s total mechanical energy.

For a circular orbit with radius 1, the total energy should stay close to −0.5. In practice, I observed that energy can drift depending on the time step and integration method. This helped me understand how small numerical errors can change a physical system.

How to Run

Install numpy and matplotlib, then run:

python simulation.py

The program plots the orbit and the total energy over time.
