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
  "project_idea": "video calling",
  "max_repos": 3
}
```

#### Response:

```json
{
  "suggested_features": "### Suggested New Features:\n\n1. **Automated Task Estimation**: This feature uses machine learning algorithms to estimate task completion time based on user performance, task complexity, and historical data. It will help users set realistic deadlines and create more accurate project schedules.\n\n2. **Intelligent Task Assignment**: A feature that suggests tasks to team members based on their skill sets, availability, and past performance. This ensures effective allocation of workload and increases team productivity.\n\n3. **Milestone-Based Progress Reporting**: In addition to project tracking, this feature will allow project managers to set specific milestones and track progress towards them. It provides a more comprehensive view of the project's overall progress.\n\n4. **Knowledge Base and Wiki**: A centralized knowledge base where team members can share information, guidelines, and best practices related to the project. This promotes knowledge sharing and reduces the need for unnecessary meetings.\n\n5. **Collaborative File Management**: A feature that allows multiple users to work on documents simultaneously, reducing the risk of version conflicts. It also provides a history of all changes made to the document.\n\n6. **User Profiling and Analytics**: A feature that tracks user activity, providing insights into usage patterns, task effectiveness, and other key metrics. This helps identify areas for improvement and informs data-driven decision-making.\n\n7. **Project Template Library**: A library of pre-built project templates that can be easily customized and applied to future projects. This saves time and ensures consistency across similar projects.\n\n8. **Integrations with Calendar and Scheduling Tools**: Seamless integration with popular calendar and scheduling tools to enable team members to schedule tasks and deadlines directly into their calendars.\n\n9. **Machine Learning-based Task Prioritization**: A feature that uses machine learning algorithms to analyze task dependencies, deadlines, and team workload to determine the most critical tasks that need attention first.\n\n10. **Real-time Translation and Localization**: A feature that enables teams to work on projects that require multiple languages, providing real-time translation and automatic localization of text and comments.\n\n### Potential Future Developments:\n- Implementing augmented reality (AR) capabilities for remote collaboration and presentation purposes.\n- Integrating AI-powered chatbots for automated issue resolution and support.\n- Developing a mobile app for on-the-go access to project management tools.\n- Expanding analytics capabilities to provide more detailed insights and predictive models.\n\n### Notes:\n- When implementing new features, assess the potential impact on system performance, scalability, and overall user experience.\n- Continuously collect user feedback to iteratively refine and improve the system.\n- Develop a phased rollout plan for new features to minimize disruption and ensure maximum adoption.",
  "suggested_tech_stack": "Python (using Flask or Django)\nNode.js (using Express.js)\nReact\nAngular\nVue.js\nMySQL\nPostgreSQL\nMongoDB\nAxios\nfetch\njQuery\nPassport.js (for Node.js)\nDjango's built-in authentication\nAsana\nTrello\nJira\nGit (with GitHub or Bitbucket)\nDocker\nKubernetes\nHeroku\nAWS Elastic Beanstalk\nWebpack\nGulp\nRollup\nTensorFlow\nPyTorch\nKeras\nscikit-learn\nD3.js\nMatplotlib\nSeaborn\nPlotly\nTableau\nPower BI\nPostgreSQL with PostgreSQL-specific extensions\nRedis\nElasticsearch\nSolr\nNext.js\nGatsby\nStorybook\nTypeScript\nESLint\nPrettier\nJest\nCypress\nMocha\nChai\nSinon\nAWS Lambda\nAzure Functions\nGoogle Cloud Functions\nApex Code\nCloudwatch\nNew Relic\nRollbar\nSentry\nCircleCI\nBamboo\nJenkins\nAnsible\nTerraform",
  "total_repos_processed": 3
}
```

---

### 🔹 2. Classify Features by Level

**POST** `/api/tool1/classify-features`

#### Request:

```json
{
  "project_idea": "video calling",
  "suggested_features_text": "### Suggested New Features:\n\n1. **Automated Task Estimation**: This feature uses machine learning algorithms to estimate task completion time based on user performance, task complexity, and historical data. It will help users set realistic deadlines and create more accurate project schedules.\n\n2. **Intelligent Task Assignment**: A feature that suggests tasks to team members based on their skill sets, availability, and past performance. This ensures effective allocation of workload and increases team productivity.\n\n3. **Milestone-Based Progress Reporting**: In addition to project tracking, this feature will allow project managers to set specific milestones and track progress towards them. It provides a more comprehensive view of the project's overall progress.\n\n4. **Knowledge Base and Wiki**: A centralized knowledge base where team members can share information, guidelines, and best practices related to the project. This promotes knowledge sharing and reduces the need for unnecessary meetings.\n\n5. **Collaborative File Management**: A feature that allows multiple users to work on documents simultaneously, reducing the risk of version conflicts. It also provides a history of all changes made to the document.\n\n6. **User Profiling and Analytics**: A feature that tracks user activity, providing insights into usage patterns, task effectiveness, and other key metrics. This helps identify areas for improvement and informs data-driven decision-making.\n\n7. **Project Template Library**: A library of pre-built project templates that can be easily customized and applied to future projects. This saves time and ensures consistency across similar projects.\n\n8. **Integrations with Calendar and Scheduling Tools**: Seamless integration with popular calendar and scheduling tools to enable team members to schedule tasks and deadlines directly into their calendars.\n\n9. **Machine Learning-based Task Prioritization**: A feature that uses machine learning algorithms to analyze task dependencies, deadlines, and team workload to determine the most critical tasks that need attention first.\n\n10. **Real-time Translation and Localization**: A feature that enables teams to work on projects that require multiple languages, providing real-time translation and automatic localization of text and comments.\n\n### Potential Future Developments:\n- Implementing augmented reality (AR) capabilities for remote collaboration and presentation purposes.\n- Integrating AI-powered chatbots for automated issue resolution and support.\n- Developing a mobile app for on-the-go access to project management tools.\n- Expanding analytics capabilities to provide more detailed insights and predictive models.\n\n### Notes:\n- When implementing new features, assess the potential impact on system performance, scalability, and overall user experience.\n- Continuously collect user feedback to iteratively refine and improve the system.\n- Develop a phased rollout plan for new features to minimize disruption and ensure maximum adoption."
}
```

#### Response:

```json
{
  "basic": [
    "User Authentication",
    "Basic Data Storage",
    "Video Call Connectivity",
    "Screen Sharing",
    "Basic Error Handling",
    "Project Creation and Management"
  ],
  "intermediate": [
    "Milestone-Based Progress Reporting",
    "Collaborative File Management",
    "User Profiling and Analytics",
    "Project Template Library",
    "Integrations with Calendar and Scheduling Tools",
    "Intelligent Task Recommendation"
  ],
  "advanced": [
    "Automated Task Estimation",
    "Machine Learning-based Task Prioritization",
    "Real-time Translation and Localization",
    "Implementing Augmented Reality (AR) Capabilities",
    "Integrating AI-powered Chatbots",
    "Developing a Mobile App",
    "Expanding Analytics Capabilities",
    "Microservices Architecture",
    "Advanced Error Handling and Logging"
  ]
}
```

---

### 🔹 3. Generate COCOMO II Parameters

**POST** `/api/tool2/cocomo2/generate-parameters`

#### Request:

```json
{
  "software": "video calling",
  "level": "basic",
  "features": [
    "User Authentication",
    "Basic Data Storage",
    "Video Call Connectivity",
    "Screen Sharing",
    "Basic Error Handling",
    "Project Creation and Management"
  ]
}
```

#### Response:

```json
{
  "function_points": {
    "fp_items": [
      {
        "fp_type": "EI",
        "det": 8,
        "ftr_or_ret": 1
      },
      {
        "fp_type": "EO",
        "det": 10,
        "ftr_or_ret": 2
      },
      {
        "fp_type": "ILF",
        "det": 18,
        "ftr_or_ret": 3
      },
      {
        "fp_type": "EIF",
        "det": 2,
        "ftr_or_ret": 1
      },
      {
        "fp_type": "EQ",
        "det": 15,
        "ftr_or_ret": 3
      },
      {
        "fp_type": "ILF",
        "det": 12,
        "ftr_or_ret": 2
      }
    ],
    "language": "Java"
  },
  "reuse": {
    "asloc": 3500,
    "dm": 20,
    "cm": 10,
    "im": 10,
    "su_rating": "L",
    "aa_rating": "2",
    "unfm_rating": "N",
    "at": 15
  },
  "revl": {
    "new_sloc": 8500,
    "adapted_esloc": 2500,
    "revl_percent": 25
  },
  "effort_schedule": {
    "sloc_ksloc": 7.5,
    "sced_rating": "L"
  }
}
```

---

### 🔹 4. Evaluate COCOMO II Effort

**POST** `/api/tool2/cocomo2_evaluation`

#### Request:

```json
{
  "function_points": {
    "fp_items": [
      {
        "fp_type": "EI",
        "det": 8,
        "ftr_or_ret": 1
      },
      {
        "fp_type": "EO",
        "det": 10,
        "ftr_or_ret": 2
      },
      {
        "fp_type": "ILF",
        "det": 18,
        "ftr_or_ret": 3
      },
      {
        "fp_type": "EIF",
        "det": 2,
        "ftr_or_ret": 1
      },
      {
        "fp_type": "EQ",
        "det": 15,
        "ftr_or_ret": 3
      },
      {
        "fp_type": "ILF",
        "det": 12,
        "ftr_or_ret": 2
      }
    ],
    "language": "Java"
  },
  "reuse": {
    "asloc": 3500,
    "dm": 20,
    "cm": 10,
    "im": 10,
    "su_rating": "L",
    "aa_rating": "2",
    "unfm_rating": "N",
    "at": 15
  },
  "revl": {
    "new_sloc": 8500,
    "adapted_esloc": 2500,
    "revl_percent": 25
  },
  "effort_schedule": {
    "sloc_ksloc": 7.5,
    "sced_rating": "L"
  }
}
```

#### Response:

```json
{
  "status": "success",
  "results": {
    "function_points": {
      "ufp": 31,
      "sloc": 1643
    },
    "reuse": null,
    "revl": {
      "sloc_total": 11000,
      "sloc_after_revl": 13750
    },
    "effort_schedule": {
      "person_months": 26.96,
      "development_time_months": 8.53,
      "avg_team_size": 3.16
    }
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
  "suggested_features": "User Authentication,Basic Data Storage,Video Call Connectivity, Screen Sharing, Basic Error Handling, Project Creation and Management",
  "suggested_tech_stack": "Python (using Flask or Django)\nNode.js (using Express.js)\nReact\nAngular\nVue.js\nMySQL\nPostgreSQL\nMongoDB\nAxios\nfetch\njQuery\nPassport.js (for Node.js)\nDjango's built-in authentication\nAsana\nTrello\nJira\nGit (with GitHub or Bitbucket)\nDocker\nKubernetes\nHeroku\nAWS Elastic Beanstalk\nWebpack\nGulp\nRollup\nTensorFlow\nPyTorch\nKeras\nscikit-learn\nD3.js\nMatplotlib\nSeaborn\nPlotly\nTableau\nPower BI\nPostgreSQL with PostgreSQL-specific extensions\nRedis\nElasticsearch\nSolr\nNext.js\nGatsby\nStorybook\nTypeScript\nESLint\nPrettier\nJest\nCypress\nMocha\nChai\nSinon\nAWS Lambda\nAzure Functions\nGoogle Cloud Functions\nApex Code\nCloudwatch\nNew Relic\nRollbar\nSentry\nCircleCI\nBamboo\nJenkins\nAnsible\nTerraform",
  "total_repos_processed": 3,
  "project_idea": "video calling",
  "preferences": ""
}
```

#### Response:

```json
{
  "folder_structure": {
    "json_structure": {
      "name": "video-calling",
      "structure": [
        {
          "type": "file",
          "name": "README.md"
        },
        {
          "type": "file",
          "name": ".gitignore"
        },
        {
          "type": "folder",
          "name": "src",
          "children": [
            {
              "type": "folder",
              "name": "python",
              "children": [
                {
                  "type": "file",
                  "name": "main.py"
                },
                {
                  "type": "folder",
                  "name": "flask",
                  "children": [
                    {
                      "type": "file",
                      "name": "app.py"
                    },
                    {
                      "type": "file",
                      "name": "models.py"
                    },
                    {
                      "type": "file",
                      "name": "routes.py"
                    }
                  ]
                },
                {
                  "type": "folder",
                  "name": "django",
                  "children": [
                    {
                      "type": "file",
                      "name": "settings.py"
                    },
                    {
                      "type": "file",
                      "name": "urls.py"
                    },
                    {
                      "type": "file",
                      "name": "wsgi.py"
                    }
                  ]
                }
              ]
            },
            {
              "type": "folder",
              "name": "node",
              "children": [
                {
                  "type": "folder",
                  "name": "express",
                  "children": [
                    {
                      "type": "file",
                      "name": "app.js"
                    },
                    {
                      "type": "file",
                      "name": "models.js"
                    },
                    {
                      "type": "file",
                      "name": "routes.js"
                    }
                  ]
                },
                {
                  "type": "folder",
                  "name": "angular",
                  "children": [
                    {
                      "type": "file",
                      "name": "app.module.ts"
                    },
                    {
                      "type": "file",
                      "name": "app.component.ts"
                    }
                  ]
                },
                {
                  "type": "folder",
                  "name": "react",
                  "children": [
                    {
                      "type": "file",
                      "name": "index.js"
                    },
                    {
                      "type": "file",
                      "name": "App.js"
                    }
                  ]
                },
                {
                  "type": "folder",
                  "name": "vue",
                  "children": [
                    {
                      "type": "file",
                      "name": "main.js"
                    },
                    {
                      "type": "file",
                      "name": "App.vue"
                    }
                  ]
                }
              ]
            },
            {
              "type": "folder",
              "name": "tests",
              "children": [
                {
                  "type": "folder",
                  "name": "python",
                  "children": [
                    {
                      "type": "file",
                      "name": "test_main.py"
                    }
                  ]
                },
                {
                  "type": "folder",
                  "name": "node",
                  "children": [
                    {
                      "type": "file",
                      "name": "test_app.js"
                    }
                  ]
                }
              ]
            },
            {
              "type": "folder",
              "name": "docs",
              "children": [
                {
                  "type": "file",
                  "name": "index.md"
                }
              ]
            }
          ]
        }
      ]
    },
    "tree_view": "video-calling/\n├── README.md\n├── .gitignore\n└── src/\n    ├── python/\n    │   ├── main.py\n    │   ├── flask/\n    │   │   ├── app.py\n    │   │   ├── models.py\n    │   │   └── routes.py\n    │   └── django/\n    │       ├── settings.py\n    │       ├── urls.py\n    │       └── wsgi.py\n    ├── node/\n    │   ├── express/\n    │   │   ├── app.js\n    │   │   ├── models.js\n    │   │   └── routes.js\n    │   ├── angular/\n    │   │   ├── app.module.ts\n    │   │   └── app.component.ts\n    │   ├── react/\n    │   │   ├── index.js\n    │   │   └── App.js\n    │   └── vue/\n    │       ├── main.js\n    │       └── App.vue\n    ├── tests/\n    │   ├── python/\n    │   │   └── test_main.py\n    │   └── node/\n    │       └── test_app.js\n    └── docs/\n        └── index.md"
  },
  "project_idea": "video calling",
  "suggested_features": "User Authentication,Basic Data Storage,Video Call Connectivity, Screen Sharing, Basic Error Handling, Project Creation and Management",
  "total_repos_processed": 3
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
  "name": "chatbottest",
  "structure": [
    {"type": "file", "name": "README.md"},
    {"type": "file", "name": ".gitignore"},
    {
      "type": "folder", "name": "src", "children": [
        {"type": "folder", "name": "main", "children": [{"type": "file", "name": "main.py"}]},
        {"type": "folder", "name": "api", "children": [{"type": "file", "name": "api.py"}]},
        {"type": "folder", "name": "models", "children": []},
        {"type": "folder", "name": "utils", "children": []},
        {"type": "folder", "name": "services", "children": []}
      ]
    },
    {
      "type": "folder", "name": "config", "children": [
        {"type": "file", "name": "config.py"},
        {"type": "file", "name": "settings.py"}
      ]
    },
    {
      "type": "folder", "name": "requirements", "children": [
        {"type": "file", "name": "requirements.txt"}
      ]
    }
  ]
}

```

#### Response:

```json
{
  "status": "success",
  "message": "Project uploaded and cleaned up successfully.",
  "repo_name": "chatbottest"
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
