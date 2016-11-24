#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2016, Sascha Girrulat <sascha@girrulat.de>
#
# This file is not part of official Ansible
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rabbitmq_message is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: rabbitmq_message
short_description: rabbitmq-message provides tasks to send messages to rabbitmq.

description:
  - Manage messages send to rabbitmq queues.
author: '"Sascha Girrulat (sascha@girrulat.de))"'
options:
    login_host:
        description:
             - rabbitMQ host to recieve the message
        required: true
        default: null
        aliases: [ "host" ]
    login_user:
        description:
            - rabbitMQ user for connection
        required: false
        default: guest
        aliases: [ "user" ]
    login_password:
        description:
            - rabbitMQ password for connection
        required: false
        default: false
        aliases: [ "password" ]
    login_port:
        description:
            - rabbitMQ management api port
        required: false
        default: 15672
        aliases: [ "port" ]
    destination:
        description:
            - destination exchange or queue for the binding
        required: true
        aliases: [ "exchange", "queue", "dest" ]
    destination_type:
        description:
            - Either queue or exchange
        required: true
        choices: [ "queue", "exchange" ]
        aliases: [ "type", "dest_type" ]
    exchange_type:
        description:
            - Either direct, topic, headers and fanout.
        required: true
        choices: [ "direct", "topic", "headers", "fanout" ]
        aliases: [ "exchange_type", "type", "dest_type" ]
        default: topic
    routing_key:
        description:
            - routing key of the message
        required: false
    message:
        description:
            - Body of the message, as a JSON term
        required: false
        default: "{}"
        aliases: [ "message_body", "body" ]
'''

EXAMPLES = '''
# Send a message to myExchange with routing key example.info
- rabbitmq_message:
    host: rabbitMQHost
    destination: myExchange
    destination_type: exchange
    routing_key: example.info
    message: '{ "myData" : "example"}'

# Send a message to a queue myQueue with routing
- rabbitmq_message:
    host: rabbitMQHost
    destination: myQueue
    destination_type: queue
    message: '{ "myData" : "example"}'
'''

import json


def main():
    module = AnsibleModule(
        argument_spec = dict(
            login_user = dict(aliases=['user'], default='guest', type='str'),
            login_password = dict(default='', type='str', no_log=True),
            login_host = dict(required=True, aliases=['host'], type='str'),
            login_port = dict(aliases=['port'], default='15672', type='str'),
            destination = dict(required=True, aliases=[ "dest"], type='str'),
            destination_type = dict(required=True, aliases=[ "type", "dest_type"], choices=[ "queue", "exchange" ],  type='str'),
            routing_key = dict(type='str'),
            message = dict(aliases=['body', 'message_body'], type='str'),
        )
    )
