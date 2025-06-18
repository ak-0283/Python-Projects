# 💰 Command-Line Personal Finance Tracker

A simple and effective terminal-based application to track your personal income and expenses using only Python and SQLite — no web, no GUI, just clean CLI interaction.

---

## 🧠 What It Does

This app helps you manage your daily finances by allowing you to:

- Add income or expense entries
- Categorize transactions
- View a list of all transactions
- Get a summary of total income, expenses, and balance
- Store everything locally using SQLite

Perfect for minimalists who love working in the terminal.

---

## ⚙️ Features

- 📥 Add new transactions (income or expense)
- 📋 View all past transactions in reverse-chronological order
- 📊 Get a balance summary (income, expenses, and net)
- 🗃️ Stores data in a local SQLite database (`database.db`)
- 🧪 Written entirely in Python, no external libraries required

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/ak-0283/Python-Projects

cd finance-tracker
```

### 2. Run the script

Make sure you have Python 3 installed. Then:

```bash
python finance.py
```

---

## 🛠️ Usage

You interact with the app using command-line arguments:

### ➕ Add a transaction

```bash
python finance.py add 1000 income Salary --description "June salary"
python finance.py add 200 expense Food --description "Dinner with friends"
```

### 📄 View all transactions

```bash
python finance.py view
```

### 📊 Get a summary report

```bash
python finance.py summary
```

---

## 📦 Example Output

```bash
$ python finance.py summary

💰 Income: 1000.00
💸 Expense: 200.00
📊 Balance: 800.00
```

```bash
$ python finance.py view

📋 All Transactions:
[2] Dinner with friends | 200.0 | expense | Food | 2025-06-17
[1] June salary | 1000.0 | income | Salary | 2025-06-17
```

---

## 📂 File Structure

```
finance-tracker/
├── finance.py         # Main script
├── database.db        # SQLite database (auto-generated)
```

---

## 🔒 No Internet, No API — 100% Local

This tool runs completely offline and requires **no third-party libraries or accounts**.

---

## 📌 Future Improvements

- Filter by date or category
- Export to CSV
- Daily/weekly/monthly reports
- Fancy terminal UI with `rich`

---

## 🙋‍♂️ Author

Created with ❤️ by [Abhay Kumar](https://github.com/ak-0283)

---

## 📄 License

MIT License — free to use, modify, and share.