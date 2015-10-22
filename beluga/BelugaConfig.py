from configparser import SafeConfigParser
import os.path, os
import sys

class BelugaConfig:
    """Defines configuration options for Beluga and allows loading/saving configuration files"""
    section_name = 'beluga'
    option_names = {
        'root':['','Set Beluga installation path '], # Installation directory
        # 'default_solver':['SingleShooting','Select default BVP solver ']
    }


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
                                for option in BelugaConfig.option_names):
                    self.config_tool()

        # Create easily accessible variable
        self.config = self.cfgdata[BelugaConfig.section_name]

    def config_tool(self,arguments=None):
        """Interacts with user to configure Beluga"""

        print('Welcome to the Beluga configuration tool\n')
        self.cfgdata[BelugaConfig.section_name] = {}

        default_path = os.path.abspath(os.path.dirname(__file__)+'/../')

        inst_path = input('Set Beluga installation path ['+default_path+']: ')
        if inst_path.strip() == '':
            inst_path = default_path

        if os.path.isdir(inst_path):
            self.cfgdata[BelugaConfig.section_name]['root'] = inst_path
        else:
            sys.stderr.write('Invalid path!')
            return

        with open(self.config_file, 'w+') as f:
            self.cfgdata.write(f)
        print('Configuration complete.')

# import argparse
# from gooey import Gooey
#
# @Gooey(program_name='Beluga configuration tool')
# def main():
#     default_path = os.path.abspath(os.path.dirname(__file__))
#     parser = argparse.ArgumentParser()
#
#     parser.add_argument('-r','--root',default=default_path, help='Select Beluga installation path', widget="DirChooser")
#
#     args = parser.parse_args()
#     print(args)
#     # BelugaConfig(run_tool = True, arguments = args)
#
# if __name__ == '__main__':
#     main()
