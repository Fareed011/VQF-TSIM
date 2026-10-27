
import pennylane as qml

# 1. Create a simulator with one qubit
dev = qml.device("default.qubit", wires=1)

# 2. Define the quantum circuit
@qml.qnode(dev)
def circuit():
    #qml.Hadamard(wires=0)
    return qml.probs(wires=0)

# 3. Execute the circuit
result = circuit()
print(result)
