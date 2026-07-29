# 📊 Smart Personal Finance & Expense Tracker

An interactive, command-line personal finance and savings analyzer built with **Python**, **NumPy**, and **Matplotlib**. 

This application allows users to log monthly income and expenses across multiple months, save/load data via JSON, compute key financial metrics using vectorized matrix math, and export visual charts of their spending habits.

---

## ✨ Features

* **Interactive CLI Interface:** Prompt-driven data collection with built-in input validation for income and multi-month expenses.
* **Vectorized Financial Analytics:** High-performance matrix calculations powered by **NumPy** to calculate monthly totals, category averages, net savings, and savings rates.
* **Data Persistence (JSON):** Automatically save your financial entries to a local `expenses.json` file and reload them whenever you run the app.
* **Visual Data Insights:** Auto-generates and exports a publication-grade bar chart (`spending_chart.png`) using **Matplotlib**.
* **Smart Financial Health Report:** Automatically flags your largest spending category and calculates your average monthly savings rate.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.8+
* **Libraries:**
  * [NumPy](https://numpy.org/) — Matrix math and statistical calculations
  * [Matplotlib](https://matplotlib.org/) — Data visualization and chart generation

### Quick Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nuhamaryam/Personal-Finance-Tracker-NumPy.git
   cd Personal-Finance-Tracker-NumPy
   ```

2. **Install required dependencies:**
   ```bash
   pip install numpy matplotlib
   ```



---

## 🚀 How to Run

Execute the main script from your terminal:

```bash
python tracker.py

```

### Application Options on Launch:

1. **Load Saved Data:** Load previous entries directly from `expenses.json`.
2. **Interactive Setup:** Enter fresh data for custom income, number of months, and category expenses.
3. **Generate Visual Chart:** Optionally generate and display a Matplotlib spending breakdown chart.

---

## 📊 Generated Output Examples

### 1. Terminal Summary Report

```text
==========================================
      PERSONAL FINANCE & SAVINGS REPORT   
==========================================
Monthly Income: $3,500.00

Month 1: Spent = $2,180.00 | Saved = $1,320.00
Month 2: Spent = $2,050.00 | Saved = $1,450.00
------------------------------------------
Average Monthly Expense Breakdown:
  • Housing        : $1,200.00
  • Food           : $435.00
  • Transport      : $140.00
  • Entertainment  : $165.00
  • Utilities      : $175.00
------------------------------------------
Largest Expense Area   : Housing ($1,200.00/mo avg)
Average Monthly Savings: $1,385.00
Average Savings Rate   : 39.6%
==========================================

```

### 2. Auto-Exported Chart (`spending_chart.png`)

When prompted, the script exports a clean visualization showing your average spending per category:

> *Note: Running the app saves `spending_chart.png` directly to your project directory.*

---

## 💡 How NumPy & Python Concepts Are Applied

| Feature | Concept / Module | Technical Detail |
| --- | --- | --- |
| **Monthly Totals** | NumPy Vectorized Sum (`axis=1`) | `np.sum(self.expenses, axis=1)` |
| **Category Averages** | NumPy Column Mean (`axis=0`) | `np.mean(self.expenses, axis=0)` |
| **Top Expense Identification** | NumPy Argmax | `np.argmax(avg_spending)` |
| **Data Persistence** | Python `json` & `os` modules | Reads/writes `expenses.json` |
| **Data Visualization** | Matplotlib Pyplot | Renders bar charts with custom themes & grids |

---

## 📂 Project Structure

```text
Personal-Finance-Tracker-NumPy/
│
├── tracker.py          # Main application source code
├── expenses.json       # Auto-generated JSON database (created on first run)
├── spending_chart.png  # Auto-generated visualization chart
├── README.md           # Project documentation
└── LICENSE             # MIT License

```

---

## 📝 License

Distributed under the MIT License. Feel free to fork, adapt, or use this code for personal or educational projects!

