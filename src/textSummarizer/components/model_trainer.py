from transformers import TrainingArguments, Trainer, DataCollatorForSeq2Seq, AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
from textSummarizer.entity import ModelTrainerConfig
import torch
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        # Loading data
        dataset = load_from_disk(self.config.data_path)

        # Define training arguments
        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=5,  # Increased number of epochs
            warmup_steps=500,
            per_device_train_batch_size=2,  # Increased batch size
            per_device_eval_batch_size=2,
            weight_decay=0.01,
            logging_steps=10,
            evaluation_strategy='steps',
            eval_steps=500,
            save_steps=1000,  # More frequent checkpointing
            gradient_accumulation_steps=8,  # Adjusted for new batch size
            fp16=True,  # Enable mixed precision training
            learning_rate=3e-5,  # Adjusted learning rate
        )

        # Initialize Trainer
        trainer = Trainer(
            model=model,
            args=training_args,
            tokenizer=tokenizer,
            data_collator=data_collator,
            train_dataset=dataset["train"],
            eval_dataset=dataset["validation"]
        )

        # Train the model
        trainer.train()

        # Save the model and tokenizer
        model.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
