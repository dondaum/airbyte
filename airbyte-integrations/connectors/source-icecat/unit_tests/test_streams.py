#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

import json
from unittest.mock import MagicMock

import pytest
import requests

from source_icecat.streams import Product


@pytest.fixture
def patch_base_class(mocker):
    # Mock abstract methods to enable instantiating abstract class
    mocker.patch.object(Product, "path", "v0/example_endpoint")
    mocker.patch.object(Product, "primary_key", "test_primary_key")
    mocker.patch.object(Product, "__abstractmethods__", set())


def test_product_instance(config):
    """
    Test that a Product instance has expected configuration
    """
    stream = Product(**config)
    assert stream.url_base == "https://live.icecat.biz/"
    assert stream.primary_key is None


def test_request_params(config, patch_base_class):
    stream = Product(**config)
    # TODO: replace this with your input parameters
    inputs = {"stream_slice": None, "stream_state": None, "next_page_token": None}
    # TODO: replace this with your expected request parameters
    expected_params = {}
    assert stream.request_params(**inputs) == expected_params


def test_next_page_token(config):
    """
    Test that the Product Stream has no pagination, thus it should return None
    """
    stream = Product(**config)
    inputs = {"response": MagicMock()}
    assert stream.next_page_token(**inputs) is None


def test_path(config, gtinconfig, badconfig):
    """
    Test if the the correct path is returned based on the identifier type
    """
    stream = Product(**config)
    assert (
        stream.path(stream_slice=MagicMock())
        == "api?UserName=openIcecat-live&Language=en&icecat_id=1198270"
    )
    stream = Product(**gtinconfig)
    assert (
        stream.path(stream_slice=MagicMock())
        == "api?UserName=openIcecat-live&Language=en&GTIN=0882780751682"
    )

    with pytest.raises(NotImplementedError) as excinfo:
        stream = Product(**badconfig)
        stream.path(stream_slice=MagicMock())
    exp_msg = "The following identifier are supported: Icecat product id and GTIN"
    assert str(excinfo.value) == exp_msg


def test_parse_response_expected_response(config, product_raw_resp):
    """
    Test an expected response
    """
    stream = Product(**config)
    response = requests.Response()
    response.status_code = 200
    response_content = bytes(product_raw_resp, "utf-8")
    response._content = response_content
    parsed_response = stream.parse_response(response, stream_state={})
    records = [record for record in parsed_response]
    assert len(records) == 1
    assert records[0] == json.loads(response_content)
