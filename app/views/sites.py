from typing import Any

from app.core.logging import Logger

from app.services.career_sites_service.sites.create_site import create_site_service


class SiteViewSet:
    # Authentication/Authorization: permission_classes

    def create(self, request, *args, **kwargs):
        """
        @apiVersion 2.2.8
        @api {POST} site_builder/sites
        @apiName Create Site
        @apiGroup SITE_BUILDER
        @apiPermission IsParadoxAdmin
        @apiBody {json} payload
            {
                "site_name": "PRDTai_Test8",
                "company_name": "Dao company",
                "company_id": 999
            }
        @apiResponse {json} Success-Response
            {
                "site_id": 123456
            }
        """
        # > LOG: request
        # > Request Integration
        # -- Authorization at site-level
        # -- Validate request
        # -- Field mapping
        # > Handler
        # -- LOG: before communicating
        # -- Communicate with Career Site Service
        # -- LOG: after communicating
        # > Response integration
        # -- Mapping response from Career Site Service
        # -- LOG: before implement callback
        # -- Callback
        # -- LOG after implement callback
        # > LOG response

        """
        Logger.info(message=f"Request: {request.data}", api_name="create_site_api")
        career_site_service = CareerSiteService.get_service('create-site-api')
        response: dict[str, Any] = career_site_service.execute(data=request.data)

        Logger.info(message=f"Response: {request.data}", api_name="create_site_api")
        return Response(response, status=status.HTTP_200_CREATED)
        """
        Logger.info(message=f"Request: {request.data}", api_name="create_site_api")
        response: dict[str, Any] = create_site_service(data=request.data)
        Logger.info(message="Callback: Start", api_name="create_site_api")
        # Call callback for create_site
        Logger.info(message="Callback: End", api_name="create_site_api")
        Logger.info(message=f"Response: {request.data}", api_name="create_site_api")

        return response
