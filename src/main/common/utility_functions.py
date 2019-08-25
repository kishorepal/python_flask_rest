'''
Created on Aug 25, 2019

@author: kishore
'''

class UtiliyFunctions(object):
    '''
    classdocs
    '''
    _m_instance = None
    
    @classmethod 
    def getInstance(cls):    
        if cls._m_instance is None :
            _m_instance = object.__new__(cls)
        return _m_instance
    
    @classmethod
    def getName(self): 
        return "KISHORE"