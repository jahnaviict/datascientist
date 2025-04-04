import torch
from unsloth import FastLanguageModel, FastTokenizer
from datasets import load_dataset
from peft import LoraConfig

# Model and Tokenizer
model_name = "Qwen/Qwen2.5-7B"
model, tokenizer = FastLanguageModel.from_pretrained(model_name, load_in_4bit=True)
tokenizer.pad_token = tokenizer.eos_token  # Ensure pad token is set

# PEFT LoRA Configuration
lora_config = LoraConfig(
    r=8, lora_alpha=16, lora_dropout=0.1, target_modules=["q_proj", "v_proj"]
)

# Load dataset
dataset = load_dataset("Abirate/gpt4-alpaca", split="train[:1%]")  # Example dataset

def tokenize_function(example):
    return tokenizer(example["instruction"] + " " + example["output"], truncation=True, padding="max_length", max_length=512)

dataset = dataset.map(tokenize_function, batched=True)

dataset = dataset.remove_columns(["instruction", "input", "output"])
dataset.set_format("torch")

# Training Arguments
training_args = {
    "output_dir": "./fine_tuned_model",
    "num_train_epochs": 3,
    "per_device_train_batch_size": 2,
    "save_steps": 100,
    "save_total_limit": 2,
    "logging_dir": "./logs",
    "logging_steps": 10,
    "learning_rate": 2e-5,
    "fp16": torch.cuda.is_available(),
    "bf16": torch.cuda.is_available(),
    "optim": "adamw_torch",
}

# Fine-tune the model
model = FastLanguageModel.get_peft_model(model, lora_config)
trainer = FastLanguageModel.create_trainer(model, tokenizer, dataset, training_args)
trainer.train()

# Save the fine-tuned model
trainer.save_model("./fine_tuned_model")
print("Model fine-tuning complete!")
