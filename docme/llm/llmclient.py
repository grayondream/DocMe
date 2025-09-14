from enum import Enum, auto
from base.singleton import SingletonBase
from llm.ollama.ollamaclient import OllamaModel

class LLMModelType(Enum):
    OLLAMA = auto()
    REMOTE = auto()

class LLMClient(SingletonBase):
    def __init__(self, model_type: LLMModelType, model_name: str):
        # Always validate the model_type, even if the instance is already initialized
        if model_type == LLMModelType.OLLAMA:
            if not hasattr(self, 'initialized'):
                self.model = OllamaModel(model_name=model_name)
                self.initialized = True
        elif model_type == LLMModelType.REMOTE:
            raise NotImplementedError("REMOTE model type is not implemented yet")
        else:
            raise ValueError(f"Invalid model type: {model_type}. Use LLMModelType.OLLAMA or LLMModelType.REMOTE.")

    def generate(self, prompt: str) -> str:
        return self.model.generate(prompt)