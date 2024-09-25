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
from swagger_client.api.custom_speech_transcriptions_api import CustomSpeechTranscriptionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCustomSpeechTranscriptionsApi(unittest.TestCase):
    """CustomSpeechTranscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.custom_speech_transcriptions_api.CustomSpeechTranscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_transcriptions_create(self):
        """Test case for transcriptions_create

        Creates a new transcription.  # noqa: E501
        """
        pass

    def test_transcriptions_delete(self):
        """Test case for transcriptions_delete

        Deletes the specified transcription task.  # noqa: E501
        """
        pass

    def test_transcriptions_get(self):
        """Test case for transcriptions_get

        Gets the transcription identified by the given ID.  # noqa: E501
        """
        pass

    def test_transcriptions_get_file(self):
        """Test case for transcriptions_get_file

        Gets one specific file (identified with fileId) from a transcription (identified with id).  # noqa: E501
        """
        pass

    def test_transcriptions_list(self):
        """Test case for transcriptions_list

        Gets a list of transcriptions for the authenticated subscription.  # noqa: E501
        """
        pass

    def test_transcriptions_list_files(self):
        """Test case for transcriptions_list_files

        Gets the files of the transcription identified by the given ID.  # noqa: E501
        """
        pass

    def test_transcriptions_list_supported_locales(self):
        """Test case for transcriptions_list_supported_locales

        Gets a list of supported locales for offline transcriptions.  # noqa: E501
        """
        pass

    def test_transcriptions_update(self):
        """Test case for transcriptions_update

        Updates the mutable details of the transcription identified by its ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
