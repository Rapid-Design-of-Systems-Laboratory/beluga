from configparser import SafeConfigParser
import os.path
import sys

# TODO: Fix config file being created in every folder!!!
class BelugaConfig:
    """Defines configuration options for Beluga and allows loading/saving configuration files"""
    section_name = 'beluga'
    option_names = [
        'root', # Installaton directory
    ]
    def __init__(self, config_file = 'config.ini', run_tool = False):
        """Initializes a BelugaConfig object with existing an config file or defaults"""
        self.cfgdata = SafeConfigParser()
        self.config_file = config_file

        if run_tool:
            self.config_tool()
        if config_file is not None:
            if not os.path.isfile(config_file):
                self.config_tool() # Run configuration tool if file is missing

            self.cfgdata.read(config_file)
            if BelugaConfig.section_name not in self.cfgdata:
                # If config file does not have the required information ask the user
                self.cfgdata[BelugaConfig.section_name] = {}
                self.config_tool()
            else:
                # If all the listed options are not present in the file
                # run the configuration tool
                # TODO: Validate individual options even if they exist in the file
                if not all(option in self.cfgdata[BelugaConfig.section_name]
                                for option in BelugaConfig.option_names):
                    self.config_tool()

        # Create easily accessible variable
        self.config = self.cfgdata[BelugaConfig.section_name]


    def config_tool(self):
        """Interacts with user to configure Beluga"""
        print('Welcome to the Beluga configuration tool\n')
        self.cfgdata[BelugaConfig.section_name] = {}

        inst_path = input('Set Beluga installation path ['+os.getcwd()+']: ')
        if inst_path.strip() == '':
            inst_path = os.getcwd()

        if os.path.isdir(inst_path):
            self.cfgdata[BelugaConfig.section_name]['root'] = inst_path
        else:
            sys.stderr.write('Invalid path!')
            return

        with open(self.config_file, 'w') as f:
            self.cfgdata.write(f)
        print('Configuration complete.')

if __name__ == '__main__':
    cfg = BelugaConfig(run_tool = True)
