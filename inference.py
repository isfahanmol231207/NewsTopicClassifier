from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load your fine-tuned model
model_path = "models/bert-agnews"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Create pipeline
clf = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Test with some examples
examples = [
    "The stock market crashed due to inflation fears.",
    "The new iPhone was released with groundbreaking features.",
    "The football team won the championship.",
    "Global leaders meet to discuss climate change."
]

for text in examples:
    print(f"Text: {text}")
    print("Prediction:", clf(text))
    print("-" * 50)
