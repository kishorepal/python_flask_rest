# from jproperti import 

class PropertyConfig(object):   
   __m_instance = None
   __property_file = "properties.properties"
   
   """Singletone Instance creation
   """
   @classmethod
   def getInstance(cls): 
       if cls.__m_instance is None:
           __m_instance = object.__new__(cls)
           __m_instance.readProperty()
       return __m_instance
   
   @classmethod
   def readProperty(self):
#        p = Properties()
#        with open("foobar.properties", "rb") as f:
#            p.load(self.__property_file, "utf-8")
   
   
   
           
    
    
    
           
    