from typing import Type


class System:
    def __init__(self, entity, required_components: list[Type] = []) -> None:
        self.entity = entity
        self.required_components: list[Type] = required_components

    def _check_for_required_components(self) -> bool:
        for required_comp in self.required_components:
            if self.entity.get_component(required_comp) == None:
                return False

        return True

    def apply(self) -> None: ...
