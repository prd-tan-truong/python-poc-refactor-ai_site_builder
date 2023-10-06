from typing import Any

from http import Me

from app.services.career_sites_service import CareerSiteService

from app.services.career_sites_service.core.communication.rest import (
    CareerSiteRESTClient,
)
from app.services.career_sites_service.core.request_handler import (
    BaseRequestHandler,
)
from app.services.career_sites_service.core.response_handler.rest import (
    BaseRESTResponseHandler,
    IResponseSerializer,
)


class RequestSerializer:
    data: Any


class ResponseSerializer(IResponseSerializer):
    data: dict[str, Any]

    def serialize(self) -> dict[str, Any]:
        return self.data


class DuplicatedSiteException(Exception):
    code: str = "10001"
    message: str = "Site name must be unique."
    field: str = "site_name"


class RequestHandler(BaseRequestHandler):
    _data: dict[str, Any]

    @property
    def data(self) -> dict[str, Any]:
        return self._data

    @data.setter
    def data(self, val) -> None:
        serializer = RequestSerializer(data=val)
        self._data = serializer.data


class ResponseHandler(BaseRESTResponseHandler):
    serializer: IResponseSerializer = ResponseSerializer

    def custom_error(self) -> Any:
        _error: dict[str, Any] = self.response.json()
        match _error["code"]:
            case 10001:
                raise DuplicatedSiteException
            case _:
                raise Exception


create_site_api = CareerSiteRESTClient(
    api_endpoint="https://career-sites.recruiting.com/dev/site",
    api_method="POST",
)


create_site_service = CareerSiteService(
    service_name="/api/rest/site/create-sites",
    communicator=create_site_api,
    request_handler=RequestHandler,
    response_handler=ResponseHandler,
)
