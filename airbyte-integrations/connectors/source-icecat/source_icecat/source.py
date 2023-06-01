#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from typing import Any, List, Mapping, Tuple

from airbyte_cdk.models import SyncMode  # type: ignore[attr-defined]
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream

from source_icecat.streams import Product


class SourceIcecat(AbstractSource):
    """Source Icecat implementation."""

    def check_connection(self, logger, config: Mapping[str, Any]) -> Tuple[bool, Any]:
        """:param config:  the user-input config object conforming to the
        connector's spec.yaml :param logger:  logger object :return Tuple[bool,
        any]: (True, None) if the input config can be used to connect to the
        API successfully, (False, error) otherwise."""
        try:
            kwargs = self.connector_config(config)
            product_stream = Product(**kwargs)
            list(product_stream.read_records(sync_mode=SyncMode.full_refresh))
            return True, None
        except Exception as e:
            return False, repr(e)

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        """Returns the existing airbyte streams.

        :param config: A Mapping of the user input configuration as
                defined in the connector spec.
        """
        return [Product(**config)]

    def connector_config(self, config: Mapping[str, Any]) -> Mapping[str, Any]:
        """Returns the connector config."""
        return {
            "catalog_type": config.get("catalog_type"),
            "catalog_language": config.get("catalog_language"),
            "identifier_type": config.get("identifier_type"),
            "username": config.get("username"),
            "password": config.get("password"),
        }
