from .step import Step
from .step import StepException

class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in Preflight')
        utils.create_dirs()