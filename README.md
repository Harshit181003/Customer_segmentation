🧠 RFM Customer Segmentation with KMeans

This project performs customer segmentation using RFM analysis (Recency, Frequency, Monetary) and KMeans clustering, based on retail transaction data. The goal is to identify valuable customer segments (e.g., Loyal, High Spenders, At Risk) to support targeted marketing strategies.

---

📊 Project Overview

- Objective: Segment customers based on their purchasing behavior.
- Data Source: Retail transactional dataset containing order details, customer IDs, timestamps, and product info.
- Tech Stack: Python, Pandas, Scikit-learn, Streamlit

---

🚀 Features

- 📌 Calculate RFM metrics from raw transactions
- 📌 Apply KMeans clustering on scaled RFM data
- 📌 Assign interpretable segment labels (e.g., Loyal, At Risk)
- 📌 View customer profiles and segment summaries
- 📌 Export segmented data to CSV
- 📌 Visualize RFM distributions and clusters (in Streamlit )

---

📁 Files in this Repo

| File/Folder                | Description                                           |
|----------------------------|-------------------------------------------------------|
| `rfm_cleaned_segmented.csv`| Final RFM data with clusters and segment labels       |
| `app.py`                   | Streamlit app to interactively view segments & profiles |
| `Online_Retail.xlsx`    | Raw transaction data (InvoiceNo, CustomerID, etc.)    |
| `README.md`                | You're reading it 🙂                                   |

---

## 💡 How to Use

### 🛠  Run RFM App with Streamlit

```bash
streamlit run app.py
