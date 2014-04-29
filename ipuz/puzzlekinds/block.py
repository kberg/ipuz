from ipuz.structures import (
    validate_dimensions,
    validate_groupspec_dict,
    validate_styledcell,
)
from ipuz.validators import (
    validate_bool,
    validate_list_of_lists,
)


def validate_field(field_name, field_data):
    validate_list_of_lists(field_name, field_data, "StyledCell", validate_styledcell)


IPUZ_BLOCK_VALIDATORS = {
    "dimensions": validate_dimensions,
    "slide": validate_bool,
    "move": validate_bool,
    "rotatable": validate_bool,
    "flippable": validate_bool,
    "field": validate_field,
    "enter": validate_groupspec_dict,
    "start": validate_groupspec_dict,
    "saved": validate_groupspec_dict,
    "end": validate_groupspec_dict,
    "exit": validate_groupspec_dict,
}
