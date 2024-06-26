
# Stripe Invoice Fetcher

This Python script fetches invoice data from the Stripe API and extracts specific information into a CSV file.

## Features

- Fetches invoice data from the Stripe API
- Extracts the following fields:
  - `id`
  - `created`
  - `amount_paid`
  - `currency`
  - `invoice_pdf`
  - `number`
  - `subtotal`
  - `tax`
  - `country`
- Sorts invoices by creation date in ascending order
- Saves the extracted data to a CSV file

## Prerequisites

- Python 3.6+
- Stripe account with API keys

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/stripe-invoice-fetcher.git
   cd stripe-invoice-fetcher
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Stripe secret key:

   ```plaintext
   STRIPE_SECRET_KEY=your_stripe_secret_key
   ```

## Usage

1. Run the script to fetch invoices and save them to a CSV file:

   ```bash
   python fetch_invoices.py
   ```

2. The script will print the DataFrame of invoices to the console and save it to `invoices.csv`.

## Example

The resulting CSV file (`invoices.csv`) will look like this:

```csv
id,created,amount_paid,currency,invoice_pdf,number,subtotal,tax,country
in_1OpYlMBLRKsqtTK3BRUZ50Zs,2024-03-01 17:16:44,10,usd,https://pay.stripe.com/invoice/acct_1OcnxzBLRKsqtTK3/live_YWNjdF8xT2NueHpCTFJLc3F0VEszLF9QZXNXQWJEZ0pBY1JnMUJJenJzM1lrcFhQOFZIUkZJLDk5ODUwNjM10200nRdIx7qS/pdf?s=ap,AC1FA5E2-0002,10,1.74,ES
in_1OpWusBLRKsqtTK3kCq6xa1W,2024-03-01 15:18:26,10,usd,https://pay.stripe.com/invoice/acct_1OcnxzBLRKsqtTK3/live_YWNjdF8xT2NueHpCTFJLc3F0VEszLF9QZXFjaTI4YmI1blhsVDlFMHJaTkQ0U1FBamxpMFdBLDk5ODQ0NTA00200hJC6ETEK/pdf?s=ap,AC1FA5E2-0001,10,1.74,ES
in_1Oqd8NBLRKsqtTK3cpnHOAcZ,2024-03-04 16:08:55,10,usd,https://pay.stripe.com/invoice/acct_1OcnxzBLRKsqtTK3/live_YWNjdF8xT2NueHpCTFJLc3F0VEszLF9QZno2WHFBZHdvaTNOUVRjbXZqVmRVZlNqRHE4NHFvLDEwMDEwNTc2OA0200InB9ZwHv/pdf?s=ap,AC1FA5E2-0003,10,0,US
in_1OqvAkBLRKsqtTK3vgbSxiz2,2024-03-05 11:24:34,10,usd,https://pay.stripe.com/invoice/acct_1OcnxzBLRKsqtTK3/live_YWNjdF8xT2NueHpCTFJLc3F0VEszLF9QZ0hrVzk3ampsTHk2Tjh0UHdBUnRiYks1Nk53VEZmLDEwMDE3NTA5OA0200aI5Z7CuS/pdf?s=ap,AC1FA5E2-0004,10,1.87,PT
in_1OqwpsBLRKsqtTK3s3QIDVCw,2024-03-05 13:11:08,10,usd,https://pay.stripe.com/invoice/acct_1OcnxzBLRKsqtTK3/live_YWNjdF8xT2NueHpCTFJLc3F0VEszLF9QZ0pTMlh2Rk5SeDBqTVRHaHZ1d1dhbXhGTWMzOGw0LDEwMDE4MTQ5Mw0200WBPYIOQi/pdf?s=ap,AC1FA5E2-0005,10,1.87,PT
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

- [Stripe API](https://stripe.com/docs/api)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
