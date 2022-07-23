import typing
import datetime



def substep_demonstration(params, substep, state_history, previous_state):
    """
    ## Manages Liquidity

    """
    # State Variables
    current_stage = previous_state["stage"]
    last_state_history_timestep = previous_state['last_state_history_timestep']
    last_state_history_substep = previous_state['last_state_history_substep']

    max_timestep = 0
    max_substep = 0
    for ts in state_history:
        for sub in ts:
            if sub['timestep'] > max_timestep:
                max_timestep =sub['timestep']
                max_substep = 0
            if sub['substep'] >= max_substep:
                if sub['timestep'] >= max_timestep:
                    max_substep = sub['substep']
    return {'last_state_history_timestep': max_timestep,
            'last_state_history_substep': max_substep
            }
