from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class Action:
    def perfom(self, engine: Engine, entity: Entity) -> None:
        '''Perfom this action with the objects needed to determine its scope.
        
        'engine' is the scope this action is being perfomed in.

        'entity' is the object perfoming the action.

        This method must be overridden by Action subclasses'''
        raise NotImplementedError()

class EscapeAction(Action):
    def perfom(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()

class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perfom(self, engine: Engine, entity, Entity) -> None:
        entity.move(self.dx, self.dy)

