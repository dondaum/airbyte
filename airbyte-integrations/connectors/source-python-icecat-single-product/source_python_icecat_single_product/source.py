#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from abc import ABC
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.auth import TokenAuthenticator


class IcecatProduct(HttpStream):
    url_base = 'https://live.icecat.biz'

    # Set this as a noop.
    primary_key = None

    def __init__(self, icecat_product_id: str, username: str, language: str, **kwargs):
        super().__init__(**kwargs)
        self.icecat_product_id = icecat_product_id
        self.username = username
        self.language = language

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        # The API does not offer pagination, so we return None to indicate there are no more pages in the response
        return None

    def path(
            self, **kwargs
    ) -> str:
        # return f"/api?Username={self.username}&Language={self.language}&icecat_id={self.icecat_product_id}"
        return "/api"

    def request_params(
            self,
            stream_state: Mapping[str, Any],
            stream_slice: Mapping[str, Any] = None,
            next_page_token: Mapping[str, Any] = None,
    ) -> MutableMapping[str, Any]:
        return {"UserName": self.username, "Language": self.language, "icecat_id": self.icecat_product_id}
        # return {}

    def parse_response(
            self,
            response: requests.Response,
            stream_state: Mapping[str, Any],
            stream_slice: Mapping[str, Any] = None,
            next_page_token: Mapping[str, Any] = None,
    ) -> Iterable[Mapping]:
        # The response is a simple JSON whose schema matches our stream's schema exactly,
        # so we just return a list containing the response.
        return [response.json()["data"]]

# Source
class SourcePythonIcecatSingleProduct(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        """
        TODO: Implement a connection check to validate that the user-provided config can be used to connect to the underlying API

        See https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-stripe/source_stripe/source.py#L232
        for an example.

        :param config:  the user-input config object conforming to the connector's spec.yaml
        :param logger:  logger object
        :return Tuple[bool, any]: (True, None) if the input config can be used to connect to the API successfully, (False, error) otherwise.
        """
        logger.info("checking the connection")
        username = config["username"]
        product_id = config["icecat_product_id"]
        language = config["language"]

        if username and product_id:
            logger.info(f"fetchingd data using username : {username} || icecat_product_id : {product_id}  ||  language : {language}")
            return True, None
        else:
            return_str = "Username or Icecat product ID can not be NULL. please enter the input values."
            logger.info(return_str)
            return False, return_str

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        """
            :param config: A Mapping of the user input configuration as defined in the connector spec.
        """
        from airbyte_cdk.sources.streams.http.auth import NoAuth
        auth = NoAuth()

        return [IcecatProduct(authenticator=auth, **config)]
