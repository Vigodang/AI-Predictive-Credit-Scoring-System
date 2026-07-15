# AI Predictive Credit Scoring System

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/PyQt6-Desktop%20Application-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost%20%7C%20LightGBM%20%7C%20Logistic-F7931E?style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-Operational%20Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Full%20Stack%20ML%20Prototype-2E7D32?style=for-the-badge)

## 📖 Executive Summary (About)

This project is a full-stack desktop credit-risk scoring system that combines machine learning, a PyQt6 banking-style interface, MySQL-backed operational workflows, and an optional Gemini-powered AI assistant. It is designed to help financial users evaluate customer default risk, compare model outputs, manage prediction history, generate reports, and support admin-level model governance from a single application.

The business problem is credit decision support: lenders need a repeatable way to estimate default probability from customer financial history while keeping predictions explainable, auditable, and operationally usable. This system extends the classic UCI credit-card default dataset into a 12-month feature format and exposes risk scoring through role-based UI workflows for administrators and end users.

The implemented ML pipeline trains **XGBoost**, **LightGBM**, and **calibrated Logistic Regression** models on a 30,000-row credit dataset with a **77.88% non-default / 22.12% default** target distribution. The application layer supports active-model selection, customer-level scoring, model comparison, dashboard/report outputs, outlier detection, clustering, authentication, and AI-assisted risk explanations.

## 🚀 Technical Highlights & Business Value

- **End-to-end ML product architecture:** Combines data preprocessing, model training, model persistence, prediction services, GUI workflows, reports, and operational logs in one deployable desktop application.
- **Credit-risk model pipeline:** Trains gradient-boosted tree models and calibrated linear baselines using a reproducible 70/15/15 train/validation/test split and AUC/accuracy evaluation.
- **Role-based risk operations:** Provides login, signup, admin/user roles, model management, dashboards, prediction screens, and report views through a modern PyQt6 UI.
- **Model governance workflow:** Tracks model metadata such as algorithm, version, AUC, accuracy, precision, recall, F1, active status, model path, training time, and model size.
- **Decision intelligence tooling:** Includes outlier detection, customer clustering, generated HTML/CSV reports, prediction history, and optional Gemini explanations for human-readable risk interpretation.

## 🛠️ Tech Stack & Skills Demonstrated

* **Languages:** Python, SQL
* **Frameworks & Libraries:** PyQt6, pandas, NumPy, scikit-learn, XGBoost, LightGBM, CatBoost, TensorFlow/Keras, imbalanced-learn, matplotlib, seaborn, bcrypt, joblib, google-generativeai
* **Databases & Storage:** MySQL, CSV datasets, JSON operational files, serialized model artifacts with joblib
* **Methodologies:** Credit Risk Modelling, Binary Classification, Gradient Boosting, Probability Calibration, Stratified Splitting, Feature Engineering, Model Registry Design, Role-Based Access Control, Outlier Detection, Customer Segmentation, AI-Assisted Explanation
* **Domain Skills:** Banking Analytics, Default Prediction, Risk Scoring, Model Governance, Financial Decision Support, Data Quality Monitoring, Explainable AI Product Design

## 🔑 Keywords & Tags

credit scoring, default prediction, credit risk analytics, machine learning, XGBoost, LightGBM, logistic regression, PyQt6, MySQL, model registry, customer risk segmentation, outlier detection, Gemini AI assistant, banking analytics, financial technology

## 🏗️ Architecture & Methodology

The repository follows a layered desktop-application architecture. The `ui/` package contains PyQt6 screens for login, signup, prediction, dashboarding, reporting, system management, model management, data quality, and AI assistant interactions. The `services/` package holds business logic for authentication, ML inference, model governance, query orchestration, data quality, and Gemini-powered explanations. The `ml/` package contains preprocessing, training, evaluation, and prediction utilities, while `models/` defines typed domain objects such as customers, users, and prediction results.

The machine learning workflow is centred on the UCI credit-card default dataset. The base dataset contains **30,000 customers and 25 columns**, while the 12-month training dataset expands the financial history into **43 columns**, including 41 model input features plus identifier/target fields. Preprocessing standardises education and marriage codes, clips repayment-status variables into valid ranges, removes direct identifiers, and prepares a clean feature matrix for model training.

