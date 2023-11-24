#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "fc31348a-bee3-4f59-8614-3e974fb3e036")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
