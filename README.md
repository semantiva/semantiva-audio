# Semantiva - Audio specialization

## Overview

`semantiva_audio` is the audio specialization of the [Semantiva](https://docs.semantiva.org/) framework. It offers tailored data types and operations for
audio operations. This module provides algorithms for processing **single-channel** and **dual-channel** audio data.  It includes specialized algorithms for both types, as well as utilities for merging dual-channel audio into a single-channel format and expanding single-channel audio into dual-channel.


## Installation

This module is available via Pypi:

`pip install semantiva_audio`

This command should install the package and all its dependencies, including Semantiva itself.

---

## Getting Started: A Minimal Example

Below is a quick demonstration showing how to use the specialization.  This assumes that the installation section was completed successfully.  In this example, we will create a custom audio algorithm **SingleChannelAudioMultiplyAlgorithm**,   which multiplies single-channel audio data by a given factor.

```python
import numpy as np
from semantiva_audio.audio_data_types import SingleChannelAudioDataType
from semantiva_audio.audio_operations import SingleChannelAudioAlgorithm

class SingleChannelAudioMultiplyAlgorithm(SingleChannelAudioAlgorithm):
    """
    A specialized algorithm to multiply single-channel audio data by a given factor.
    """

    def _operation(self, data, factor):
        self.logger.debug("Inside the SingleChannelAudioMultiplyAlgorithm")
        multiplied_data = data.data * factor
        return SingleChannelAudioDataType(multiplied_data)

# Example usage of SingleChannelAudioMultiplyAlgorithm

# Create an instance of the multiplication algorithm
multiply_algorithm = SingleChannelAudioMultiplyAlgorithm()

# Example input: Single-channel audio data
input_audio = SingleChannelAudioDataType(np.random.rand(1000))

# Define a multiplication factor
factor = 2.0

# Process the data using the algorithm
output_audio = multiply_algorithm._operation(input_audio, factor)

```

### Explanation:

1. **Class Inheritance**:
   - `SingleChannelAudioMultiplyAlgorithm` extends `SingleChannelAudioAlgorithm`, which defines input/output data types.

2. **Custom Operation**:
   - The `_operation(data, factor)` method multiplies every element in the input audio data by a specified factor.
   - The method takes `SingleChannelAudioDataType` as input and returns a new instance of the same type.

3. **Usage Example**:
   - We create a `SingleChannelAudioMultiplyAlgorithm` instance.
   - Provide an example single-channel audio input with numerical values.
   - Define a multiplication factor (`2.0` in this case).
   - Call `_operation(input_audio, factor)` to process the data.
   - The modified output is printed, showing the multiplied values.

---
## License

Semantiva is released under the [MIT License](./LICENSE), promoting collaborative development and broad adoption.


## Acknowledgments

This framework draws inspiration from the rigorous demands of transparency and traceability in data-driven systems, particularly exemplified by the ALICE O2 project at CERN. The lessons learned from managing large-scale, high-throughput data in that environment—combined with the need for robust, domain-aligned workflows—shaped Semantiva’s emphasis on type-safe design, semantic clarity, and modular extensibility. By blending these concepts with principles of ontology-driven computing, Semantiva aims to deliver the same level of reliability and interpretability for any domain requiring advanced data processing and HPC integration.
