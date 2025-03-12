from semantiva.specializations.specialization_loader import SemantivaSpecialization
from semantiva.component_loader import ComponentLoader


class AudioSpecialization(SemantivaSpecialization):
    """Specialization for audio processing"""

    def register(self) -> None:
        registered_modules = [
            "semantiva_audio.processing.processors",
        ]
        ComponentLoader.register_modules(registered_modules)
