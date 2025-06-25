# 🛠️ Modular Python API with Google Cloud Run Deployment

This project demonstrates a fully modular Python API built with FastAPI, containerized with Docker, and deployed to **Google Cloud Run**. The API is intentionally lightweight, focusing on scalable structure, clean deployment workflows, and easy cloud portability.

---

## 📄 Overview

- FastAPI-powered modular API  
- Fully containerized using Docker  
- Deployed to Google Cloud Run  
- Integrated with **Google Artifact Registry** for container storage  
- Designed as a reusable, scalable foundation for API-based Python projects  

---

## 🧰 Key Features

- 📦 Containerized with Docker for portability  
- ☁️ Deployed on Google Cloud Run with scalable API endpoints  
- ⚙️ API-driven architecture using FastAPI  
- 🛠️ Modular Python code structure ready for expansion  
- 🔄 Cloud-native deployment flow using Google Artifact Registry  
- ⚡ Runs on Uvicorn for fast asynchronous API serving  

---

## 🧩 Notes

- This project is designed as a **template** for scalable, cloud-deployed Python APIs.  
- The modular structure makes it easy to add:
  - Additional API endpoints  
  - Browser automation tasks  
  - Custom workflows or external integrations  
- Deployment files (Dockerfile, cloud configuration) are included for fast redeployment.  

---

## 🏗️ Cloud Deployment Flow

1. **Containerization:** The Python API is dockerized for easy portability.  
2. **Artifact Registry:** The Docker image is pushed to **Google Artifact Registry** for secure storage.  
3. **Google Cloud Run:** The container is deployed to **Google Cloud Run** for fully managed, scalable hosting.  

---

## 🚀 Local Setup (Optional)

Clone the repository:
```bash
git clone <repo_url>
cd <repo_folder>
```

Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run the FastAPI app locally:
```bash
uvicorn browser_script:app --host 0.0.0.0 --port 8080
```

---

## ⚙️ Dependencies

- FastAPI  
- Uvicorn  
- Playwright  
- Docker  
- Google Cloud Run  
- Google Artifact Registry  

---

## 👤 About

Created by Brett C. as part of my Python automation and cloud deployment portfolio. I specialize in building modular, scalable Python systems that are easy to maintain, expand, and redeploy across cloud platforms.

---

## 📝 License

MIT
