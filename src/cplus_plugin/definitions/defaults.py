# -*- coding: utf-8 -*-
"""
    Definitions for all defaults settings
"""

import os

PILOT_AREA_EXTENT = {
    "type": "Polygon",
    "coordinates": [-23.960197335, 32.069186664, -25.201606226, 30.743498637],
}

DOCUMENTATION_SITE = "https://kartoza.github.io/cplus-plugin"

OPTIONS_TITLE = "CPLUS"  # Title in the QGIS settings
ICON_PATH = ":/plugins/cplus_plugin/icon.svg"
DEFAULT_LOGO_PATH = (
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/logos/ci_logo.png"
)
