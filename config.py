#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "dce619df-8104-4d6c-a98d-25c59bee2b3e")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
