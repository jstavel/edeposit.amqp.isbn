# -*- coding: utf-8 -*-
#
# AMQP ISBN module
#

from __future__ import unicode_literals
from __future__ import print_function

# AMQP framework
from kombu import Connection
from kombu import Exchange
from kombu import Queue


class IsbnMessage(object):
    '''Base ISBN message class.'''
    
    pass


class IsbnReceiver:
    
    pass
