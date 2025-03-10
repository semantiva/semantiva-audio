from semantiva.specializations.specialization_loader import load_specializations
from semantiva.component_loader import ComponentLoader


def test_registering_specialization():
    """Test registering the audio specialization"""
    # ComponentLoader.get_registered_modules()
    load_specializations("audio")
    assert (
        "semantiva_audio.processing.processors"
        in ComponentLoader.get_registered_modules()
    )
