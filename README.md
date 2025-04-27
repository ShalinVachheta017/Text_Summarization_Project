# pegasus-dialogue-summarization



# Text Summarization Project 🚀

> Fine-tuning PEGASUS on the SAMSum dataset to summarize conversational dialogues into short, meaningful text summaries.  
> Built with a complete ML pipeline: Research ➔ Modular Codebase ➔ API Deployment ➔ Dockerization.

---

## 📚 Problem Statement

Modern conversations (chat, emails, messages) often contain redundant and lengthy information.  
**Text summarization** helps extract key information efficiently, saving time and effort.

This project focuses on building a **dialogue summarization system** using **Transformer-based models**.

---

## 🎯 Project Goals

- Fine-tune **google/pegasus** model on real-world chat conversations (SAMSum dataset).
- Build an **end-to-end machine learning pipeline**: from data ingestion to model evaluation.
- Deploy the trained summarizer via an **API**.
- Containerize the entire application using **Docker** for easy deployment.

---

## 🏗️ Project Architecture

| Stage | Details |
|:------|:--------|
| **Research Notebooks** | Data ingestion, validation, transformation, training, evaluation (modular Jupyter notebooks). |
| **Training Pipeline (Python scripts)** | Modularized under `src/textSummarizer/` using Clean Code principles. |
| **Configuration Management** | `params.yaml` (training parameters) and `config/config.yaml` (paths/settings). |
| **Model Serving** | `app.py` to deploy model API (FastAPI based). |
| **Docker Containerization** | `Dockerfile` for building and running the app easily. |

---

## 📂 Project Structure

```bash
Text_Summarization_Project/
├── .github/workflows/        # CI/CD workflows (future-ready)
├── config/                   # Configuration files
│    └── config.yaml
├── research/                 # Jupyter notebooks for research and experimentation
│    ├── 01_data_ingestion.ipynb
│    ├── 02_data_validation.ipynb
│    ├── 03_data_transformation.ipynb
│    ├── 04_model_trainer.ipynb
│    ├── 05_model_evaluation.ipynb
│    ├── Text_Summarization.ipynb
│    └── trials.ipynb
├── src/textSummarizer/        # Core source code
│    ├── components/           # Modular components (ingestion, training etc.)
│    ├── config/               # Configuration parsers
│    ├── constants/            # Constant values
│    ├── entity/               # Data schemas
│    ├── logging/              # Logging utilities
│    ├── pipeline/             # Training and prediction pipelines
│    ├── utils/                # Helper functions
│    └── __init__.py
├── app.py                     # Serve model API
├── main.py                    # Main runner
├── Dockerfile                 # Docker setup
├── setup.py                   # Package installation
├── requirements.txt           # Project dependencies
├── params.yaml                # Hyperparameters for training
├── README.md                  # Project documentation
└── template.py                # Folder structure generator
```

---

## 🔥 Key Features

- **Fine-tuning** PEGASUS-large model using Hugging Face Transformers.
- **Research-first Approach** with modular notebooks.
- **Production-Ready Codebase** inside `src/textSummarizer/`.
- **Config-Driven Development** using `yaml` files.
- **Containerization** with Docker for easy deployment.
- **Scalable Architecture** – ready for extending to larger datasets or newer models.

---

## 🛠 Tech Stack

- Python 3.8+
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- Flask (for API serving)
- Docker
- YAML Configuration Management
- GitHub Actions (for future CI/CD)

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ShalinVachheta017/Text_Summarization_Project.git
cd Text_Summarization_Project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python main.py
```

### 4. Run the API Server

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000/`.

---



Sample Input:

```
Alex: Are we still on for 6 PM?
Jordan: Running 10 minutes late, but yes!
```

Generated Summary:

> Alex and Jordan plan to meet at 6 PM, with a slight delay.

---

## ⚡ Future Work

- Deploy model on Hugging Face Spaces / Streamlit.
- Fine-tune PEGASUS on larger dialogue datasets (e.g., Reddit conversations).
- Experiment with model distillation to reduce size and improve speed.
- Add MLflow tracking for experiments and metrics.
- Add CI/CD pipeline for automatic deployment.

---

## 🙋‍♂️ Author

- **Shalin Vachheta**  
- [GitHub](https://github.com/ShalinVachheta017) | [LinkedIn](https://linkedin.com/in/shalin-vachheta)

---

> _"Summarizing conversations is not just compression, it's distilling meaning."_ 🌟

---

