import unittest
from unittest.mock import patch
import sys
import os
# Add the docme directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'docme'))

from llm.llmclient import LLMClient, LLMModelType
from llm.ollama.ollamaclient import OllamaModel

class TestLLMClient(unittest.TestCase):

    @patch('llm.ollama.ollamaclient.OllamaModel.__init__')
    @patch('llm.ollama.ollamaclient.OllamaModel.generate')
    def test_initialize_local_model(self, mock_generate, mock_init):
        # Configure the mocks
        mock_init.return_value = None  # __init__ should return None
        mock_generate.return_value = "Mock response"

        client = LLMClient(LLMModelType.OLLAMA, "deepseek-r1:7b")

        self.assertIsNotNone(client.model)
        # Check that OllamaModel was instantiated with the correct parameters
        mock_init.assert_called_once_with(model_name="deepseek-r1:7b")
        
        response = client.generate("Test prompt")
        self.assertEqual(response, "Mock response")
        mock_generate.assert_called_once_with("Test prompt")

    def test_invalid_model_type(self):
        # Test that the REMOTE model type raises NotImplementedError
        from llm.llmclient import LLMModelType
        
        # Reset the singleton instance to ensure we get a fresh instance
        # Access the _instances dictionary through the metaclass
        if hasattr(LLMClient, '__class__') and hasattr(LLMClient.__class__, '_instances'):
            LLMClient.__class__._instances.pop(LLMClient, None)
        
        with self.assertRaises(NotImplementedError) as context:
            LLMClient(LLMModelType.REMOTE, "test_model")
        
        # Check that the error message is correct
        self.assertIn("REMOTE model type is not implemented yet", str(context.exception))

if __name__ == "__main__":
    unittest.main()