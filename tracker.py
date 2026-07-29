import numpy as np
import json
import os
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self):
        self.categories = np.array(["Housing", "Food", "Transport", "Entertainment", "Utilities"])
        self.income = 0.0
        self.expenses = None

    def collect_user_data(self):
        """Asks the user to input income and expenses interactively."""
        print("==========================================")
        print("       PERSONAL FINANCE INPUT SETUP       ")
        print("==========================================")
        
        # 1. Income Input
        while True:
            try:
                self.income = float(input("Enter your fixed Monthly Income ($): "))
                if self.income <= 0:
                    print("Please enter a positive income amount.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # 2. Months Input
        while True:
            try:
                num_months = int(input("How many months of expense data do you want to analyze? "))
                if num_months <= 0:
                    print("Please enter at least 1 month.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        # 3. Expenses Matrix
        expense_list = []
        for m in range(num_months):
            print(f"\n--- Month {m + 1} Expenses ---")
            month_data = []
            for cat in self.categories:
                while True:
                    try:
                        val = float(input(f"  Enter amount spent on '{cat}' ($): "))
                        if val < 0:
                            print("Expenses cannot be negative.")
                            continue
                        month_data.append(val)
                        break
                    except ValueError:
                        print("Invalid number. Please try again.")
            expense_list.append(month_data)

        self.expenses = np.array(expense_list)

    def save_data(self, filename="expenses.json"):
        """Saves current financial data to a JSON file."""
        data = {
            "income": self.income,
            "categories": self.categories.tolist(),
            "expenses": self.expenses.tolist()
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"\n[✓] Data successfully saved to '{filename}'!")

    def load_data(self, filename="expenses.json"):
        """Loads financial data from a saved JSON file."""
        if not os.path.exists(filename):
            print(f"\n[!] No saved file found named '{filename}'.")
            return False
        
        with open(filename, "r") as f:
            data = json.load(f)
        
        self.income = data["income"]
        self.categories = np.array(data["categories"])
        self.expenses = np.array(data["expenses"])
        print(f"\n[✓] Data successfully loaded from '{filename}'!")
        return True

    def total_monthly_expenses(self):
        return np.sum(self.expenses, axis=1)

    def average_category_spending(self):
        return np.mean(self.expenses, axis=0)

    def monthly_savings(self):
        return self.income - self.total_monthly_expenses()

    def plot_expense_breakdown(self):
        """Generates and saves a clean chart of expense distribution."""
        avg_spending = self.average_category_spending()
        
        plt.figure(figsize=(8, 5))
        plt.bar(self.categories, avg_spending, color=['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B3'])
        plt.title('Average Monthly Expense Breakdown', fontsize=14, fontweight='bold')
        plt.xlabel('Categories', fontsize=12)
        plt.ylabel('Amount Spent ($)', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        chart_filename = "spending_chart.png"
        plt.savefig(chart_filename)
        print(f"[✓] Visual chart saved as '{chart_filename}'!")
        plt.show()

    def generate_report(self):
        """Prints a structured summary report."""
        if self.expenses is None:
            print("No expense data found.")
            return

        print("\n==========================================")
        print("      PERSONAL FINANCE & SAVINGS REPORT   ")
        print("==========================================")
        print(f"Monthly Income: ${self.income:,.2f}\n")

        totals = self.total_monthly_expenses()
        savings = self.monthly_savings()
        
        for month_num, (tot, sav) in enumerate(zip(totals, savings), 1):
            print(f"Month {month_num}: Spent = ${tot:,.2f} | Saved = ${sav:,.2f}")

        print("------------------------------------------")
        print("Average Monthly Expense Breakdown:")
        avg_category = self.average_category_spending()
        for cat, avg in zip(self.categories, avg_category):
            print(f"  • {cat:15s}: ${avg:,.2f}")

        print("------------------------------------------")
        top_idx = np.argmax(avg_category)
        avg_savings = np.mean(savings)
        savings_rate = (avg_savings / self.income) * 100

        print(f"Largest Expense Area   : {self.categories[top_idx]} (${avg_category[top_idx]:,.2f}/mo avg)")
        print(f"Average Monthly Savings: ${avg_savings:,.2f}")
        print(f"Average Savings Rate   : {savings_rate:.1f}%")
        print("==========================================")

# --- Interactive Main Menu ---
if __name__ == "__main__":
    tracker = FinanceTracker()
    
    print("Welcome to Smart Finance Tracker!")
    choice = input("Do you want to load existing saved data? (y/n): ").strip().lower()
    
    loaded = False
    if choice == 'y':
        loaded = tracker.load_data()
        
    if not loaded:
        tracker.collect_user_data()
        tracker.save_data()

    tracker.generate_report()
    
    plot_choice = input("\nGenerate spending chart image? (y/n): ").strip().lower()
    if plot_choice == 'y':
        tracker.plot_expense_breakdown()