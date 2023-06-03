#!/usr/bin/env python
# -*- coding: utf-8 -*-
import graphviz as gv
import os
import sys

# Create a graph
g1 = gv.Graph(format='svg')
g1.node('A')
g1.node('B')
g1.node('C')
g1.edge('A', 'B')
g1.edge('B', 'C')
g1.edge('C', 'A')
g1.render('g1')
