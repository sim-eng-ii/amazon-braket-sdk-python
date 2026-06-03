# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from __future__ import annotations

import itertools

from braket.circuits.circuit import Circuit
from braket.circuits.observables import I, TensorProduct, X, Y, Z
from braket.quantum_information.pauli_string import PauliString

_IDENTITY = "I"
_PAULI_X = "X"
_PAULI_Y = "Y"
_PAULI_Z = "Z"
_PAULI_INDICES = {_IDENTITY: 0, _PAULI_X: 1, _PAULI_Y: 2, _PAULI_Z: 3}
_PRODUCT_MAP = {
    "X": {"Y": ["Z", 1j], "Z": ["Y", -1j]},
    "Y": {"X": ["Z", -1j], "Z": ["X", 1j]},
    "Z": {"X": ["Y", 1j], "Y": ["X", -1j]},
}
_ID_OBS = I()
_PAULI_OBSERVABLES = {_PAULI_X: X(), _PAULI_Y: Y(), _PAULI_Z: Z()}
_SIGN_MAP = {"+": 1, "-": -1}

class PauliStringSum: 
    """A container for a sum of Pauli strings with their phases."""

    def __init__(self, pauli_string_sum: list[str | PauliString] | PauliStringSum):
        """Initializes a `PauliStringSum`.

        Args: 
            pauli_string_sum (list[str | PauliString] | PauliStringSum): The representation of list of pauli words, either a
                list of strings or another PauliStringSum object. A valid string consists of an optional phase,
                specified by an optional sign +/- followed by an uppercase string in {I, X, Y, Z}.
                Example valid strings are: XYZ, +YIZY, -YX

        Raises:
            ValueError: If the Pauli String is empty.
        """