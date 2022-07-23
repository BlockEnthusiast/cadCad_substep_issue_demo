# -*- coding: utf-8 -*-
"""
Definition of System Parameters, their types, and default values.

By using a dataclass to represent the System Parameters:
* We can use types for Python type hints
* Set default values
* Ensure that all System Parameters are initialized
"""



from dataclasses import dataclass



@dataclass
class Parameters:
    pass

# Initialize Parameters instance with default values
parameters = Parameters().__dict__
