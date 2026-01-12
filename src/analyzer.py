import mysql.connector as connector
# DB
def get_connection():
    return connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        port=3306,
        database="expense_db"
    )
# Read operations
def fetch_transactions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""select date
                   , category
                   , amount
                   , description from transactions order by date desc""")
    rows = cursor.fetchall()
    conn.close()
    return rows
def fetch_total_expense():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select sum(amount) from transactions")
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return 0
    if isinstance(result, tuple):
        result = result[0]
    return float(result) if result is not None else ()
def fetch_expense_by_category():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT category, SUM(amount)
                   FROM transactions
                   GROUP BY category
                   """)
    rows = cursor.fetchall()
    conn.close()
    return rows
# Write operations
def add_expense(date, amount, category, description):
    conn = get_connection()
    cursor = conn.cursor()
    query = """ INSERT INTO transactions (date, amount, category, description)
    VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, (date, amount, category, description))
    conn.commit()
    conn.close()
def clear_all_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("truncate table transactions")
    conn.commit()
    conn.close()
# App control
def main_menu():
    while True:
        print("1. Add Expense")
        print("2. Show total expense")
        print("3. Show expense by category")
        print("4. Show all expenses")
        print("5. Clear all expenses")
        print("6. Exit")
        choice = input("Choose an option --> ")
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD) --> ")
            amount = float(input("Enter amount --> "))
            category = input("Enter category --> ")
            description = input("Enter description --> ")
            add_expense(date,amount,category,description)
            print("Exepense added succesfully!")
        elif choice == "2":
            print("Total expense -->",fetch_total_expense())
        elif choice == "3":
            print("\nExpense by category -->")
            print("xxxxxxxxxxxxxxxxx")
            for category, amount in fetch_expense_by_category():
                print(f"{category:<12} : {amount}")
        elif choice == "4":
            print("\nAll expenses:")
            print("xxxxxxxxxxxxxxxxx")
            print("Date     | Category      | Amount       | Description")
            print("xxxxxxxxxxxxxxxxx")
            for date, category, amount, description in fetch_transactions():
                print(f"{date} | {category:<12} | {amount:<7} | {description}")
        elif choice == "5":
            clear_all_expenses()
            print("All expenses cleared!")
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid choice... Try again")
if __name__=="__main__":
    main_menu()