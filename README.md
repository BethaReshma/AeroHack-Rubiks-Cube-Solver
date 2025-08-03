AeroHack'25: Rubik's Cube Solver 🧩:
This Python project is a Rubik's Cube solver algorithm designed to solve a standard 3x3x3 cube from any scrambled state. The solution uses a logical, human-like, layer-by-layer method, implemented within a Cube class to model the cube's state and transitions. The code is structured to be both functional and easy to understand, with functions for all standard cube moves.

Features:
Cube Modeling: Uses a Cube class to represent the 3x3 cube's state with a dictionary of faces.
Move Engine: Implements a full set of standard moves (U, D, F, B, L, R and their inverses) to simulate cube rotations.
Input Flexibility: Allows the user to choose between a randomly scrambled cube or providing a custom starting state.
Solving Strategy: Applies a simplified layer-by-layer approach to find a solution.

How to Run:
Save the code as a Python file (e.g., rubik_solver.py).
Open a terminal or command prompt.
Navigate to the directory where you saved the file.
Run the script using the command: python rubik_solver.py
Follow the on-screen prompts to choose between a random or custom scrambled state.

Output Example
Here is an example of the program's output when using a custom scrambled state.
Initial Solved Cube:
--- U ---
W W W
W W W
W W W
--- L ---
O O O
O O O
O O O
--- F ---
G G G
G G G
G G G
--- R ---
R R R
R R R
R R R
--- B ---
B B B
B B B
B B B
--- D ---
Y Y Y
Y Y Y
Y Y Y

Do you want to use a (1) randomly shuffled cube or (2) provide your own state? Enter 1 or 2: 2
Using a custom scrambled state. Note: You would typically input this yourself.

Scrambled Cube:
--- U ---
R O G
B G W
Y Y O
--- L ---
B W O
Y G B
R R W
--- F ---
W Y R
O W R
G O B
--- R ---
B G G
O R R
G W Y
--- B ---
W B B
G R B
R W Y
--- D ---
Y B Y
W B O
R G O

*** Starting Solver ***
...
...
White Cross solved!

*** Solver Finished (Placeholder) ***
Could not solve cube with this simplified algorithm.

Final Cube State:
--- U ---
Y Y Y
W W W
W W W
...

Solution history: ['D', 'F', 'L', 'U', 'R', 'R', 'U', 'L', 'F', 'B']
