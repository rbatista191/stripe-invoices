import stripe
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your Stripe secret key
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


# Function to fetch invoices and extract required information
def fetch_invoices():
    invoices = stripe.Invoice.list()
    data = []
    for invoice in invoices.auto_paging_iter():
        invoice_data = {
            "id": invoice.id,
            "created": datetime.fromtimestamp(invoice.created).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "amount_paid": invoice.amount_paid / 100,  # Stripe amounts are in cents
            "currency": invoice.currency,
            "invoice_pdf": invoice.invoice_pdf,
            "number": invoice.number,
            "subtotal": invoice.subtotal / 100,  # Stripe amounts are in cents
            "tax": (invoice.tax if invoice.tax is not None else 0)
            / 100,  # Stripe amounts are in cents
            "country": (
                invoice.customer_address["country"]
                if invoice.customer_address
                else "N/A"
            ),
        }
        data.append(invoice_data)

    # Convert data to a DataFrame
    df = pd.DataFrame(data)
    # Sort by created date in ascending order
    df["created"] = pd.to_datetime(df["created"])
    df = df.sort_values(by="created", ascending=True)
    return df


# Fetch the invoice data
invoice_df = fetch_invoices()

# Display the DataFrame
print(invoice_df)

# Optionally, save the DataFrame to a CSV file
invoice_df.to_csv("invoices.csv", index=False)
