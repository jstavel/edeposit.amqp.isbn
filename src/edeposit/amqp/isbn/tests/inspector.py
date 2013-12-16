# -*- coding: utf-8 -*-

#
# library for Robot Framework to inspect python modules
# - 

import inspect

class PythonModule(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, modulePath):
        self.modulePath = modulePath
        open("/tmp/vystup.txt","w").write(modulePath)

    def get_module_variables(self):
        pass

    def has_variable(self,name):
        raise AssertionError("module: %s has no variable '%s'" % (self.modulePath, name))
    
