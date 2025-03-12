import numpy as np
from semantiva_audio.data_types.data_types import (
    SingleChannelAudioDataType,
    DualChannelAudioDataType,
)
from semantiva_audio.processing.operations import (
    SingleChannelAudioOperation,
    DualChannelAudioOperation,
)


class SingleChannelAudioMultiplyOperation(SingleChannelAudioOperation):
    """
    A specialized operation to multiply single-channel audio data by a given factor.
    """

    def _process_logic(self, data, factor):
        self.logger.debug("Inside the SingleChannelAudioMultiplyOperation")
        multiplied_data = data.data * factor
        return SingleChannelAudioDataType(multiplied_data)


class DualChannelAudioMultiplyOperation(DualChannelAudioOperation):
    """
    A specialized operation to multiply each channel of dual-channel audio data
    by a given factor, reusing SingleChannelAudioMultiplyOperation.
    """

    def _process_logic(self, data, factor):
        self.logger.debug("Inside the SingleChannelAudioMultiplyOperation")
        left_channel = SingleChannelAudioDataType(data.data[:, 0])
        right_channel = SingleChannelAudioDataType(data.data[:, 1])

        single_channel_multiplier = SingleChannelAudioMultiplyOperation()

        left_result = single_channel_multiplier(left_channel, factor)
        right_result = single_channel_multiplier(right_channel, factor)

        multiplied_data = np.column_stack((left_result.data, right_result.data))
        return DualChannelAudioDataType(multiplied_data)
