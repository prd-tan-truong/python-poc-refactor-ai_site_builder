"""Contains the core definition of Service Request Handler."""
from abc import ABC, abstractmethod
from typing import Any, TypeAlias


RequestDataT: TypeAlias = dict[str, Any]


class IRequestHandler(ABC):
    """Interface for Service Request Validator."""

    @property
    @abstractmethod
    def data(self) -> RequestDataT:
        raise NotImplementedError


class BaseRequestHandler(IRequestHandler):
    """Base class for Service Request Validator."""

    def __init__(self, raw_data: Any) -> None:
        super().__init__()
        self.data = raw_data
