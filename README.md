SpineGuard – AI-Powered Vertebral Disorder Classifier
=====================================================

**End-to-end machine learning platform** for multi-class prediction of spinal conditions:  
**Normal** | **Hernia** | **Spondylolisthesis**

Built with **PyTorch** (model), **FastAPI** (API), modern responsive frontend, and Docker support.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-2.0%2B-orange?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Docker-ready-blue?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

## 🎯 Overview

This project demonstrates a complete ML workflow:
- Data preprocessing & model training (PyTorch)
- Production-grade REST API (FastAPI)
- Clean, responsive web interface for real-time predictions
- Containerization with Docker

Perfect showcase for **machine learning engineering**, **model serving**, and **full-stack ML deployment**.

## 📸 Screenshots

<img width="1907" height="901" alt="image" src="https://github.com/user-attachments/assets/2411703d-4687-4bf1-b7ea-417b1e12243d" />
<img width="1917" height="893" alt="image" src="https://github.com/user-attachments/assets/a4fcace3-fd89-436f-a85a-ac9202ff3975" />



## 📂 Project Structure

```text
spine-ml-platform/
├── app/                    # FastAPI backend
│   ├── api/                # routes & main entry
│   ├── core/               # config & settings
│   ├── services/           # inference & preprocessing logic
│   └── schemas/            # Pydantic models
├── ml/                     # Machine Learning pipeline
│   ├── data/               # raw dataset
│   ├── src/                # ML scripts (train, predict, etc.)
│   └── artifacts/          # trained model & scaler
├── web/                    # Frontend
│   ├── static/             # CSS + JS
│   └── templates/
│       └── index.html
├── Dockerfile
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

### ✅ Prerequisites

- **Python** 3.10+
- **Docker Desktop** (optional but recommended)

### 1️⃣ Clone & install

```bash
git clone https://github.com/YOUR_USERNAME/spine-ml-platform.git
cd spine-ml-platform
pip install -r requirements.txt
```

### 2️⃣ Train the model (run once)

```bash
cd ml/src
python train.py
```

This will create:

- `ml/artifacts/model.pth`
- `ml/artifacts/scaler.pkl`

### 3️⃣ Launch the application

#### Local (recommended for development)

```bash
uvicorn app.api.main:app --reload
```

Open:

- 🌐 `http://127.0.0.1:8000/` → beautiful web interface  
- 📄 `http://127.0.0.1:8000/docs` → interactive API docs

#### Docker (clean & reproducible)

```bash
docker build -t spineguard-app .
docker run -p 8000:8000 spineguard-app
```

Open the same URLs as above.

## 🧪 Example Prediction

### Input (via web form or API)

```json
{
  "pelvic_incidence": 70.2,
  "pelvic_tilt": 13.8,
  "lumbar_lordosis_angle": 48.5,
  "sacral_slope": 56.4,
  "pelvic_radius": 112.1,
  "degree_spondylolisthesis": 18.7
}
```

### Typical output

```json
{
  "class_name": "Spondylolisthesis",
  "confidence": 0.892,
  "probabilities": [0.052, 0.056, 0.892]
}
```

## 📈 Model Performance

Multi-class classification on Vertebral Column Dataset (3 classes):

| Class               | Precision | Recall | F1-Score |
|---------------------|-----------|--------|----------|
| Normal              | 0.70      | 0.80   | 0.74     |
| Hernia              | 0.64      | 0.58   | 0.61     |
| Spondylolisthesis   | 0.93      | 0.87   | 0.90     |
| **Overall Accuracy**| **0.79**  |        |          |

## 🛠️ Tech Stack

- **ML**: PyTorch, scikit-learn, pandas, numpy  
- **API**: FastAPI, Uvicorn, Pydantic  
- **Frontend**: HTML5, CSS3 (modern gradients), vanilla JavaScript  
- **Deployment**: Docker  

## 📜 License

MIT License – feel free to use, modify, and share.

## 👤 Author

**Chiheb Rezgui**  
Big Data & Data Analytics Graduate  
Machine Learning | FastAPI | Docker | Full-Stack ML  
📍 Tunis, Tunisia

