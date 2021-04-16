# Lib imports
import numpy as np
import json
# Local imports
from constants import FILES, LAYERS, ConfigOptions
from config import Config

# Function to parse a file and split and store contents
# Returns a np.array with all data
def parseInput(filepath, addExtraInput = False, flatten = 1, normalize = False):
    with open(filepath) as f:
        # Read all lines
        lines = f.readlines()
        data = []
        subdata = [1] if addExtraInput else []
        # Count rows for flattening
        rowCount = 0
        for line in lines:
            rowCount += 1
            if addExtraInput and flatten <= 1:
                data.append(np.array([1.0] + [float(elem) for elem in line.strip().split()]))
            elif addExtraInput and flatten > 1:
                # Append to sub data
                subdata = subdata + [float(elem) for elem in line.strip().split()]
                # Flatten the array
                if rowCount == flatten:
                    data.append(np.array(subdata).flatten())
                    subdata = [1] if addExtraInput else []
                    rowCount = 0
            else:
                data.append(np.array([float(elem) for elem in line.strip().split()]))
            
    data = np.array(data)
    # Normalize between 0 - 1 by dividing by max
    if normalize:
        data = data / data.max()
    return data

# Parses the configuration
def parseConfiguration(configPath):
    with open(configPath) as json_file:
        data = json.load(json_file)
        
        # Get submaps inside config
        files = data[FILES]
        layers = data[LAYERS]
        # Get FILES data
        inputData = files[ConfigOptions.INPUT_DATA.value]
        desiredData = files[ConfigOptions.DESIRED_DATA.value]
        inputDataTest = files[ConfigOptions.INPUT_TEST_DATA.value]
        desiredDataTest = files[ConfigOptions.DESIRED_TEST_DATA.value]
        flatten = files[ConfigOptions.FLATTEN_DATA.value]
        normalizeDesired = files[ConfigOptions.NORMALIZE_DESIRED_DATA.value]
        # Get other data
        iterations = data[ConfigOptions.ITERATIONS.value]
        activation = data[ConfigOptions.ACTIVATION.value]
        learningRate = data[ConfigOptions.LEARNING_RATE.value]
        multilayer = data[ConfigOptions.MULTILAYER.value]
        error = data[ConfigOptions.ERROR_LIMIT.value]
        
        # Create config
        config = Config(
            inputs=inputData,
            inputsTest=inputDataTest,
            desired=desiredData,
            desiredTest=desiredDataTest,
            iterations=iterations,
            activation=activation,
            learningRate=learningRate,
            multilayer=multilayer,
            error=error,
            layers=layers,
            flatten=flatten,
            normalizeDesired=normalizeDesired
        )
    return config