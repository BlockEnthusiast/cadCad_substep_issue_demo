
import model.parts.demo as demo


from model.system_parameters import parameters
from model.utils import update_from_signal

demo_blocks =     {
        "description": """
            Demo track substeps in state history
        """,
        "policies": {
            "policy_adjust_weight": demo.substep_demonstration,
        },
        "variables": {
            "last_state_history_timestep": update_from_signal(
                "last_state_history_timestep"
            ),
            "last_state_history_substep": update_from_signal(
                "last_state_history_substep"
            ),
        },
    }

_state_update_blocks = [
    # {
    #     "description": """
    #         Demo track substeps in state history
    #     """,
    #     "policies": {
    #         "policy_adjust_weight": demo.substep_demonstration,
    #     },
    #     "variables": {
    #         "last_state_history_timestep": update_from_signal(
    #             "last_state_history_timestep"
    #         ),
    #         "last_state_history_substep": update_from_signal(
    #             "last_state_history_substep"
    #         ),
    #     },
    # },
    # {
    #     "description": """
    #         Adjust LBP Supply
    #     """,
    #     "policies": {
    #         "policy_add_liquidity": lbp.policy_add_liquidity,
    #     },
    #     "variables": {
    #         "lbp_supply_x": update_from_signal(
    #             "lbp_supply_x"
    #         ),
    #         "lbp_supply_y": update_from_signal(
    #             "lbp_supply_y"
    #         ),
    #     },
    # },
    # {
    #     "description": """
    #         Calc LBP Price
    #     """,
    #     "policies": {
    #         "policy_calc_pricing": lbp.policy_calc_pricing,
    #     },
    #     "variables": {
    #         "lbp_price_y_in_x": update_from_signal(
    #             "lbp_price_y_in_x"
    #         ),
    #         "lbp_price_x_in_y": update_from_signal(
    #             "lbp_price_x_in_y"
    #         ),
    #         "lbp_y_usd_price": update_from_signal(
    #             "lbp_y_usd_price"
    #         ),
    #     },
    # },
    # {
    #     "description": """
    #         Calc LBP Price Impact
    #     """,
    #     "policies": {
    #         "policy_calc_price_impact": lbp.policy_calc_price_impact,
    #     },
    #     "variables": {
    #         "lbp_sell_y_impact": update_from_signal(
    #             "lbp_sell_y_impact"
    #         ),
    #         "lbp_sell_x_impact": update_from_signal(
    #             "lbp_sell_x_impact"
    #         ),
    #     },
    # },
]



# Conditionally update the order of the State Update Blocks using a ternary operator
_state_update_blocks = (
    [
    demo_blocks,
    demo_blocks,
    demo_blocks,
    demo_blocks,
    demo_blocks,
    ]
    + _state_update_blocks
)

# Split the state update blocks into those used during the simulation (state_update_blocks)
# and those used in post-processing to calculate the system metrics (post_processing_blocks)
state_update_blocks = [
    block for block in _state_update_blocks if not block.get("post_processing", False)
]
post_processing_blocks = [
    block for block in _state_update_blocks if block.get("post_processing", False)
]
