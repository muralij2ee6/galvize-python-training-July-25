from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import numpy as np


class TransactionTransformer:
    def __init__(self):
        self.model_name = "distilbert-base-uncased-finetuned-fraud"
        try:
            self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        except:
            self.train_from_scratch()

    def train_from_scratch(self):
        """Fine-tune on financial fraud data"""
        from datasets import load_dataset
        dataset = load_dataset("financial_phrases_bank", "fraud_cases")

        # Fine-tuning code would go here
        # (See Hugging Face training tutorials)

        self.model.save_pretrained(self.model_name)
        self.tokenizer.save_pretrained(self.model_name)

    def predict(self, transaction_text):
        """Analyze transaction descriptions for fraud signals"""
        inputs = self.tokenizer(
            transaction_text,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )
        outputs = self.model(**inputs)
        return torch.softmax(outputs.logits, dim=1)[0][1].item()  # Fraud probability