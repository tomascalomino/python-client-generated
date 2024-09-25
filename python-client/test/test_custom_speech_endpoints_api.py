# coding: utf-8

"""
    Speech Services API version 3.2

    Speech Services API version 3.2.  # noqa: E501

    OpenAPI spec version: 3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.custom_speech_endpoints_api import CustomSpeechEndpointsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCustomSpeechEndpointsApi(unittest.TestCase):
    """CustomSpeechEndpointsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.custom_speech_endpoints_api.CustomSpeechEndpointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_endpoints_create(self):
        """Test case for endpoints_create

        Creates a new endpoint.  # noqa: E501
        """
        pass

    def test_endpoints_delete(self):
        """Test case for endpoints_delete

        Deletes the endpoint identified by the given ID.  # noqa: E501
        """
        pass

    def test_endpoints_delete_base_model_log(self):
        """Test case for endpoints_delete_base_model_log

        Deletes one audio or transcription log that have been stored when using the default base model of a given language.  # noqa: E501
        """
        pass

    def test_endpoints_delete_base_model_logs(self):
        """Test case for endpoints_delete_base_model_logs

        Deletes the specified audio and transcription logs that have been stored when using the default base model of a given language. It deletes all logs before (and including) a specific day.  # noqa: E501
        """
        pass

    def test_endpoints_delete_log(self):
        """Test case for endpoints_delete_log

        Deletes one audio or transcription log that have been stored for a given endpoint.  # noqa: E501
        """
        pass

    def test_endpoints_delete_logs(self):
        """Test case for endpoints_delete_logs

        Deletes the specified audio and transcription logs that have been stored for a given endpoint. It deletes all logs before (and including) a specific day.  # noqa: E501
        """
        pass

    def test_endpoints_get(self):
        """Test case for endpoints_get

        Gets the endpoint identified by the given ID.  # noqa: E501
        """
        pass

    def test_endpoints_get_base_model_log(self):
        """Test case for endpoints_get_base_model_log

        Gets a specific audio or transcription log for the default base model in a given language.  # noqa: E501
        """
        pass

    def test_endpoints_get_log(self):
        """Test case for endpoints_get_log

        Gets a specific audio or transcription log for a given endpoint.  # noqa: E501
        """
        pass

    def test_endpoints_list(self):
        """Test case for endpoints_list

        Gets the list of endpoints for the authenticated subscription.  # noqa: E501
        """
        pass

    def test_endpoints_list_base_model_logs(self):
        """Test case for endpoints_list_base_model_logs

        Gets the list of audio and transcription logs that have been stored when using the default base model of a given language.  # noqa: E501
        """
        pass

    def test_endpoints_list_logs(self):
        """Test case for endpoints_list_logs

        Gets the list of audio and transcription logs that have been stored for a given endpoint.  # noqa: E501
        """
        pass

    def test_endpoints_list_supported_locales(self):
        """Test case for endpoints_list_supported_locales

        Gets a list of supported locales for endpoint creations.  # noqa: E501
        """
        pass

    def test_endpoints_update(self):
        """Test case for endpoints_update

        Updates the metadata of the endpoint identified by the given ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
