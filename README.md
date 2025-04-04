# Fine-tuning LLaMA 8B Model with Alpaca-Formatted Dataset

This repository provides a script to fine-tune the LLaMA 8B model using a dataset formatted in the Alpaca style. The model is fine-tuned using **LoRA (Low-Rank Adaptation)** for efficient training.

---

##  **Setup Instructions**

### 1️ Install Dependencies
Ensure you have Python installed, then install the required libraries:

```bash
pip install -r requirements.txt
```
### 2️ Prepare Your Dataset  

Your dataset should be in **JSON format** with the following fields:  

- **`input`**: The instruction or prompt.  
- **`output`**: The expected response.  
- **`context`**: Any additional context (optional).
  
By running this code:

```bash
python data_format.py
```

### Example JSON format (`alpaca_output.json`):  

```json
[
    {
        "input": "What is AI?",
        "output": "AI stands for Artificial Intelligence.",
        "context": "Technology"
    },
    {
        "input": "What is ML?",
        "output": "ML stands for Machine Learning.",
        "context": "AI subfield"
    }
]
```
Place alpaca_output.json in the same directory as the script.
### 3 Running the Fine-Tuning Script
Run the script to start fine-tuning:

```bash

python training.py
```
