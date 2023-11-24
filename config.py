#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "fec675cc-27d3-42dc-9050-4819f4fd0424")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
