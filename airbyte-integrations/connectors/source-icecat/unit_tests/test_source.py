#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

import logging
from importlib.resources import files

import pytest
import yaml

import source_icecat
from source_icecat.source import SourceIcecat

logger = logging.getLogger("airbyte")


SPEC_YAML_FILE_NAME = "spec.yaml"


def test_streams(config):
    """
    That if streams method returns the expected amount of streams
    """
    source = SourceIcecat()
    streams = source.streams(config)
    expected_streams_number = 1
    assert len(streams) == expected_streams_number


@pytest.mark.parametrize(
    "status_code, response, is_connection_successful",
    (
        (200, "", True),
        (
            404,
            "Not Found",
            False,
        ),
    ),
)
def test_check_connection(
    requests_mock,
    config,
    icecat_response,
    status_code,
    response,
    is_connection_successful,
):
    """
    Test if the check connection method returns the expected response
    """
    requests_mock.register_uri(
        "GET",
        "https://live.icecat.biz/api?UserName=openIcecat-live&Language=EN&icecat_id=1198270",
        status_code=status_code,
        json=icecat_response if 200 >= status_code < 300 else {},
    )
    source = SourceIcecat()
    success, _ = source.check_connection(logger=logger, config=config)
    assert success is is_connection_successful


def test_connector_config(config):
    """
    Test if based on the config a correct config with default values can be returned
    """
    source = SourceIcecat()
    assert source.connector_config(config=config) == config


def test_yaml_spec():
    """
    That if spec.yaml has expected structure and content
    """
    spec_file = files(source_icecat).joinpath(SPEC_YAML_FILE_NAME)

    with open(spec_file) as sf:
        spec = yaml.safe_load(sf)
    assert (
        spec["documentationUrl"]
        == "https://docs.airbyte.com/integrations/sources/icecat"
    )
    assert spec["connectionSpecification"]["title"] == "Icecat Spec"
    assert sorted(spec["connectionSpecification"]["required"]) == sorted(
        ["catalog_type", "catalog_language", "identifier_type", "username", "password"]
    )
    assert sorted(spec["connectionSpecification"]["properties"].keys()) == sorted(
        ["catalog_type", "catalog_language", "identifier_type", "username", "password"]
    )
