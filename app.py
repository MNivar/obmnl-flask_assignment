# Import libraries
from flask import Flask , request, url_for, redirect, render_template
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
#Read operation
@app.route("/")
def get_transactions():
    total_balance = calculate_total_balance()  # Calculate total balance
    return render_template('transactions.html', transactions=transactions, balance=total_balance)

def calculate_total_balance():
    total = 0
    for transaction in transactions:
        total += transaction["amount"]
    return total
# Create operation
@app.route("/add", methods = ["GET", "POST"])
def add_transaction():   
    if request.method == "POST":
        transaction = {
        'date': request.form['date'],
        'amount' : request.form['amount'],
        'id' : len(transactions) + 1
        }

        transactions.append(transaction)

        return redirect(url_for("get_transactions"))

    return render_template('form.html')



# Update operation
@app.route("/edit/<int:transaction_id>", methods = ['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == "POST":
            # Extract the updated values from the form fields
        date = request.form['date']
        amount = float(request.form['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
             # Redirect to the transactions list page
        return redirect(url_for("get_transactions"))

    # Find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)


# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    return redirect(url_for("get_transactions"))

# Search Operation

@app.route("/search", methods = ["GET", "POST"])
def search():
    if request.method == "POST":
        min_amount = float(request.form['min_amount'])
        max_amount = float(request.form['max_amount'])
        filtered_transactions = []
        for transaction in transactions:
            if (transaction["amount"] > min_amount) and (transaction["amount"] < max_amount):
                filtered_transactions.append(transaction)
                return render_template('transactions.html',transactions= filtered_transactions)
    return render_template('search.html')
# Total Balance

@app.route("/balance")
def total_balance():
    total_balance = calculate_total_balance() 
    # for transaction in transactions:
    #     sum  += transaction["amount"]
    return render_template('transactions.html',balance = total_balance)

    
    
                
                
                
            

    


# Run the Flask app

if __name__ == "__main__":
    app.run(debug=True)

    
