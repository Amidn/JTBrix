import yaml
import random
from typing import Tuple, List, Dict, Any


def read_experiment_config(yml_path: str) -> Tuple[List[Dict[str, Any]], List[str]]:
    with open(yml_path, 'r') as f:
        data = yaml.safe_load(f)

    raw_blocks = data.get("experiment_content", [])

    begin_block = []
    end_block = []
    middle_blocks = []

    for block in raw_blocks:
        if not isinstance(block, list):
            continue

        first_item = block[0]

        if isinstance(first_item, str) and first_item.strip().lower() == "type begin":
            begin_block = block[1:]  # Skip the "type Begin" marker
        elif isinstance(first_item, dict) and first_item.get("type") == "end":
            end_block = block[1:]  # Skip the {"type": "end"} marker
            end_block.insert(0, first_item)  # Put end marker back in first position
        else:
            set_code = None
            block_data = []
            for item in block:
                if isinstance(item, dict) and "SetCode" in item:
                    set_code = item["SetCode"]
                else:
                    block_data.append(item)
            if set_code:
                middle_blocks.append((set_code, block_data))

    # Scramble the middle blocks order
    random.shuffle(middle_blocks)
    selected_order = [code for code, _ in middle_blocks]

    # Compose final config list
    config = []
    config.extend(begin_block)
    for _, block_data in middle_blocks:
        config.extend(block_data)
    config.extend(end_block)

    return config, selected_order