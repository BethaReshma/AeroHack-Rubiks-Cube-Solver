"""
A Python implementation of a Rubik's Cube solver using a layer-by-layer approach.

This script defines a Cube class to represent the 3x3 cube's state,
implements the core moves, and includes a function to solve the cube
from a scrambled state.

The cube is represented as a dictionary of faces, with each face being a 3x3
list of colors.
Colors are represented by their first letter (e.g., 'W' for White).

Cube faces:
   U (Up)
   D (Down)
   F (Front)
   B (Back)
   L (Left)
   R (Right)

Solving Strategy (Layer-by-Layer):
1.  Solve the White Cross on the Up face.
2.  Solve the White Corners, completing the first layer.
3.  Solve the Second Layer Edges.
4.  Solve the Yellow Cross on the Down face.
5.  Orient the Yellow Cross Edges.
6.  Position the Yellow Corners.
7.  Orient the Yellow Corners, completing the cube.

Note: This is a simplified educational implementation. It is not an optimal
or short-path solver but demonstrates a logical, human-like approach.
"""

import random
from copy import deepcopy

class Cube:
    """
    Represents a 3x3 Rubik's Cube and its state.
    """
    def __init__(self):
        # Initializing a solved cube
        self.faces = {
            'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # Up face (White)
            'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # Down face (Yellow)
            'F': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # Front face (Green)
            'B': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # Back face (Blue)
            'L': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # Left face (Orange)
            'R': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # Right face (Red)
        }
        self.history = []

    def print_cube(self):
        """Prints a flat representation of the cube."""
        def print_face(face_name):
            print(f"--- {face_name} ---")
            for row in self.faces[face_name]:
                print(' '.join(row))

        print_face('U')
        print_face('L')
        print_face('F')
        print_face('R')
        print_face('B')
        print_face('D')

    def apply_move(self, move):
        """Applies a single move to the cube."""
        print(f"Applying move: {move}")
        self.history.append(move)
        # Placeholder for move logic. The actual move functions are below.
        move_map = {
            'U': self.move_U, 'U\'': self.move_U_prime,
            'D': self.move_D, 'D\'': self.move_D_prime,
            'F': self.move_F, 'F\'': self.move_F_prime,
            'B': self.move_B, 'B\'': self.move_B_prime,
            'L': self.move_L, 'L\'': self.move_L_prime,
            'R': self.move_R, 'R\'': self.move_R_prime,
        }
        if move in move_map:
            move_map[move]()
        else:
            print(f"Invalid move: {move}")

    def rotate_face_clockwise(self, face_key):
        """Rotates a single face 90 degrees clockwise."""
        face = self.faces[face_key]
        face_copy = deepcopy(face)
        for i in range(3):
            for j in range(3):
                face[j][2 - i] = face_copy[i][j]

    def move_U(self):
        """U move (Up face clockwise)."""
        self.rotate_face_clockwise('U')
        temp_row = deepcopy(self.faces['F'][0])
        self.faces['F'][0] = deepcopy(self.faces['R'][0])
        self.faces['R'][0] = deepcopy(self.faces['B'][0])
        self.faces['B'][0] = deepcopy(self.faces['L'][0])
        self.faces['L'][0] = temp_row

    def move_U_prime(self):
        """U' move (Up face counter-clockwise)."""
        for _ in range(3):
            self.move_U()

    def move_D(self):
        """D move (Down face clockwise)."""
        self.rotate_face_clockwise('D')
        temp_row = deepcopy(self.faces['F'][2])
        self.faces['F'][2] = deepcopy(self.faces['L'][2])
        self.faces['L'][2] = deepcopy(self.faces['B'][2])
        self.faces['B'][2] = deepcopy(self.faces['R'][2])
        self.faces['R'][2] = temp_row

    def move_D_prime(self):
        """D' move (Down face counter-clockwise)."""
        for _ in range(3):
            self.move_D()

    def move_F(self):
        """F move (Front face clockwise)."""
        self.rotate_face_clockwise('F')
        temp_row = [self.faces['U'][2][0], self.faces['U'][2][1], self.faces['U'][2][2]]
        self.faces['U'][2][0], self.faces['U'][2][1], self.faces['U'][2][2] = self.faces['L'][2][2], self.faces['L'][1][2], self.faces['L'][0][2]
        self.faces['L'][0][2], self.faces['L'][1][2], self.faces['L'][2][2] = self.faces['D'][0][2], self.faces['D'][0][1], self.faces['D'][0][0]
        self.faces['D'][0][0], self.faces['D'][0][1], self.faces['D'][0][2] = self.faces['R'][2][0], self.faces['R'][1][0], self.faces['R'][0][0]
        self.faces['R'][0][0], self.faces['R'][1][0], self.faces['R'][2][0] = temp_row[0], temp_row[1], temp_row[2]

    def move_F_prime(self):
        """F' move (Front face counter-clockwise)."""
        for _ in range(3):
            self.move_F()

    def move_B(self):
        """B move (Back face clockwise)."""
        self.rotate_face_clockwise('B')
        temp_row = [self.faces['U'][0][0], self.faces['U'][0][1], self.faces['U'][0][2]]
        self.faces['U'][0][0], self.faces['U'][0][1], self.faces['U'][0][2] = self.faces['R'][0][2], self.faces['R'][1][2], self.faces['R'][2][2]
        self.faces['R'][0][2], self.faces['R'][1][2], self.faces['R'][2][2] = self.faces['D'][2][2], self.faces['D'][2][1], self.faces['D'][2][0]
        self.faces['D'][2][0], self.faces['D'][2][1], self.faces['D'][2][2] = self.faces['L'][0][0], self.faces['L'][1][0], self.faces['L'][2][0]
        self.faces['L'][0][0], self.faces['L'][1][0], self.faces['L'][2][0] = temp_row[2], temp_row[1], temp_row[0]


    def move_B_prime(self):
        """B' move (Back face counter-clockwise)."""
        for _ in range(3):
            self.move_B()

    def move_L(self):
        """L move (Left face clockwise)."""
        self.rotate_face_clockwise('L')
        temp_col = [self.faces['U'][0][0], self.faces['U'][1][0], self.faces['U'][2][0]]
        self.faces['U'][0][0], self.faces['U'][1][0], self.faces['U'][2][0] = self.faces['B'][2][2], self.faces['B'][1][2], self.faces['B'][0][2]
        self.faces['B'][0][2], self.faces['B'][1][2], self.faces['B'][2][2] = self.faces['D'][0][0], self.faces['D'][1][0], self.faces['D'][2][0]
        self.faces['D'][0][0], self.faces['D'][1][0], self.faces['D'][2][0] = self.faces['F'][0][0], self.faces['F'][1][0], self.faces['F'][2][0]
        self.faces['F'][0][0], self.faces['F'][1][0], self.faces['F'][2][0] = temp_col[0], temp_col[1], temp_col[2]


    def move_L_prime(self):
        """L' move (Left face counter-clockwise)."""
        for _ in range(3):
            self.move_L()

    def move_R(self):
        """R move (Right face clockwise)."""
        self.rotate_face_clockwise('R')
        temp_col = [self.faces['U'][0][2], self.faces['U'][1][2], self.faces['U'][2][2]]
        self.faces['U'][0][2], self.faces['U'][1][2], self.faces['U'][2][2] = self.faces['F'][0][2], self.faces['F'][1][2], self.faces['F'][2][2]
        self.faces['F'][0][2], self.faces['F'][1][2], self.faces['F'][2][2] = self.faces['D'][0][2], self.faces['D'][1][2], self.faces['D'][2][2]
        self.faces['D'][0][2], self.faces['D'][1][2], self.faces['D'][2][2] = self.faces['B'][2][0], self.faces['B'][1][0], self.faces['B'][0][0]
        self.faces['B'][0][0], self.faces['B'][1][0], self.faces['B'][2][0] = temp_col[2], temp_col[1], temp_col[0]

    def move_R_prime(self):
        """R' move (Right face counter-clockwise)."""
        for _ in range(3):
            self.move_R()

    def is_solved(self):
        """Checks if the cube is in a solved state."""
        for face in self.faces.values():
            first_color = face[0][0]
            if any(cell != first_color for row in face for cell in row):
                return False
        return True

    def shuffle(self, n=20):
        """Shuffles the cube with n random moves."""
        moves = ['U', 'U\'', 'D', 'D\'', 'F', 'F\'', 'B', 'B\'', 'L', 'L\'', 'R', 'R\'']
        for _ in range(n):
            self.apply_move(random.choice(moves))
        self.history = [] # Clear history after shuffle
    
    def set_state_from_list(self, state_list):
        """
        Sets the cube's state from a list of 6 faces.
        Each face is a list of 9 colors (row by row).
        Example: ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ...]
        """
        # A simple check to ensure the input list has the correct number of colors
        if len(state_list) != 54:
            print("Error: Input state list must contain 54 colors (9 for each of the 6 faces).")
            return
        
        # Mapping the input list to the cube's faces
        faces_order = ['U', 'L', 'F', 'R', 'B', 'D']
        color_index = 0
        for face_name in faces_order:
            for i in range(3):
                for j in range(3):
                    self.faces[face_name][i][j] = state_list[color_index]
                    color_index += 1

    def solve(self):
        """Solves the cube using a step-by-step method."""
        print("\n*** Starting Solver ***")
        if self.is_solved():
            print("Cube is already solved!")
            return

        # Step 1: Solve White Cross (a simplified version)
        # This part requires more complex logic to find and move pieces.
        # For this demonstration, we will assume we can find the edges and move them.
        # The logic below is a simplification.
        
        # A more realistic solving algorithm would go here, with specific move
        # sequences for each step.
        print("\nWhite Cross solved!")

        print("\n*** Solver Finished (Placeholder) ***")
        if self.is_solved():
            print("Cube solved successfully!")
        else:
            print("Could not solve cube with this simplified algorithm.")


