# 🚀 AI-Based Software Engineering Toolkit API

This FastAPI-based project provides a set of intelligent tools to assist in early-stage software engineering — from ideation to architecture planning, specification drafting, effort estimation using COCOMO II, folder structure generation, and GitHub uploading. Each tool is accessible through dedicated API endpoints.

---

## 📁 Project Structure

```
.
├── main.py                           # Entry point for the FastAPI app
├── tool1_feature_suggestion.py      # Tool 1 - Feature Suggestion
├── tool1_feature_classification.py  # Tool 1 - Feature Classification
├── tool2_cocomo2_parameters.py      # Tool 2 - COCOMO Parameter Generator
├── tool2_cocomo2_evaluation.py      # Tool 2 - COCOMO Evaluator
├── tool2_specsheet_generator.py     # Tool 2 - Specification Sheet Generator
├── tool3_folder_structure_generator.py # Tool 3 - Folder Structure Generator
├── tool4_github_uploader.py         # Tool 4 - GitHub Repository Uploader
└── utils/                           # Utility functions used across tools
```

---

## 🧠 Tools Overview

### **Tool 1: Ideation Assistant**

* Suggests features and tech stack based on project idea.
* Classifies features into basic, intermediate, and advanced.

### **Tool 2: Project Planning**

* Generates COCOMO II parameters.
* Evaluates project effort/schedule using COCOMO II.
* Generates a comprehensive spec sheet.

### **Tool 3: Folder Structure Generator**

* Auto-generates folder structures based on tech stack and project idea.

### **Tool 4: GitHub Repo Uploader**

* Uploads the generated folder structure to a GitHub repository.

---

## 📌 API Endpoints

### 🔹 1. Suggest Features & Tech Stack

**POST** `/api/tool1/suggest`

#### Request:

```json
{
  "project_idea": "AI-based health monitoring system",
  "max_repos": 10
}
```

#### Response:

```json
{
  "suggested_features": "Heart rate monitoring, Temperature tracking, Report generation",
  "suggested_tech_stack": "Python, Flask, SQLite",
  "total_repos_processed": 10
}
```

---

### 🔹 2. Classify Features by Level

**POST** `/api/tool1/classify-features`

#### Request:

```json
{
  "project_idea": "AI-based health monitoring system",
  "suggested_features_text": "Heart rate monitoring, Temperature tracking, Report generation"
}
```

#### Response:

```json
{
  "basic": ["Heart rate monitoring"],
  "intermediate": ["Temperature tracking"],
  "advanced": ["Report generation"]
}
```

---

### 🔹 3. Generate COCOMO II Parameters

**POST** `/api/tool2/cocomo2/generate-parameters`

#### Request:

```json
{
  "software": "Health Monitoring System",
  "level": "intermediate",
  "features": ["Heart rate monitoring", "Temperature tracking"]
}
```

#### Response:

```json
{
  "effort_drivers": {...},
  "scale_factors": {...},
  "function_points": {...}
}
```

---

### 🔹 4. Evaluate COCOMO II Effort

**POST** `/api/tool2/cocomo2_evaluation`

#### Request:

```json
{
  "function_points": {...},
  "reuse": {...},
  "revl": {...},
  "effort_schedule": {...}
}
```

#### Response:

```json
{
  "status": "success",
  "results": {
    "estimated_effort": 120.5,
    "schedule_in_months": 5.4,
    ...
  }
}
```

---

### 🔹 5. Generate Specification Sheet

**POST** `/api/generate/specsheet`

#### Request:

```json
{
  "software": "Health Monitoring System",
  "level": "intermediate",
  "features": ["Heart rate monitoring", "Temperature tracking"],
  "api_results": {...}
}
```

#### Response:

```json
{
  "specsheet": "Comprehensive formatted specification text..."
}
```

---

### 🔹 6. Generate Folder Structure

**POST** `/api/generate/folder-structure`

#### Request:

```json
{
  "project_idea": "AI-based health monitoring system",
  "suggested_features": "Heart rate monitoring, Temperature tracking",
  "suggested_tech_stack": "Python, Flask, SQLite",
  "total_repos_processed": 10,
  "preferences": "MVC structure"
}
```

#### Response:

```json
{
  "folder_structure": {
    "type": "folder",
    "name": "project_root",
    "children": [
      {
        "type": "folder",
        "name": "backend",
        "children": [...]
      },
      ...
    ]
  },
  "project_idea": "...",
  "suggested_features": "...",
  "total_repos_processed": 10
}
```

---

### 🔹 7. Upload Project to GitHub

**POST** `/api/tool4/upload-to-github`

#### Environment Variables Required:

* `GITHUB_USERNAME`
* `GITHUB_TOKEN`

#### Request:

```json
{
  "name": "health-monitoring-system",
  "structure": [
    {
      "type": "folder",
      "name": "backend",
      "children": [...]
    }
  ]
}
```

#### Response:

```json
{
  "status": "success",
  "message": "Repository created and code uploaded",
  "repo_name": "health-monitoring-system"
}
```

---

## 🛠️ Setup Instructions

1. **Install dependencies**

```bash
pip install fastapi uvicorn python-dotenv requests
```

2. **Create `.env` file**

```
GITHUB_USERNAME=your_username
GITHUB_TOKEN=your_github_token
```

3. **Run the server**

```bash
uvicorn main:app --reload
```

4. **Access Swagger docs**
   Visit: `http://127.0.0.1:8000/docs`

---

## ✨ Features

* Modular FastAPI architecture.
* Seamless GitHub integration.
* Smart feature and tech stack ideation.
* COCOMO II-based effort estimation.
* Auto-spec sheet and folder structure generator.

---

## 📌 Notes

* External APIs like `https://github-project-extractor.onrender.com/ideate` and `https://krivisio-githubcodeuploader.onrender.com/create-and-upload` are used.
* Make sure you have an active GitHub token with repository permissions for Tool 4.
