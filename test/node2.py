# coding: utf-8

__author__ = 'zhenhang.sun@gmail.com'
__version__ = '1.0.0'

import sys
sys.path.append("..")
from raft.node import Node

if __name__ == '__main__':

    conf = {
              'group_id': '1',
              'id': '2',
              'addr': ('localhost', 10002),
              'peers': { '1': ('localhost', 10001), 
                         '3': ('localhost', 10003)
                       }
            }
     
    node = Node(conf)

    node.run()