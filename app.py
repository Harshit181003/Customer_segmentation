import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

st.set_page_config(layout="wide")
st.title("🧠 Customer Segmentation")

uploaded_file = st.file_uploader("Upload your cleaned RFM data (CSV)", type=['csv'])

if uploaded_file:
    rfm = pd.read_csv(uploaded_file)

    st.subheader("📄 Raw RFM Data")
    st.dataframe(rfm.head())

    rfm_scaled = StandardScaler().fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

    k = st.slider("Select number of clusters (K)", min_value=2, max_value=8, value=4)
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
    rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

    cluster_map = {0: 'Loyal Customers', 1: 'High Spenders', 2: 'At Risk', 3: 'New Customers'}
    rfm['Segment'] = rfm['Cluster'].map(cluster_map)

    st.subheader("📊 Customer Segment Counts")
    segment_counts = rfm['Segment'].value_counts()
    fig1, ax1 = plt.subplots()
    sns.barplot(x=segment_counts.index, y=segment_counts.values, ax=ax1)
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    st.subheader("📋 Cluster Summary")
    if 'CustomerID' not in rfm.columns and rfm.index.name == 'CustomerID':
        rfm = rfm.reset_index()

    cluster_summary = rfm.groupby('Segment').agg({
        'Recency': 'mean',
        'Frequency': 'mean',
        'Monetary': 'mean',
        'CustomerID': 'count'
    }).rename(columns={'CustomerID': 'Num_Customers'})
    st.dataframe(cluster_summary.style.format("{:.2f}"))

    st.subheader("📌 2D Scatter (Recency vs Monetary)")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Segment', palette='tab10', ax=ax2)
    st.pyplot(fig2)

    st.subheader("📌 3D RFM Cluster Visualization")
    fig3 = plt.figure(figsize=(8, 6))
    ax3 = fig3.add_subplot(111, projection='3d')
    ax3.scatter(rfm['Recency'], rfm['Frequency'], rfm['Monetary'],
                c=rfm['Cluster'], cmap='Set2', s=60)
    ax3.set_xlabel('Recency')
    ax3.set_ylabel('Frequency')
    ax3.set_zlabel('Monetary')
    st.pyplot(fig3)

    csv = rfm.to_csv(index=False).encode()
    st.download_button("📥 Download Segmented Data", data=csv, file_name="rfm_segmented.csv", mime='text/csv')

else:
    st.info("Please upload your cleaned RFM CSV file to begin.")