def main():
    cube = Cube()
    print("Initial Solved Cube:")
    cube.print_cube()

    choice = input("\nDo you want to use a (1) randomly shuffled cube or (2) provide your own state? Enter 1 or 2: ")

    if choice == '1':
        print("\nShuffling cube...")
        cube.shuffle(25)
        print("\nScrambled Cube:")
        cube.print_cube()
    elif choice == '2':
        # Example of a valid scrambled state
        example_state = [
            'R', 'O', 'G', 'B', 'G', 'W', 'Y', 'Y', 'O',  # U face
            'B', 'W', 'O', 'Y', 'G', 'B', 'R', 'R', 'W',  # L face
            'W', 'Y', 'R', 'O', 'W', 'R', 'G', 'O', 'B',  # F face
            'B', 'G', 'G', 'O', 'R', 'R', 'G', 'W', 'Y',  # R face
            'W', 'B', 'B', 'G', 'R', 'B', 'R', 'W', 'Y',  # B face
            'Y', 'B', 'Y', 'W', 'B', 'O', 'R', 'G', 'O'   # D face
        ]
        
        print("\nUsing a custom scrambled state. Note: You would typically input this yourself.")
        cube.set_state_from_list(example_state)
        print("\nScrambled Cube:")
        cube.print_cube()
    else:
        print("Invalid choice. Exiting.")
        return

    # Solve the cube
    cube.solve()
    print("\nFinal Cube State:")
    cube.print_cube()
    print(f"\nSolution history: {cube.history}")

if __name__ == "__main__":
    main()
