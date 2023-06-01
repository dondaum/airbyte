#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from typing import Any, Iterable, Mapping, Optional, Union

import requests
from airbyte_cdk.sources.streams.http import HttpStream

from source_icecat.types import IdentifierType


class Product(HttpStream):
    """Icecat Product stream."""

    url_base = "https://live.icecat.biz/"
    primary_key = None

    def __init__(
        self,
        catalog_type: str,
        catalog_language: str,
        identifier_type: IdentifierType,
        username: str,
        password: str,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.catalog_type = catalog_type
        self.catalog_language = catalog_language
        self.identifier_type = identifier_type
        self.username = username
        self.password = password

    def path(
        self, stream_slice: Union[Mapping[str, Any], None] = None, **kwargs
    ) -> str:
        """Read actual data from endpoint."""
        identifier_type = self.identifier_type["type"]
        identifier_value = self.identifier_type["value"]
        if identifier_type == "productid":
            return (
                f"api?UserName={self.username}&Language="
                f"{self.catalog_language.lower()}&icecat_id={str(identifier_value)}"
            )
        elif identifier_type == "GTIN":
            return (
                f"api?UserName={self.username}&Language="
                f"{self.catalog_language.lower()}&GTIN={str(identifier_value)}"
            )
        else:
            raise NotImplementedError(
                "The following identifier are supported: Icecat product id and GTIN"
            )

    def next_page_token(
        self, response: requests.Response
    ) -> Optional[Mapping[str, Any]]:
        return None

    def parse_response(
        self, response: requests.Response, **kwargs
    ) -> Iterable[Mapping]:
        """Parse result."""
        return [response.json()]
