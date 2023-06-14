# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import DnsManagementClientConfiguration
from .operations import DnsResourceReferenceOperations, DnssecConfigsOperations, RecordSetsOperations, ZonesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class DnsManagementClient:  # pylint: disable=client-accepts-api-version-keyword
    """The DNS Management Client.

    :ivar dnssec_configs: DnssecConfigsOperations operations
    :vartype dnssec_configs: azure.mgmt.dns.v2023_07_01_preview.operations.DnssecConfigsOperations
    :ivar record_sets: RecordSetsOperations operations
    :vartype record_sets: azure.mgmt.dns.v2023_07_01_preview.operations.RecordSetsOperations
    :ivar zones: ZonesOperations operations
    :vartype zones: azure.mgmt.dns.v2023_07_01_preview.operations.ZonesOperations
    :ivar dns_resource_reference: DnsResourceReferenceOperations operations
    :vartype dns_resource_reference:
     azure.mgmt.dns.v2023_07_01_preview.operations.DnsResourceReferenceOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-07-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = DnsManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.dnssec_configs = DnssecConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01-preview"
        )
        self.record_sets = RecordSetsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01-preview"
        )
        self.zones = ZonesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01-preview"
        )
        self.dns_resource_reference = DnsResourceReferenceOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-07-01-preview"
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "DnsManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
