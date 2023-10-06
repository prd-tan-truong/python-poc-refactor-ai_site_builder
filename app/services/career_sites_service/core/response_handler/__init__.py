"""Contains the core definition of Service Response Handler."""
from abc import ABC, abstractmethod
from typing import Any, TypeAlias


ServiceResponseT: TypeAlias = dict[str, Any]


class IResponseHandler(ABC):
    """Interface for Service Response Handler."""

    @property
    @abstractmethod
    def data(self) -> ServiceResponseT:
        pass

    @abstractmethod
    def is_success(self, *args, **kwargs) -> bool:
        raise NotImplementedError

    @abstractmethod
    def on_success(self, *args, **kwargs) -> ServiceResponseT:
        raise NotImplementedError

    @abstractmethod
    def on_error(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class BaseResponseHandler(IResponseHandler):
    """Defines base class for Service Response Handler."""

    response: Any
    result: dict[str, Any]

    def __init__(self, service_response: Any) -> None:
        super().__init__()
        self.response = service_response
        self.result = self.serializer.serialize()

    @property
    def data(self) -> ServiceResponseT:
        return self.on_success() if self.is_success() else self.on_error
