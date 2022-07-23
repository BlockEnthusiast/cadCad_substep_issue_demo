import numpy as np
from dataclasses import dataclass
from datetime import datetime

# from model.system_parameters import validator_environments
from model.types import (

    Stage,
)

@dataclass
class StateVariables:
    """State Variables
    Each State Variable is defined as:
    state variable key: state variable type = default state variable value
    """

    # Time state variables
    stage: Stage = None
    """
    The stage of the network upgrade process.

    See "stage" System Parameter in model.system_parameters
    & model.types.Stage Enum for further documentation.
    """
    timestamp: datetime = None
    """
    The timestamp for each timestep as a Python `datetime` object, starting from `date_start` Parameter.
    """

    last_state_history_substep: int = None
    last_state_history_timestep: int = None


# Initialize State Variables instance with default values
initial_state = StateVariables().__dict__
