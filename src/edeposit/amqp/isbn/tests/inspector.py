# -*- coding: utf-8 -*-

#
# library for Robot Framework to inspect python modules
# - 

import inspect
import imp

class PythonModule(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, modulePath):
        self.modulePath = modulePath

    def get_module_variables(self):
        pass

    def has_variable(self,name):
        #import sys, pdb; pdb.Pdb(stdout=sys.__stdout__).set_trace()
        settings = imp.load_source("settings", self.modulePath)
        value = getattr(settings,name)
        if not value:
            raise AssertionError("module: %s has no variable '%s'" % (self.modulePath, name))
    
