
# 🧠 AI-Based Portfolio Management System

An intelligent, modular, and agent-driven portfolio management system powered by LLMs, designed to help users plan, execute, and monitor their investment portfolios efficiently.

---

## 🧩 Problem Statement

Traditional portfolio management tools are either too generic or require significant manual intervention and financial expertise. Users struggle with:

- Translating financial goals into investment policies
- Allocating assets intelligently based on risk and return profiles
- Selecting securities and constructing a diversified portfolio
- Regularly monitoring and rebalancing based on performance

There is a need for a system that can automate and personalize this entire lifecycle.

---

## ✅ Solution Overview

This project introduces a **multi-agent AI-based portfolio management system** using large language models (LLMs) and modular execution logic. The system:

1. Understands user requirements
2. Creates a custom Investment Policy Statement (IPS)
3. Executes portfolio construction via:
   - Asset Allocation
   - Security Selection
   - Portfolio Construction
4. Continuously monitors portfolio performance and generates reports
5. Recommends rebalancing when needed

---

## 🧠 Architecture

![alt text](agentic_pm\assets\image.png)
---

## 🧠 Agent Responsibilities

### 🧭 Main Agent (Orchestrator)
- Controls workflow between sub-agents
- Maintains conversation context and state
- Ensures modular interaction and task delegation

### 📝 Planning Agent
- Gathers user financial information (risk, goals, income, etc.)
- Generates Investment Policy Statement (IPS)
- Defines constraints for execution agents

### 🚀 Execution Agent
#### 📊 Asset Allocation Agent
- Determines weights for asset classes using optimization methods
- Models: Mean-Variance, Risk Parity, Black-Litterman

#### 📈 Security Selection Agent
- Filters stocks or ETFs based on rules or ML models
- Incorporates fundamentals, technicals, or quant metrics

#### 🏗️ Portfolio Construction Agent
- Final portfolio generation
- Constraint-based optimization (sector limits, diversification, etc.)

### 📉 Feedback Agent
- Tracks portfolio returns, risk, and drawdowns
- Generates performance reports
- Suggests rebalancing based on thresholds or time periods

---

## 🔧 Tech Stack

| Layer              | Technology / Tool                     |
|--------------------|----------------------------------------|
| Language Models    | LLama3.3:8b                            |
| Agent Framework    | Agno                                   |
| Data APIs          | Yahoo Finance, NSE API, Alpha Vantage  |
| ML & Optimization  | PyPortfolioOpt, Scikit-learn, CVXPY    |
| Backend API        | FastAPI                                |
| Frontend UI        | Streamlit                              |
| Database           | PostgreSQL, TimescaleDB, MongoDB       |
| Vector Store (RAG) | Milvus                                 |
| Visualization      | Plotly                                 |
| Hosting            | AWS / Docker                           |

---

## 📈 Key Features

- ✅ Personalized IPS generation using LLMs
- ✅ Modular agent-based architecture
- ✅ Intelligent asset allocation and security selection
- ✅ Dynamic portfolio construction with constraints
- ✅ Real-time performance monitoring and reporting
- ✅ Rebalancing alerts and recommendations

---

## 🚀 Future Enhancements

- 🗣️ Voice interaction and chatbot assistant
- 🧾 Tax-optimization module
- 🛡️ Risk profiling using behavioral models
- 🌍 Support for global securities and currencies
- 🧠 Reinforcement learning-based strategy tuning

---

## 🏁 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-portfolio-manager.git
cd ai-portfolio-manager
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App (Example with Streamlit)
```bash
streamlit run app.py
```

---

## 🤝 Contribution

Feel free to open issues, suggest improvements, or contribute new agent strategies.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🧑‍💻 Author

**Sumeet Maheshwari**  
AI/ML Engineer | CFA Level 1 Passed | Aspiring FinTech Innovator
---
