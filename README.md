# 🥔 Potato Leaf Disease Classifier

A deep learning web app that detects diseases in potato leaves from a photo. Upload a leaf image and get an instant AI diagnosis — **Early Blight**, **Late Blight**, or **Healthy**.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 📸 Demo

> Drag and drop a potato leaf photo → get instant disease prediction with confidence scores.

The frontend features an animated potato farm night scene with fireflies, drag-and-drop upload, a confidence progress bar, and per-class score breakdown.

---

## 🌿 Classes

| Label | Description |
|-------|-------------|
| **Early Blight** | Caused by *Alternaria solani* — dark spots with yellow rings on older leaves |
| **Late Blight** | Caused by *Phytophthora infestans* — water-soaked lesions that spread rapidly |
| **Healthy** | No disease detected |

---

## 🗂️ Project Structure

```
potato_leaf_disease_classification/
│
├── backend/
│   ├── main.py               # FastAPI backend
│   └── model_v1.keras        # Trained TensorFlow model
│
├── frontend/
│   └── index.html            # Single-file frontend (no framework needed)
│
├── training/
│   └── potato_disease.ipynb  # Model training notebook
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/your-username/potato-leaf-disease-classifier.git
cd potato-leaf-disease-classifier
```

### 2. Install backend dependencies

```bash
pip install fastapi uvicorn python-multipart pillow tensorflow
```

### 3. Start the backend

Make sure `model_v1.keras` is in the same folder as `main.py`, then run:

```bash
cd backend
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

### 4. Open the frontend

Simply open `frontend/index.html` in your browser — no build step or npm required.

---

## 🔌 API Reference

### `POST /predict`

Accepts a leaf image and returns the predicted class with confidence scores.

**Request**

```
Content-Type: multipart/form-data
Body: file=<image file>
```

**Response**

```json
{
  "prediction": "Early Blight",
  "confidence": 94.73,
  "all_scores": {
    "Early Blight": 94.73,
    "Late Blight": 3.12,
    "Healthy": 2.15
  }
}
```

---

## 🧠 Model

- Architecture: Convolutional Neural Network (CNN)
- Framework: TensorFlow / Keras
- Input size: 256×256 RGB
- Dataset: [PlantVillage Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village)
- Saved format: `.keras`

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Model | TensorFlow / Keras |
| Backend | FastAPI + Uvicorn |
| Frontend | Vanilla HTML, CSS, JavaScript |
| Image Processing | Pillow, NumPy |

---

## ⚠️ Troubleshooting

**`ERR_OSSL_EVP_UNSUPPORTED` when running React frontend**
```cmd
set NODE_OPTIONS=--openssl-legacy-provider
npm start
```

**Backend not reachable from frontend**
Make sure the backend is running on port 8000 and CORS is enabled (it is by default in `main.py`).

**Model not found error**
Ensure `model_v1.keras` is in the same directory as `main.py`.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [PlantVillage Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village) for training data
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [TensorFlow](https://www.tensorflow.org/) for the deep learning framework
