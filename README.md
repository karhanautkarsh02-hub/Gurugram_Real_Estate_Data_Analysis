# Gurugram Real Estate Data Analysis & Insights

An Exploratory Data Analysis (EDA) project analyzing residential property listings in Gurugram to uncover price distribution, locality trends, and key business insights for buyers, investors, and developers.

---

## 📌 Project Overview
The primary goal of this project is to transform raw property listings into actionable real estate market intelligence. By cleaning messy listing data and applying exploratory data analysis techniques, we answer critical business questions regarding property valuation, location pricing, and structural impacts on cost.

---

## 🛠️ Tech Stack & Skills
- **Language:** Python 3.11
- **Libraries:** Pandas, Matplotlib, Seaborn
- **Domain:** Real Estate Analytics, Exploratory Data Analysis (EDA), Data Wrangling

---

## 🧹 Data Cleaning & Preparation
- **Standardization:** Column headers cleaned and updated to `lower_snake_case`.
- **Deduplication:** Removed duplicate records across property listings.
- **Data Transformation:** 
  - Converted `price`, `area`, and `rate_per_sqft` into clean numeric formats for aggregation.
  - Trimmed categorical attributes (`status`, `rera_approval`, `flat_type`).
  - Standardized `rera_approval` values into Boolean formats for statistical comparison.

---

## 💡 Key Business Questions & Findings

1. **Costliest Property Identified:** 
   - An **apartment located in Sector 42** with a valuation of **₹12.26 Cr (122,630,000)**.
2. **Top Locality by Average Price:** 
   - **Baliawas** holds the highest overall average listing price across the dataset.
3. **Top Micro-Market by Rate/Sqft:** 
   - **Sector 42** commands the highest rate per square foot in the region.
4. **Ready-to-Move vs. Under Construction:** 
   - Ready-to-move properties command a clear price premium over under-construction listings.
5. **RERA Approval Premium:** 
   - RERA approval alone does not guarantee a higher price per sqft; pricing is primarily driven by location and builder reputation.
6. **Property Type Impact:** 
   - **Villas** are the most expensive property type on a per square foot basis.
7. **Premium Builders:** 
   - Developers like *Camelliaass*, *Tulip*, and *Magnoliaass* consistently charge higher-than-average rates per square foot.
8. **Data Anomaly Detected:** 
   - Identified an abnormal **114 BHK** configuration entry during aggregation—flagged as a data entry outlier for domain validation.

---

## 📊 Visual Insights

### 1. Area vs Price Distribution
*Observation: Prices generally scale with total area, with strong concentration in standard layouts alongside distinct high-value luxury outliers.*

### 2. Area vs Rate per Square Foot
*Observation: Larger homes do not necessarily mean higher rate per sqft. Sharp spikes in per-sqft price occur in exclusive micro-markets.*

---

## 📁 Repository Structure
```
├── main.py                                    # Core Python script with cleaning & analysis pipelines
├── data.csv                                   # Dataset file
├── Gurgaon_Real_Estate_Analysis_Case_Study.pdf # Detailed portfolio presentation
└── README.md                                  # Project documentation
```

---

## 👨‍💻 Author
**Utkarsh Karhana**  
*Data Analyst*  
- ✉️ Email: karhanautkarsh02@gmail.com  
- 🔗 LinkedIn: 
www.linkedin.com/in/utkarsh-karhana-24414b384
