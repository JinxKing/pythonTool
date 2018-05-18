# coding: utf-8

"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options: 
    -h,--help        显示帮助菜单
    -g               高铁
    -d               动车
    -t               特快
    -k               快速
    -z               直达

Example:
    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01
"""

# def cli():
#     """command-line interface""" 
#     arguments = docopt(__doc__)
#     print(arguments)

# if __name__ == '__main__': 
#     cli()

from docopt import docopt

class Cli(object):

     def __init__(self):
        self.arguments = docopt(__doc__, version='Tickets 1.0')
        ## Cli参数解析
        self.from_station = stations.get_telecode(self.arguments['<from>'])
        self.to_station = stations.get_telecode(self.arguments['<to>'])
        self.date = self.arguments['<date>']
        self.check_arguments_validity()
        self.options = ''.join([key for key, value in self.arguments.items() if value is True])
