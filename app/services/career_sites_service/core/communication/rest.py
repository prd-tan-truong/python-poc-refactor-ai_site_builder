from typing import Any


from requests import Request, Response


from app.services.career_sites_service.core.communication import IServiceCommunicator


class CareerSiteRESTClient(IServiceCommunicator):
    api_method: str
    api_endpoint: str

    def __init__(
        self,
        api_method: str,
        api_endpoint: str,
    ) -> None:
        super().__init__()
        self.api_endpoint = api_endpoint
        self.api_method = api_method

    def authenticate(data: Any) -> Any:
        raise NotImplementedError

    def authorize(site_id: None | str) -> dict[str, Any]:
        """
        site = site_credentials(site_id=site_id)
        if site:
            return site
        else:
            raise core.exception.SiteAuthorizationException
        """
        return {
            "API-Key": "a",
            "API-Token": "b",
        }

    def execute(self) -> Response:
        site_credentials: dict[str, Any] = self.authorize(site_id=self.site_id)
        _headers: dict[str, Any] = {**site_credentials}
        return Request(
            method=self.api_method,
            url=self.api_endpoint,
            headers=_headers,
        )

    @property
    def site_id(self) -> str:
        return self._site_id

    @site_id.setter
    def site_id(self, val) -> None:
        self._site_id = val
