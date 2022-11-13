from premium.exception import PremiumException
from premium.logger import logging
from premium.entity.config_entity import DataIngestionConfig
from premium.entity.artifact_entity import DataIngestionArtifact
import os, sys
import zipfile
import numpy as np
from six.moves import urllib
import pandas as pd
from premium.constant import *
from sklearn.model_selection import StratifiedShuffleSplit