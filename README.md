# Electric Vehicle Population & Market Analysis

An interactive data analytics dashboard built with **Python, Pandas, Plotly, and Streamlit** to analyze electric vehicle registrations in Washington State.

The dashboard explores EV adoption trends, manufacturers, Tesla's market share, vehicle models, electric range, vehicle types, and geographic distribution across cities.

---

## Project Overview

This project analyzes electric vehicle registration data to identify patterns and trends in the EV market.

The dashboard provides an interactive experience that allows users to explore the data based on:

- Model Year
- Electric Vehicle Type
- Manufacturer
- County

The analysis also focuses on **Tesla's position within the electric vehicle market** and compares it with other manufacturers.

---

## Objectives

The main objectives of this project are to:

- Analyze electric vehicle registrations across different model years.
- Compare Tesla with other EV manufacturers.
- Identify the most common EV manufacturers and models.
- Analyze the distribution of fully electric and plug-in hybrid vehicles.
- Compare average electric range across manufacturers.
- Identify cities with the highest number of registered EVs.
- Analyze Tesla model distribution and trends over the years.
- Build an interactive dashboard for data exploration and visualization.

---

## Tools & Technologies

- **Python**
- **Pandas** – Data cleaning and analysis
- **Plotly Express** – Interactive data visualization
- **Streamlit** – Interactive dashboard development
- **CSV** – Data source and filtered data export

---

## Data Cleaning & Preparation

The dataset was prepared and cleaned using Pandas.

The main data preparation steps include:

- Removing duplicate records.
- Handling missing values in important fields.
- Standardizing manufacturer and model names.
- Treating zero electric-range values as unavailable values.
- Converting electric vehicle types into user-friendly labels.
- Excluding the incomplete latest model year from the analysis.
- Creating a custom grouping to compare **Tesla vs. Other Manufacturers**.

---

## Interactive Filters

The dashboard allows users to dynamically filter the analysis by:

- Model Year
- Electric Vehicle Type
- Manufacturer
- County

All KPIs and visualizations update based on the selected filters.

---

## Dashboard Sections

### 1. Overview

The Overview section provides a high-level view of the EV market.

It includes:

- Total number of registered EVs
- Tesla market share
- Percentage of fully electric vehicles
- Average electric range
- Top 10 manufacturers
- Tesla vs. other manufacturers by year
- Electric vehicle type distribution
- Average electric range by manufacturer

---

### 2. Tesla Analysis

The Tesla section provides a focused analysis of Tesla vehicles.

It includes:

- Total Tesla registrations
- Most common Tesla model
- City with the highest Tesla registrations
- Tesla model distribution
- Tesla model trends across manufacturing years

---

### 3. City Analysis

The Cities section explores the geographic distribution of EV registrations.

Users can:

- Identify cities with the highest number of registered EVs.
- Select the number of cities displayed.
- Compare EV registrations across different cities.

---

### 4. Filtered Data

The Data section provides access to the records after applying the selected filters.

Users can:

- View the filtered dataset.
- Explore individual vehicle records.
- Download the filtered data as a CSV file.

---

## Key Dashboard Metrics

The dashboard currently displays the following metrics based on the default filter selection:

| Metric | Value |
|---|---:|
| Total EV Records | 133,876 |
| Tesla Share | 46.1% |
| Fully Electric Vehicles | 77% |
| Average Electric Range | 130 miles |
| Analysis Period | 2012–2023 |

> These values are based on the dashboard's default filter selection and may change when filters are applied.

---

## Analytical Questions

The project explores several analytical questions, including:

1. How have electric vehicle registrations changed over the years?
2. How does Tesla compare with other EV manufacturers?
3. Which manufacturers have the highest number of registered EVs?
4. Which Tesla models are the most common?
5. How does electric range vary across manufacturers?
6. Which cities have the highest number of EV registrations?
7. What proportion of registered vehicles are fully electric compared with plug-in hybrids?

---

## Project Structure

```text
Electric-Vehicle-Analysis/
│
├── ev_dashboard_v2.py
├── Electric_Vehicle_Population_Data.csv
└── README.md
```

---

## Dataset

**Dataset:** Electric Vehicle Population Data

**Source:** Kaggle – Electric Vehicle Population Data

[View Dataset on Kaggle](https://www.kaggle.com/datasets/rajkumarpandey02/electric-vehicle-population-data)

---

## Author

**Razan Albishri**

Computer Science Graduate | Data Analytics & AI

[LinkedIn](https://www.linkedin.com/in/razan-albishri)

[Portfolio](https://heyzine.com/flip-book/eb4c80790d.html#page/1)