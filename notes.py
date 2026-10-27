'''
Amazon Bracket: Cloud Service by AWS. 

Accessing Hardware:
1)Install Plugin 
2)Define qpu as specified
3)

Hybrid Jobs:
QML (optimizing using classical comp)


'''
import pennylane as qml
from pennylane import numpy as np

qml.about()

#example of hybrid(quantum/classical) job.

def circuit(params):
    qml.RX(params[0], wires = 0)
    qml.RY(params[1], wires = 0)
    #qml.RZ(params[2], wires = 0)
    return qml.expval(qml.PauliZ(0)) 

# What is the difference between a quantum circuit and a classical circuit?
# What is the PauliZ operator? What is the expectation value of an operator?
'''
from bracket.devices import Devices 
from bracket.aws import AwsDevice
'''
