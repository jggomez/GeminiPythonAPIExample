from abc import ABC
from abc import abstractmethod


class UseCase(ABC):
    @abstractmethod
    async def run(self, params):
        pass
