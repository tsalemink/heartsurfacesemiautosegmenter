'''
MAP Client Plugin
'''

__version__ = '0.1.0'
__author__ = 'Hugh Sorby'
__stepname__ = 'Heart Surface Semi Auto Segmenter'
__location__ = 'https://github.com/mapclient-plugins/heartsurfacesemiautosegmenter/archive/master.zip'

# import class that derives itself from the step mountpoint.
from mapclientplugins.heartsurfacesemiautosegmenterstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
