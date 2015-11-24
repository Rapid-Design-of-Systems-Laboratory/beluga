from configparser import SafeConfigParser
import os.path, os
import sys
from beluga.utils.pythematica import mathematica_root

class BelugaConfig(dict):
    """Defines configuration options for Beluga and allows loading/saving configuration files"""
    section_name = 'beluga'

    option_list = {
        # Format of list items are as follows
        # 'option_name': ['default_str' or default_func(), 'Input prompt string', validation_function or None]
        # TODO: add validation function for mathematica_root option
        'mathematica_root':[mathematica_root,'Set Mathematica installation path ',None],
        'logfile':['beluga.log','Default log file name',None]
        # 'default_solver':['SingleShooting','Select default BVP solver ']
    }

    def getroot(self):
        """Gets the base path where beluga is installed"""
        return os.path.abspath(os.path.dirname(__file__)+'/../')

    def __init__(self, config_file = '~/.beluga/config.ini', run_tool = False, arguments=None):
        """Initializes a BelugaConfig object with existing an config file or defaults"""
        self.cfgdata = SafeConfigParser()
        self.config_file = os.path.expanduser(config_file)

        try:
            os.mkdir(os.path.expanduser('~/.beluga'))
        except:
            pass

        if run_tool:
            self.config_tool(arguments)
        if config_file is not None:
            if not os.path.isfile(self.config_file):
                self.config_tool() # Run configuration tool if file is missing

            self.cfgdata.read(self.config_file)
            if BelugaConfig.section_name not in self.cfgdata:
                # If config file does not have the required information ask the user
                self.cfgdata[BelugaConfig.section_name] = {}
                self.config_tool()
            else:
                # If all the listed options are not present in the file
                # run the configuration tool
                # TODO: Validate individual options even if they exist in the file
                if not all(option in self.cfgdata[BelugaConfig.section_name]
                                for option in BelugaConfig.option_list):
                    self.config_tool()

        # Update the object's dictionary with new data
        self.update(self.cfgdata[BelugaConfig.section_name])

    def config_tool(self,arguments=None):
        """Interacts with user to configure Beluga"""

        print('Welcome to the Beluga configuration tool\n')
        self.cfgdata[BelugaConfig.section_name] = {}

        for opt_name,opt in BelugaConfig.option_list.items():
            opt_done = False
            # Repeat until user enters a valid input
            while not opt_done:
                # Set the default value
                if callable(opt[0]):
                    default_val = opt[0]()       # If it is a function, call it
                else:
                    default_val = str(opt[0])    # Or use string value

                user_val = input(opt[1]+' ['+str(default_val)+']: ')
                if user_val.strip() == '':
                    user_val = default_val

                # Call validation function if one is specified
                if opt[2] is not None and callable(opt[2]):
                    if opt[2](user_val):    # Call validation function
                        break               # Stop if it passes
                    else:
                        continue            # Repeat if it fails
                else:
                    break                   # Stop if no validation function given

            self.cfgdata[BelugaConfig.section_name][opt_name] = user_val

        # Save data into configuration file
        with open(self.config_file, 'w+') as f:
            self.cfgdata.write(f)
        print('Configuration complete.')

if __name__ == '__main__':
    config = BelugaConfig()
#     main()
