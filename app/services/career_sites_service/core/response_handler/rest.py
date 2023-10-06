from abc import ABC, abstractmethod
from typing import Any

from http import HTTPStatus

from requests import Response

from app.core.logging import Logger

from app.services.career_sites_service.core.response_handler import BaseResponseHandler


class IResponseSerializer(ABC):
    """Interface for Service Response Serializer."""

    @abstractmethod
    def serialize(self) -> dict[str, Any]:
        raise NotImplementedError


class BaseRESTResponseHandler(BaseResponseHandler):
    response: Response
    serializer: IResponseSerializer

    def is_success(self) -> bool:
        return self.response.ok

    def on_success(self) -> dict[str, Any]:
        _raw_data: dict[str, Any] = self.response.json()
        _data: dict[str, Any] = self.serializer.serialize(_raw_data)
        return _data

    def on_error(self) -> Any:
        match self.response.status_code:
            case HTTPStatus.BAD_REQUEST | HTTPStatus.CONFLICT:
                return self.custom_error()
            case HTTPStatus.UNAUTHORIZED | HTTPStatus.FORBIDDEN:
                Logger.info(
                    message=f"{self.response.status_code}: {self.response.text}",
                    service_name=self.response.url,
                )
                raise Exception
            case _:
                raise Exception

    def custom_error(self) -> Any:
        raise Exception
