from netparsers.staticnets import StaticNet
from typing import Tuple
from models.realmodels import *
from models.stochModels import *
from optstructs import *

def get_model_module(model_name:str) -> Tuple[StaticNet,allOpts]:
	opts = globals()[model_name]()
	module = StaticNet(opts.netopts)
	return module, opts