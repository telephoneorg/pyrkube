"""
PyRKube
~~~~~~~~~~~~~

Readonly wrapper for pykube with a different focus.
"""

import logging

from . import config, util, adict, client, hosts, objects
from .client import KubeAPIClient, KubeInterfaceBase
from .hosts import PodHostname, StatefulPodHostname
from .objects import (
    Pod,
    ConfigMap,
    Secret,
    ReplicaSet,
    Deployment,
    DaemonSet,
    StatefulSet,
    Endpoint,
    Service,
    KubeApp,
    KubeApps
)

__title__ = 'pyrkube'
__version__ = '0.2.0'
__build__ = 0x000200
__author__ = "Joe Black <joe@valuphone.com>"
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016 Joe Black'


logging.getLogger(__name__).addHandler(logging.NullHandler())