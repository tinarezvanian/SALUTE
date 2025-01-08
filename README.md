# SALUTE: Suicide-prevention AI using Language Understanding for Timely Engagement

This repository hosts the code for **SALUTE**, a proof-of-concept system designed to assist mental health professionals in detecting suicide risk factors among veterans and providing timely interventions. The acronym **SALUTE** stands for **Suicide-prevention AI using Language Understanding for Timely Engagement**.

---
## Table of Contents
1. [Overview](#overview)  
2. [Key Features](#key-features)  
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [Training and Evaluation](#training-and-evaluation)  
7. [License & Disclaimers](#license--disclaimers)  
8. [References](#references)  
9. [Contact](#contact)

---

## Overview

Veteran suicide remains a significant public health crisis. **SALUTE** aims to fill the gap in after-hours mental health coverage by leveraging **parameter-efficient fine-tuning** of large language models (LLMs) to identify at-risk language cues. By focusing on multi-step reasoning strategies and environment-based “language decision processes,” this project attempts to create a *clinical co-pilot* that can both reduce clinician workload and improve mental health outcomes for at-risk veterans.

**Key objectives:**
- **Timely Identification:** Detect suicidal or depressive language in real-time text.
- **Context-Aware Interventions:** Provide immediate escalation options or empathetic responses, guided by subject matter experts (SMEs).
- **24/7 Feasibility:** Leverage smaller, more cost-effective models (LoRA or QLoRA) to enable around-the-clock deployment.

---

## Key Features

- **LoRA-based Fine-Tuning** – Utilizes parameter-efficient techniques (e.g. [LoRA](https://arxiv.org/abs/2106.09685)) to adapt LLMs on limited hardware.  
- **Multi-Step Conversation** – Inspired by environment-based language agents, SALUTE can reason, “observe,” and “act” across repeated cycles.  
- **Tool Integration** – Potential to query external crisis-line databases, scheduling systems, or VA resources for context-aware advice or escalation.  
- **High Accuracy** – Demonstrates near 99% accuracy on a *Suicide Watch* dataset (Kaggle-based), showing potential for real-world mental health screening tasks.

---

## Getting Started

### Prerequisites
- Python 3.8+  
- [PyTorch](https://pytorch.org/) (or [Accelerate](https://github.com/huggingface/accelerate)) for GPU acceleration  
- [Hugging Face Transformers](https://github.com/huggingface/transformers)  
- [Datasets](https://github.com/huggingface/datasets) for data loading  
- A supported GPU (NVIDIA/CUDA or Apple Silicon MPS) – or run on CPU for demonstration

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/tinarezvanian/veterans.git
cd veterans

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt
