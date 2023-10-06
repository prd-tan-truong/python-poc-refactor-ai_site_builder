from typing import Any

from app.core.logging import Logger

from app.services.career_sites_service.core.request_handler import (
    RequestDataT,
    IRequestHandler,
)
from app.services.career_sites_service.core.response_handler import IResponseHandler
from app.services.career_sites_service.core.communication import IServiceCommunicator


class CareerSiteService:
    """Defines the base class of career site service."""

    service_name: str
    request_handler: IRequestHandler
    response_handler: IResponseHandler
    communicator: IServiceCommunicator

    def __init__(
        self,
        service_name: str,
        request_handler: IRequestHandler,
        response_handler: IResponseHandler,
        communicator: IServiceCommunicator,
    ) -> None:
        self.service_name = service_name
        self.request_handler = request_handler
        self.response_handler = response_handler
        self.communicator = communicator

    def __call__(
        self,
        data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        # region: Step 1: Service request integration
        Logger.info(
            service_name=self.service_name,
            message="Request Handler: Start",
        )
        _req_handler: IRequestHandler = self.request_handler(data=data)
        cleaned_data: RequestDataT = _req_handler.data
        Logger.info(
            service_name=self.service_name,
            message="Request Handler: End",
        )
        # endregion

        # region: Step 2: Service execution
        Logger.info(
            service_name=self.service_name,
            message="Remote service communication: Start",
        )
        _service_response: Any = self.communicator.execute(data=cleaned_data)
        Logger.info(
            service_name=self.service_name,
            message="Remote service communication: End",
        )
        # endregion

        # region: Step 3: Response integration
        Logger.info(
            service_name=self.service_name,
            message="Response Handler: Start",
        )
        _res_handler: IResponseHandler = self.response_handler(
            response=_service_response
        )
        Logger.info(
            service_name=self.service_name,
            message="Response Handler: End",
        )
        # endregion

        return _res_handler.data
