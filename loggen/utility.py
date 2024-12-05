# encoding: utf-8

#
## BaseClass
#
# Base class for most other classes (in subfolders)
class BaseClass(object):

    ## Constructor
    # @param config An instance of the ConfigParser class
    # @param parent The parent class, so that a child class can access the parent class namespace (variables and methods) at any moment
    def __init__(self, config=None, parent=None, *args, **kwargs):
        if not self.loadconfig(config, parent):
            print('CRITICAL ERROR : COULD NOT LOAD CONFIG IN CLASS %s' % self.__class__)
            raise SystemExit(220)
        if parent:
            self.parent = parent
        return object.__init__(self)

    ## Register the configuration to be directly accessible as a variable inside this object
    # @param config An instance of the ConfigParser class, or path to the config file
    def loadconfig(self, config, *args, **kwargs):

        # No config, we quit
        if not config:
            return False

        # If we were supplied a string, we consider it to be the path to the config file to load
        if isinstance(config, str):
            # Loading the config
            from configparser import ConfigParser
            self.configParser = ConfigParser()
            self.configParser.init(config)
            self.configParser.load(*args)
        # Else we already have a loaded config object, we just reference it locally
        else:
            self.configParser = config

        return True
    
class Environment(BaseClass):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        config = self.configParser.config

