# coding: utf-8

"""
    Speech Services API version 3.2

    Speech Services API version 3.2.  # noqa: E501

    OpenAPI spec version: 3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class BaseModelDeprecationDates(object):
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
        'adaptation_date_time': 'datetime',
        'transcription_date_time': 'datetime'
    }

    attribute_map = {
        'adaptation_date_time': 'adaptationDateTime',
        'transcription_date_time': 'transcriptionDateTime'
    }

    def __init__(self, adaptation_date_time=None, transcription_date_time=None, _configuration=None):  # noqa: E501
        """BaseModelDeprecationDates - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._adaptation_date_time = None
        self._transcription_date_time = None
        self.discriminator = None

        if adaptation_date_time is not None:
            self.adaptation_date_time = adaptation_date_time
        if transcription_date_time is not None:
            self.transcription_date_time = transcription_date_time

    @property
    def adaptation_date_time(self):
        """Gets the adaptation_date_time of this BaseModelDeprecationDates.  # noqa: E501

        The date when adaptation becomes deprecated.  # noqa: E501

        :return: The adaptation_date_time of this BaseModelDeprecationDates.  # noqa: E501
        :rtype: datetime
        """
        return self._adaptation_date_time

    @adaptation_date_time.setter
    def adaptation_date_time(self, adaptation_date_time):
        """Sets the adaptation_date_time of this BaseModelDeprecationDates.

        The date when adaptation becomes deprecated.  # noqa: E501

        :param adaptation_date_time: The adaptation_date_time of this BaseModelDeprecationDates.  # noqa: E501
        :type: datetime
        """

        self._adaptation_date_time = adaptation_date_time

    @property
    def transcription_date_time(self):
        """Gets the transcription_date_time of this BaseModelDeprecationDates.  # noqa: E501

        The date when transcription becomes deprecated.  # noqa: E501

        :return: The transcription_date_time of this BaseModelDeprecationDates.  # noqa: E501
        :rtype: datetime
        """
        return self._transcription_date_time

    @transcription_date_time.setter
    def transcription_date_time(self, transcription_date_time):
        """Sets the transcription_date_time of this BaseModelDeprecationDates.

        The date when transcription becomes deprecated.  # noqa: E501

        :param transcription_date_time: The transcription_date_time of this BaseModelDeprecationDates.  # noqa: E501
        :type: datetime
        """

        self._transcription_date_time = transcription_date_time

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
        if issubclass(BaseModelDeprecationDates, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BaseModelDeprecationDates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseModelDeprecationDates):
            return True

        return self.to_dict() != other.to_dict()
