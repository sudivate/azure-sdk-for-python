# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class CheckNameAvailabilityResult(msrest.serialization.Model):
    """The CheckNameAvailability operation response.

    :param name_available: Boolean value that indicates whether the name is available for you to
     use. If true, the name is available. If false, the name has already been taken or is invalid
     and cannot be used.
    :type name_available: bool
    :param reason: The reason that a storage account name could not be used. The Reason element is
     only returned if NameAvailable is false. Possible values include: "AccountNameInvalid",
     "AlreadyExists".
    :type reason: str or ~azure.mgmt.storage.v2015_06_15.models.Reason
    :param message: The error message explaining the Reason value in more detail.
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CheckNameAvailabilityResult, self).__init__(**kwargs)
        self.name_available = kwargs.get('name_available', None)
        self.reason = kwargs.get('reason', None)
        self.message = kwargs.get('message', None)


class CustomDomain(msrest.serialization.Model):
    """The custom domain assigned to this storage account. This can be set via Update.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The custom domain name. Name is the CNAME source.
    :type name: str
    :param use_sub_domain_name: Indicates whether indirect CName validation is enabled. Default
     value is false. This should only be set on updates.
    :type use_sub_domain_name: bool
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'use_sub_domain_name': {'key': 'useSubDomainName', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CustomDomain, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.use_sub_domain_name = kwargs.get('use_sub_domain_name', None)


class Endpoints(msrest.serialization.Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or table object.

    :param blob: The blob endpoint.
    :type blob: str
    :param queue: The queue endpoint.
    :type queue: str
    :param table: The table endpoint.
    :type table: str
    :param file: The file endpoint.
    :type file: str
    """

    _attribute_map = {
        'blob': {'key': 'blob', 'type': 'str'},
        'queue': {'key': 'queue', 'type': 'str'},
        'table': {'key': 'table', 'type': 'str'},
        'file': {'key': 'file', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Endpoints, self).__init__(**kwargs)
        self.blob = kwargs.get('blob', None)
        self.queue = kwargs.get('queue', None)
        self.table = kwargs.get('table', None)
        self.file = kwargs.get('file', None)


class Resource(msrest.serialization.Model):
    """Describes a storage resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class StorageAccount(Resource):
    """The storage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param provisioning_state: The status of the storage account at the time the operation was
     called. Possible values include: "Creating", "ResolvingDNS", "Succeeded".
    :type provisioning_state: str or ~azure.mgmt.storage.v2015_06_15.models.ProvisioningState
    :param account_type: The type of the storage account. Possible values include: "Standard_LRS",
     "Standard_ZRS", "Standard_GRS", "Standard_RAGRS", "Premium_LRS".
    :type account_type: str or ~azure.mgmt.storage.v2015_06_15.models.AccountType
    :param primary_endpoints: The URLs that are used to perform a retrieval of a public blob,
     queue, or table object. Note that Standard_ZRS and Premium_LRS accounts only return the blob
     endpoint.
    :type primary_endpoints: ~azure.mgmt.storage.v2015_06_15.models.Endpoints
    :param primary_location: The location of the primary data center for the storage account.
    :type primary_location: str
    :param status_of_primary: The status indicating whether the primary location of the storage
     account is available or unavailable. Possible values include: "Available", "Unavailable".
    :type status_of_primary: str or ~azure.mgmt.storage.v2015_06_15.models.AccountStatus
    :param last_geo_failover_time: The timestamp of the most recent instance of a failover to the
     secondary location. Only the most recent timestamp is retained. This element is not returned if
     there has never been a failover instance. Only available if the accountType is Standard_GRS or
     Standard_RAGRS.
    :type last_geo_failover_time: ~datetime.datetime
    :param secondary_location: The location of the geo-replicated secondary for the storage
     account. Only available if the accountType is Standard_GRS or Standard_RAGRS.
    :type secondary_location: str
    :param status_of_secondary: The status indicating whether the secondary location of the storage
     account is available or unavailable. Only available if the SKU name is Standard_GRS or
     Standard_RAGRS. Possible values include: "Available", "Unavailable".
    :type status_of_secondary: str or ~azure.mgmt.storage.v2015_06_15.models.AccountStatus
    :param creation_time: The creation date and time of the storage account in UTC.
    :type creation_time: ~datetime.datetime
    :param custom_domain: The custom domain the user assigned to this storage account.
    :type custom_domain: ~azure.mgmt.storage.v2015_06_15.models.CustomDomain
    :param secondary_endpoints: The URLs that are used to perform a retrieval of a public blob,
     queue, or table object from the secondary location of the storage account. Only available if
     the SKU name is Standard_RAGRS.
    :type secondary_endpoints: ~azure.mgmt.storage.v2015_06_15.models.Endpoints
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'account_type': {'key': 'properties.accountType', 'type': 'str'},
        'primary_endpoints': {'key': 'properties.primaryEndpoints', 'type': 'Endpoints'},
        'primary_location': {'key': 'properties.primaryLocation', 'type': 'str'},
        'status_of_primary': {'key': 'properties.statusOfPrimary', 'type': 'str'},
        'last_geo_failover_time': {'key': 'properties.lastGeoFailoverTime', 'type': 'iso-8601'},
        'secondary_location': {'key': 'properties.secondaryLocation', 'type': 'str'},
        'status_of_secondary': {'key': 'properties.statusOfSecondary', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'secondary_endpoints': {'key': 'properties.secondaryEndpoints', 'type': 'Endpoints'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccount, self).__init__(**kwargs)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.account_type = kwargs.get('account_type', None)
        self.primary_endpoints = kwargs.get('primary_endpoints', None)
        self.primary_location = kwargs.get('primary_location', None)
        self.status_of_primary = kwargs.get('status_of_primary', None)
        self.last_geo_failover_time = kwargs.get('last_geo_failover_time', None)
        self.secondary_location = kwargs.get('secondary_location', None)
        self.status_of_secondary = kwargs.get('status_of_secondary', None)
        self.creation_time = kwargs.get('creation_time', None)
        self.custom_domain = kwargs.get('custom_domain', None)
        self.secondary_endpoints = kwargs.get('secondary_endpoints', None)


class StorageAccountCheckNameAvailabilityParameters(msrest.serialization.Model):
    """The parameters used to check the availability of the storage account name.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param type:
    :type type: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountCheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.type = kwargs.get('type', "Microsoft.Storage/storageAccounts")


class StorageAccountCreateParameters(msrest.serialization.Model):
    """The parameters to provide for the account.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The location of the resource. This will be one of the supported and
     registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). The geo region of a
     resource cannot be changed once it is created, but if an identical geo region is specified on
     update, the request will succeed.
    :type location: str
    :param tags: A set of tags. A list of key value pairs that describe the resource. These tags
     can be used for viewing and grouping this resource (across resource groups). A maximum of 15
     tags can be provided for a resource. Each tag must have a key with a length no greater than 128
     characters and a value with a length no greater than 256 characters.
    :type tags: dict[str, str]
    :param account_type: The sku name. Required for account creation; optional for update. Note
     that in older versions, sku name was called accountType. Possible values include:
     "Standard_LRS", "Standard_ZRS", "Standard_GRS", "Standard_RAGRS", "Premium_LRS".
    :type account_type: str or ~azure.mgmt.storage.v2015_06_15.models.AccountType
    """

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_type': {'key': 'properties.accountType', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountCreateParameters, self).__init__(**kwargs)
        self.location = kwargs['location']
        self.tags = kwargs.get('tags', None)
        self.account_type = kwargs.get('account_type', None)


class StorageAccountKeys(msrest.serialization.Model):
    """The access keys for the storage account.

    :param key1: The value of key 1.
    :type key1: str
    :param key2: The value of key 2.
    :type key2: str
    """

    _attribute_map = {
        'key1': {'key': 'key1', 'type': 'str'},
        'key2': {'key': 'key2', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountKeys, self).__init__(**kwargs)
        self.key1 = kwargs.get('key1', None)
        self.key2 = kwargs.get('key2', None)


class StorageAccountListResult(msrest.serialization.Model):
    """The list storage accounts operation response.

    :param value: The list of storage accounts and their properties.
    :type value: list[~azure.mgmt.storage.v2015_06_15.models.StorageAccount]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[StorageAccount]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class StorageAccountRegenerateKeyParameters(msrest.serialization.Model):
    """The parameters used to regenerate the storage account key.

    All required parameters must be populated in order to send to Azure.

    :param key_name: Required.
    :type key_name: str
    """

    _validation = {
        'key_name': {'required': True},
    }

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountRegenerateKeyParameters, self).__init__(**kwargs)
        self.key_name = kwargs['key_name']


class StorageAccountUpdateParameters(msrest.serialization.Model):
    """The parameters to update on the account.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param account_type: The account type. Note that StandardZRS and PremiumLRS accounts cannot be
     changed to other account types, and other account types cannot be changed to StandardZRS or
     PremiumLRS. Possible values include: "Standard_LRS", "Standard_ZRS", "Standard_GRS",
     "Standard_RAGRS", "Premium_LRS".
    :type account_type: str or ~azure.mgmt.storage.v2015_06_15.models.AccountType
    :param custom_domain: User domain assigned to the storage account. Name is the CNAME source.
     Only one custom domain is supported per storage account at this time. To clear the existing
     custom domain, use an empty string for the custom domain name property.
    :type custom_domain: ~azure.mgmt.storage.v2015_06_15.models.CustomDomain
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_type': {'key': 'properties.accountType', 'type': 'str'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.account_type = kwargs.get('account_type', None)
        self.custom_domain = kwargs.get('custom_domain', None)


class Usage(msrest.serialization.Model):
    """Describes Storage Resource Usage.

    All required parameters must be populated in order to send to Azure.

    :param unit: Required. The unit of measurement. Possible values include: "Count", "Bytes",
     "Seconds", "Percent", "CountsPerSecond", "BytesPerSecond".
    :type unit: str or ~azure.mgmt.storage.v2015_06_15.models.UsageUnit
    :param current_value: Required. The current count of the allocated resources in the
     subscription.
    :type current_value: int
    :param limit: Required. The maximum count of the resources that can be allocated in the
     subscription.
    :type limit: int
    :param name: Required. The name of the type of usage.
    :type name: ~azure.mgmt.storage.v2015_06_15.models.UsageName
    """

    _validation = {
        'unit': {'required': True},
        'current_value': {'required': True},
        'limit': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'str'},
        'current_value': {'key': 'currentValue', 'type': 'int'},
        'limit': {'key': 'limit', 'type': 'int'},
        'name': {'key': 'name', 'type': 'UsageName'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Usage, self).__init__(**kwargs)
        self.unit = kwargs['unit']
        self.current_value = kwargs['current_value']
        self.limit = kwargs['limit']
        self.name = kwargs['name']


class UsageListResult(msrest.serialization.Model):
    """The List Usages operation response.

    :param value: The list Storage Resource Usages.
    :type value: list[~azure.mgmt.storage.v2015_06_15.models.Usage]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Usage]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UsageListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class UsageName(msrest.serialization.Model):
    """The Usage Names.

    :param value: A string describing the resource name.
    :type value: str
    :param localized_value: A localized string describing the resource name.
    :type localized_value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UsageName, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.localized_value = kwargs.get('localized_value', None)
