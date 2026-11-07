# National Security Intelligence

### Global Conflict Analytics & Strategic Intelligence Platform
🌐 **Live Dashboard:** https://emigdioluque.github.io/National-Security-Intelligence/

National Security Intelligence is an independent, open-source intelligence (OSINT) analytics project designed to explore historical patterns of organized violence and geopolitical conflict through real-world data.

The platform transforms conflict event records into an interactive intelligence dashboard, allowing users to analyze geographical distributions, historical trends, country-level activity and comparative indicators.

Built using the Uppsala Conflict Data Program (UCDP) Georeferenced Event Dataset, the project examines recorded conflict events between 2015 and 2025.

## 1. Project Objectives

The project was developed to demonstrate how data analytics, programming and interactive visualization can support evidence-based analysis of complex international security issues.

Its main objectives are to:

* Explore historical patterns of organized violence using publicly available conflict data.
* Identify geographical concentrations of recorded conflict events.
* Analyze how recorded conflict activity changes over time.
* Compare historical activity patterns between countries.
* Develop transparent analytical indicators to support exploratory strategic assessments.
* Communicate complex information through an accessible, interactive dashboard.

## 2. Dataset

Source: Uppsala Conflict Data Program (UCDP)
Dataset: Georeferenced Event Dataset (GED), version 26.1
Analysis period: 2015–2025
Recorded events analyzed: 216,383
Countries represented: 101

The analysis uses historical event records rather than real-time intelligence feeds.

Event counts describe the number of records included in the selected dataset and should not be interpreted as direct measures of conflict severity, national security risk or the overall level of violence in a country.

## 3. Core Features

### Global Conflict Dashboard

* Overview of recorded conflict events between 2015 and 2025.
* Summary indicators covering total events, countries analyzed and latest-year activity.
* Identification of countries with the highest recorded event counts.
* Interactive visualizations of historical conflict trends.

### Geospatial Conflict Analysis

* Interactive geographical visualization of conflict events using Leaflet.
* Exploration of recorded events through geographical filters.
* Country-level geographical analysis based on UCDP event locations.

### Country Intelligence Profiles

* Individual country selection and historical activity analysis.
* Identification of historical peaks in recorded conflict activity.
* Analysis of conflict activity persistence across the observation period.
* Measurement of historical event concentration.
* Interpretation of recorded activity levels using project-defined analytical indicators.

### Comparative Intelligence Assessment

* Historical comparison of two selected countries.
* Visualization of annual conflict event trends.
* Comparison of total recorded events and historical activity persistence.
* Analysis of annual percentage changes.
* Identification of historical activity surges using predefined analytical thresholds.
* Automated comparative interpretations and methodological warnings.

### Analytical Transparency

The platform distinguishes between recorded conflict activity and broader security conditions.

Its analytical indicators are intended to support historical exploration and comparative analysis, rather than predict future conflicts or provide official national security risk assessments.

## 4. Technologies & Tools

The platform combines data processing, analytical programming and interactive web development.

### Data Analysis & Processing

**Python**

* Data processing and analytical workflow development.
* Automated generation of structured datasets for the dashboard.

**Pandas**

* Filtering and aggregation of UCDP conflict event records.
* Country-level and annual event analysis.
* Preparation of historical indicators and exportable data.

**Matplotlib**

* Exploratory data visualization during the analytical development process.

### Frontend Development

**JavaScript**

* Implementation of interactive dashboard functionality.
* Dynamic country selection and comparative analysis.
* Calculation and presentation of historical intelligence indicators.

**HTML5**

* Structure and organization of the web dashboard.

**CSS3**

* Responsive layouts, visual styling and dashboard interface design.

### Data Visualization & Mapping

**Chart.js**

* Interactive charts displaying historical conflict trends and country comparisons.

**Leaflet.js**

* Interactive geographical visualization of georeferenced conflict events.

**OpenStreetMap**

* Geographical base maps used in the interactive mapping interface.

### Development Environment

**Visual Studio Code**

* Code development and project organization.

**GitHub**

* Version control, source code hosting and project documentation.
* Public deployment of the interactive dashboard using GitHub Pages.

## 5. Analytical Methodology

The analytical workflow follows four main stages:

### Data Preparation

Historical conflict event records are processed using Python and Pandas.

