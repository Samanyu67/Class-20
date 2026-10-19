import requests

MODEL_URL = "https://huggingface.co"
HF_TOKEN = "YOUR_HUGGING_FACE_API_TOKEN"

def summarize_text(text, max_length=130, min_length=30):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": max_length,
            "min_length": min_length,
            "do_sample": False
        }
    }
    
    response = requests.post(MODEL_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]['summary_text']
    else:
        return f"Error {response.status_code}: {response.text}"

if __name__ == "__main__":
    sample_text = (
        "The Hugging Face Inference API allows developers to quickly integrate state-of-the-art "
        "machine learning models into their applications without having to host the heavy model "
        "weights locally. By sending a simple HTTP request, you can perform tasks like text "
        "generation, translation, classification, and summarization. Models like Facebook's "
        "BART and Google's Pegasus are specifically fine-tuned on large datasets to compress long "
        "documents into concise, readable summaries while maintaining the original context."
    )
    
    print(summarize_text(sample_text, max_length=50, min_length=15))
