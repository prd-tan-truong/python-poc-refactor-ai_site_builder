from abc import ABC, abstractmethod

from typing import Any


class IServiceCommunicator(ABC):
    """Interface for Career Site Service Communicator."""

    @abstractmethod
    def authorize(data: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def authenticate(data: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def execute(data: Any) -> Any:
        raise NotImplementedError