The dataset is filtered to cover the 2015–2025 period, and event counts are aggregated by country and year.

### Historical Activity Analysis

The platform calculates several descriptive indicators:

- **Total Recorded Events:** Number of conflict events recorded during the selected period.
- **Historical Activity Persistence:** Proportion of years with at least one recorded conflict event.
- **Historical Activity Concentration:** Percentage of a country's recorded events occurring in its highest-activity year.
- **Annual Percentage Change:** Relative variation in recorded events between consecutive years when the baseline is greater than zero.

### Historical Activity Surge Detection

The platform identifies historical increases in recorded conflict activity using two project-defined conditions:

- The number of recorded events increases by at least 100% compared with the previous year.
- The absolute increase is at least 20 additional recorded events.

Both conditions must be satisfied.

These thresholds are exploratory analytical criteria developed for this project. They do not represent official UCDP classifications or security alerts.

### Comparative Analysis

Users can compare two countries across the same observation period.

The platform generates descriptive interpretations based on differences in recorded activity, persistence, concentration and annual trends.

## 6. Limitations & Responsible Interpretation

This project is intended for historical analysis and educational exploration.

### Important Limitations

- **Historical Data:** The platform uses historical data and does not provide real-time conflict monitoring.
- **Event Counts:** Recorded event counts are not direct measures of conflict severity or national security risk.
- **Country Comparability:** Countries with different populations, geographical sizes or reporting conditions may not be directly comparable.
- **Zero Recorded Events:** A year with zero recorded events in the selected dataset does not necessarily indicate an absence of violence.
- **Percentage Changes:** Percentage changes can be misleading when calculated from small event counts.
- **Predictive Limitations:** Historical patterns should not be interpreted as predictions of future conflicts.
- **Independent Indicators:** The analytical indicators and interpretations are independently developed and are not official UCDP assessments.

### Project Disclaimer

The platform is an independent portfolio project and is not affiliated with any government intelligence agency.

## 7. Project Structure

The project is organized into the following directories:

```text
National-Security-Intelligence/
├── backend/
│   ├── analyze_conflicts.py
│   ├── export_dashboard.py
│   └── export_map.py
├── data/
│   ├── dashboard_data.json
│   ├── map_data.json
│   └── map_statistics.json
├── docs/
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── notebooks/
└── README.md
```

The backend processes historical conflict records and generates structured JSON files consumed by the frontend.

## 8. Running the Project Locally

### Requirements

- Python 3
- A modern web browser
- Python dependencies: Pandas and Matplotlib for the analytical workflow

### Launching the Dashboard

1. Download or clone the repository.
2. Open a terminal in the project's root directory.
3. Start a local HTTP server:

```bash
python3 -m http.server 8000
```

4. Open the following address in your browser:

```text
http://localhost:8000/frontend/
```

The dashboard requires its generated JSON files to be available in the `data/` directory.

### Data Processing

The Python scripts in `backend/` are used to process the source dataset and generate analytical outputs.

The dashboard uses preprocessed JSON files rather than querying UCDP directly from the browser.

## 9. Data Sources & References

### Primary Data Source

**Uppsala Conflict Data Program (UCDP)**

- Dataset: UCDP Georeferenced Event Dataset (GED)
- Version: 26.1
- Analysis period: 2015–2025

Official resources:

- UCDP website: https://ucdp.uu.se/
- UCDP downloads: https://ucdp.uu.se/downloads/
- UCDP GED documentation: https://ucdp.uu.se/downloads/ged/ged261.pdf

### Mapping & Visualization Resources

- Leaflet: https://leafletjs.com/
- OpenStreetMap: https://www.openstreetmap.org/

## 10. Project Status

**Version:** 1.0 — Public Portfolio Release

**Status:** Completed — Initial Public Release

National Security Intelligence is an independent, open-source intelligence (OSINT) analytics project developed to explore historical patterns of organized violence using publicly available conflict data.

The platform includes interactive dashboards, geospatial visualization, country-level historical analysis, comparative intelligence assessments, and historical activity surge detection.

The current release analyzes UCDP GED 26.1 data covering 2015–2025.

**Important:** This platform provides historical data analysis. It is not a real-time conflict monitoring system, a security risk prediction tool, or an official intelligence product.

Future improvements may include additional open-source datasets, advanced statistical methods, and expanded geographical comparisons.