#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_python_icecat_single_product import SourcePythonIcecatSingleProduct

if __name__ == "__main__":
    source = SourcePythonIcecatSingleProduct()
    launch(source, sys.argv[1:])
