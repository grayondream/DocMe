import requests

kOllamaDefaultBaseUrl = "http://localhost:11434"
class OllamaModel:
    def __init__(self, model_name: str, base_url: str = kOllamaDefaultBaseUrl):
        self.model_name = model_name
        self.base_url = base_url

    def generate(self, prompt: str) -> str:
        url = f"{self.base_url}/generate"
        payload = {
            "model": self.model_name,
            "prompt": prompt
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # 检查请求是否成功
            return response.json().get("completion", "")
        except requests.exceptions.RequestException as e:
            print(f"Error calling Ollama model: {e}")
            return ""