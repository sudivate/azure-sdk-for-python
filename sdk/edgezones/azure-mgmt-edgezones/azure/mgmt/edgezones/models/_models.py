# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ErrorAdditionalInfo(_model_base.Model):
    """The resource management error additional info.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    type: Optional[str] = rest_field(visibility=["read"])
    """The additional info type."""
    info: Optional[Any] = rest_field(visibility=["read"])
    """The additional info."""


class ErrorDetail(_model_base.Model):
    """The error detail.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.edgezones.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.mgmt.edgezones.models.ErrorAdditionalInfo]
    """

    code: Optional[str] = rest_field(visibility=["read"])
    """The error code."""
    message: Optional[str] = rest_field(visibility=["read"])
    """The error message."""
    target: Optional[str] = rest_field(visibility=["read"])
    """The error target."""
    details: Optional[List["_models.ErrorDetail"]] = rest_field(visibility=["read"])
    """The error details."""
    additional_info: Optional[List["_models.ErrorAdditionalInfo"]] = rest_field(
        name="additionalInfo", visibility=["read"]
    )
    """The error additional info."""


class ErrorResponse(_model_base.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations.

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.edgezones.models.ErrorDetail
    """

    error: Optional["_models.ErrorDetail"] = rest_field()
    """The error object."""

    @overload
    def __init__(
        self,
        *,
        error: Optional["_models.ErrorDetail"] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Resource(_model_base.Model):
    """Common properties for all Azure Resource Manager resources.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.edgezones.models.SystemData
    """

    id: Optional[str] = rest_field(visibility=["read"])
    """Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long"""
    name: Optional[str] = rest_field(visibility=["read"])
    """The name of the resource."""
    type: Optional[str] = rest_field(visibility=["read"])
    """The type of the resource. E.g. \"Microsoft.Compute/virtualMachines\" or
     \"Microsoft.Storage/storageAccounts\"."""
    system_data: Optional["_models.SystemData"] = rest_field(name="systemData", visibility=["read"])
    """Azure Resource Manager metadata containing createdBy and modifiedBy information."""


class ProxyResource(Resource):
    """The base proxy resource.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.edgezones.models.SystemData
    """


class ExtendedZone(ProxyResource):
    """Resource that represents an Azure Extended Zone available to a subscription for registering and
    unregistering.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.edgezones.models.SystemData
    :ivar properties: The resource-specific properties for this resource.
    :vartype properties: ~azure.mgmt.edgezones.models.ExtendedZoneProperties
    """

    properties: Optional["_models.ExtendedZoneProperties"] = rest_field(visibility=["read", "create"])
    """The resource-specific properties for this resource."""

    @overload
    def __init__(
        self,
        *,
        properties: Optional["_models.ExtendedZoneProperties"] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ExtendedZoneProperties(_model_base.Model):  # pylint: disable=too-many-instance-attributes
    """The properties of an Extended Zone resource.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar provisioning_state: Status of the last operation performed by the subscription on the
     Edge Zone resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning",
     "Updating", "Deleting", and "Accepted".
    :vartype provisioning_state: str or ~azure.mgmt.edgezones.models.ProvisioningState
    :ivar registration_state: Indicates the Azure Extended Zone registration’s approval status.
     Known values are: "NotRegistered", "PendingRegister", "Registered", and "PendingUnregister".
    :vartype registration_state: str or ~azure.mgmt.edgezones.models.RegistrationState
    :ivar display_name: Display name of the Azure Extended Zone. Required.
    :vartype display_name: str
    :ivar regional_display_name: Regional display name of the Azure Extended Zone. Required.
    :vartype regional_display_name: str
    :ivar region_type: Type of region for the Azure Extended Zone. Required.
    :vartype region_type: str
    :ivar region_category: Category of region for the Azure Extended Zone. Required.
    :vartype region_category: str
    :ivar geography: Geography of the Azure Extended Zone. Required.
    :vartype geography: str
    :ivar geography_group: The Geography Group of the Azure Extended Zone. Required.
    :vartype geography_group: str
    :ivar longitude: The Longitude of the Azure Extended Zone. Required.
    :vartype longitude: str
    :ivar latitude: The Latitude of the Azure Extended Zone. Required.
    :vartype latitude: str
    :ivar home_location: The Home Location of the Azure Extended Zone. Required.
    :vartype home_location: str
    """

    provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = rest_field(
        name="provisioningState", visibility=["read"]
    )
    """Status of the last operation performed by the subscription on the Edge Zone resource. Known
     values are: \"Succeeded\", \"Failed\", \"Canceled\", \"Provisioning\", \"Updating\",
     \"Deleting\", and \"Accepted\"."""
    registration_state: Optional[Union[str, "_models.RegistrationState"]] = rest_field(
        name="registrationState", visibility=["read"]
    )
    """Indicates the Azure Extended Zone registration’s approval status. Known values are:
     \"NotRegistered\", \"PendingRegister\", \"Registered\", and \"PendingUnregister\"."""
    display_name: str = rest_field(name="displayName", visibility=["read"])
    """Display name of the Azure Extended Zone. Required."""
    regional_display_name: str = rest_field(name="regionalDisplayName", visibility=["read"])
    """Regional display name of the Azure Extended Zone. Required."""
    region_type: str = rest_field(name="regionType", visibility=["read"])
    """Type of region for the Azure Extended Zone. Required."""
    region_category: str = rest_field(name="regionCategory", visibility=["read"])
    """Category of region for the Azure Extended Zone. Required."""
    geography: str = rest_field(visibility=["read"])
    """Geography of the Azure Extended Zone. Required."""
    geography_group: str = rest_field(name="geographyGroup", visibility=["read"])
    """The Geography Group of the Azure Extended Zone. Required."""
    longitude: str = rest_field(visibility=["read"])
    """The Longitude of the Azure Extended Zone. Required."""
    latitude: str = rest_field(visibility=["read"])
    """The Latitude of the Azure Extended Zone. Required."""
    home_location: str = rest_field(name="homeLocation", visibility=["read"])
    """The Home Location of the Azure Extended Zone. Required."""


class Operation(_model_base.Model):
    """Details of a REST API operation, returned from the Resource Provider Operations API.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action".
    :vartype name: str
    :ivar is_data_action: Whether the operation applies to data-plane. This is "true" for
     data-plane operations and "false" for Azure Resource Manager/control-plane operations.
    :vartype is_data_action: bool
    :ivar display: Localized display information for this particular operation.
    :vartype display: ~azure.mgmt.edgezones.models.OperationDisplay
    :ivar origin: The intended executor of the operation; as in Resource Based Access Control
     (RBAC) and audit logs UX. Default value is "user,system". Known values are: "user", "system",
     and "user,system".
    :vartype origin: str or ~azure.mgmt.edgezones.models.Origin
    :ivar action_type: Extensible enum. Indicates the action type. "Internal" refers to actions
     that are for internal only APIs. "Internal"
    :vartype action_type: str or ~azure.mgmt.edgezones.models.ActionType
    """

    name: Optional[str] = rest_field(visibility=["read"])
    """The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     \"Microsoft.Compute/virtualMachines/write\",
     \"Microsoft.Compute/virtualMachines/capture/action\"."""
    is_data_action: Optional[bool] = rest_field(name="isDataAction", visibility=["read"])
    """Whether the operation applies to data-plane. This is \"true\" for data-plane operations and
     \"false\" for Azure Resource Manager/control-plane operations."""
    display: Optional["_models.OperationDisplay"] = rest_field()
    """Localized display information for this particular operation."""
    origin: Optional[Union[str, "_models.Origin"]] = rest_field(visibility=["read"])
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
     logs UX. Default value is \"user,system\". Known values are: \"user\", \"system\", and
     \"user,system\"."""
    action_type: Optional[Union[str, "_models.ActionType"]] = rest_field(name="actionType")
    """Extensible enum. Indicates the action type. \"Internal\" refers to actions that are for
     internal only APIs. \"Internal\""""

    @overload
    def __init__(
        self,
        *,
        display: Optional["_models.OperationDisplay"] = None,
        action_type: Optional[Union[str, "_models.ActionType"]] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class OperationDisplay(_model_base.Model):
    """Localized display information for and operation.

    :ivar provider: The localized friendly form of the resource provider name, e.g. "Microsoft
     Monitoring Insights" or "Microsoft Compute".
    :vartype provider: str
    :ivar resource: The localized friendly name of the resource type related to this operation.
     E.g. "Virtual Machines" or "Job Schedule Collections".
    :vartype resource: str
    :ivar operation: The concise, localized friendly name for the operation; suitable for
     dropdowns. E.g. "Create or Update Virtual Machine", "Restart Virtual Machine".
    :vartype operation: str
    :ivar description: The short, localized friendly description of the operation; suitable for
     tool tips and detailed views.
    :vartype description: str
    """

    provider: Optional[str] = rest_field()
    """The localized friendly form of the resource provider name, e.g. \"Microsoft Monitoring
     Insights\" or \"Microsoft Compute\"."""
    resource: Optional[str] = rest_field()
    """The localized friendly name of the resource type related to this operation. E.g. \"Virtual
     Machines\" or \"Job Schedule Collections\"."""
    operation: Optional[str] = rest_field()
    """The concise, localized friendly name for the operation; suitable for dropdowns. E.g. \"Create
     or Update Virtual Machine\", \"Restart Virtual Machine\"."""
    description: Optional[str] = rest_field()
    """The short, localized friendly description of the operation; suitable for tool tips and detailed
     views."""

    @overload
    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class SystemData(_model_base.Model):
    """Metadata pertaining to creation and last modification of the resource.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.mgmt.edgezones.models.CreatedByType
    :ivar created_at: The type of identity that created the resource.
    :vartype created_at: ~datetime.date
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or ~azure.mgmt.edgezones.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.date
    """

    created_by: Optional[str] = rest_field(name="createdBy", visibility=["read"])
    """The identity that created the resource."""
    created_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(
        name="createdByType", visibility=["read"]
    )
    """The type of identity that created the resource. Known values are: \"User\", \"Application\",
     \"ManagedIdentity\", and \"Key\"."""
    created_at: Optional[datetime.date] = rest_field(name="createdAt", visibility=["read"])
    """The type of identity that created the resource."""
    last_modified_by: Optional[str] = rest_field(name="lastModifiedBy", visibility=["read"])
    """The identity that last modified the resource."""
    last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(
        name="lastModifiedByType", visibility=["read"]
    )
    """The type of identity that last modified the resource. Known values are: \"User\",
     \"Application\", \"ManagedIdentity\", and \"Key\"."""
    last_modified_at: Optional[datetime.date] = rest_field(name="lastModifiedAt", visibility=["read"])
    """The timestamp of resource last modification (UTC)."""
