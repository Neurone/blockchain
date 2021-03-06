# coding: utf-8

"""
    Azure Blockchain Workbench REST API

    The Azure Blockchain Workbench REST API is a Workbench extensibility point, which allows developers to create and manage blockchain applications, manage users and organizations within a consortium, integrate blockchain applications into services and platforms, perform transactions on a blockchain, and retrieve transactional and contract data from a blockchain.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserInput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'external_id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email_address': 'str'
    }

    attribute_map = {
        'external_id': 'externalID',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email_address': 'emailAddress'
    }

    def __init__(self, external_id=None, first_name=None, last_name=None, email_address=None):  # noqa: E501
        """UserInput - a model defined in Swagger"""  # noqa: E501

        self._external_id = None
        self._first_name = None
        self._last_name = None
        self._email_address = None
        self.discriminator = None

        if external_id is not None:
            self.external_id = external_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email_address is not None:
            self.email_address = email_address

    @property
    def external_id(self):
        """Gets the external_id of this UserInput.  # noqa: E501


        :return: The external_id of this UserInput.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this UserInput.


        :param external_id: The external_id of this UserInput.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def first_name(self):
        """Gets the first_name of this UserInput.  # noqa: E501


        :return: The first_name of this UserInput.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserInput.


        :param first_name: The first_name of this UserInput.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserInput.  # noqa: E501


        :return: The last_name of this UserInput.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserInput.


        :param last_name: The last_name of this UserInput.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email_address(self):
        """Gets the email_address of this UserInput.  # noqa: E501


        :return: The email_address of this UserInput.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserInput.


        :param email_address: The email_address of this UserInput.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
