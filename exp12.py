# Quantum Algorithm and Computational Methods
# Program: Deutsch–Jozsa Algorithm (n=3) for a constant function f(x) = 0

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display

def deutsch_jozsa_constant(n=3, shots=1024):
    """
    Implements Deutsch–Jozsa algorithm for n input qubits with a constant oracle (f(x)=0)
    """
    # Total qubits = n input + 1 ancilla
    qc = QuantumCircuit(n + 1, n)

    # Step 1: Initialize ancilla in |1⟩ state
    qc.x(n)

    # Step 2: Apply Hadamard to all qubits (inputs + ancilla)
    qc.h(range(n + 1))

    # --- Oracle for constant f(x)=0 ---
    # Do nothing (oracle leaves ancilla unchanged)
    # (For f(x)=1, you would add a single X gate on the ancilla.)
    # --- End oracle ---

    # Step 3: Apply Hadamard to input qubits
    qc.h(range(n))

    # Step 4: Measure only the input qubits
    qc.measure(range(n), range(n))

    # Simulate
    sim = AerSimulator()
    result = sim.run(qc, shots=shots).result()
    counts = result.get_counts()

    # Display results
    print("Deutsch–Jozsa Algorithm for Constant Function (f(x)=0)")
    display(qc.draw('mpl'))
    display(plot_histogram(counts))

    # Interpretation
    print("\nMeasurement counts (input qubits):")
    print(counts)
    print("\nExpected result: Only '000' should appear → Oracle is constant.")

# Run for n = 3
deutsch_jozsa_constant(n=3, shots=1024)