Training is implemented in `ml/train_models.py`. The pipeline loads `UCI_Credit_Card_12months_OLD.csv`, creates a stratified train/validation/test split, trains XGBoost and LightGBM with class-imbalance handling, trains an elastic-net Logistic Regression pipeline with one-hot encoding and scaling, calibrates the linear model with isotonic calibration, and saves model artifacts plus evaluation arrays under `outputs/`.

At runtime, the prediction service accepts customer inputs in a fixed **41-feature schema**, applies the same cleaning rules as training, loads the selected model, and returns a structured `PredictionResult` containing the predicted default label, probability, model name, and raw context. Admin workflows can switch active models, compare model metrics, run model training, inspect data quality, and manage support/signup requests.

## 📊 Data & Model Summary

| Area | Details |
| :--- | :--- |
| Base dataset | `UCI_Credit_Card.csv`, 30,000 rows, 25 columns |
| Training dataset | `UCI_Credit_Card_12months_OLD.csv`, 30,000 rows, 43 columns |
| Target | `default.payment.next.month` |
| Target distribution | 23,364 non-defaults and 6,636 defaults |
| Input schema | 41 credit, repayment, billing, and payment-history features |
| Split strategy | Stratified 70% train, 15% validation, 15% test |
| Models | XGBoost, LightGBM, calibrated Logistic Regression; service-level support for CatBoost and RandomForest |
| Metrics | ROC-AUC, accuracy, precision, recall, F1, confusion matrices, optimal thresholds |
| Operational outputs | HTML report snapshot, latest-day prediction CSV, support/signup request JSON, chat history JSON |

## 📂 Repository Structure

```text
AI-Predictive-Credit-Scoring-System/
|-- README.md                         # Project documentation
|-- requirements.txt                  # Python dependencies
|-- UCI_Credit_Card.csv               # Original UCI credit dataset
|-- UCI_Credit_Card_12months_OLD.csv  # 12-month modelling dataset
|-- config/                           # Database and Gemini config
|-- docs/                             # Setup, architecture, services, UI docs
|-- ml/                               # Training, preprocessing, prediction
|-- models/                           # Domain data models
|-- outputs/                          # Reports, chat logs, system requests
|-- scripts/                          # Utility scripts
|-- services/                         # Auth, ML, query, AI, governance services
|-- tests/                            # Application launcher / sanity entrypoint
`-- ui/                               # PyQt6 desktop UI modules and assets
```

## ▶️ How to Reproduce

1. Clone the repository.

```bash
git clone https://github.com/Vigodang/AI-Predictive-Credit-Scoring-System.git
cd AI-Predictive-Credit-Scoring-System
```

2. Create and activate a virtual environment.

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Configure environment variables for local services.

```powershell
$env:CREDIT_DB_HOST="localhost"
$env:CREDIT_DB_PORT="3306"
$env:CREDIT_DB_USER="root"
$env:CREDIT_DB_PASSWORD="your_mysql_password"
$env:CREDIT_DB_NAME="credit_risk_db"
$env:GEMINI_API_KEY="your_optional_gemini_key"
```

4. Train baseline models.

```bash
python ml/train_models.py
```

5. Launch the desktop application.

```bash
python -m tests.main
```

The application opens a PyQt6 login flow, then routes users to prediction, dashboard, report, AI assistant, and admin/system management screens according to role.

## 🔐 Security & Configuration Notes

- Secrets should be provided through environment variables, not committed directly to source control.
- `config/database_config.py` reads database settings from `CREDIT_DB_*` environment variables with local defaults.
- `config/gemini_config.py` reads `GEMINI_API_KEY`; the AI assistant remains optional when no key is configured.
- Model files and large generated evaluation artifacts are intentionally excluded from version control through `.gitignore`.

## 📌 Project Outcome

This repository demonstrates the practical engineering bridge between predictive modelling and usable financial software. It is not just a standalone notebook: it includes a desktop application, role-aware workflows, model lifecycle management, reporting, customer analytics, data quality services, and optional AI explanations. The project is a strong portfolio example for machine learning engineering, fintech analytics, data product development, and applied AI system design.
