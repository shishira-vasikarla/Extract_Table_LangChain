
Extracting Structured Data from PDFs to Databases

By: Prof. Dr. Randy Lin, Naga Vasikarla, Aanya Goel

Project Overview:

This project automates the extraction of **financial tables** from PDF documents and integrates them directly into a structured database. Our goal is to streamline the process of **competitor market analysis** by providing clean, well-formatted, and accessible data extracted from financial reports.

Objectives:

* Automate extraction of complex financial tables from multi-page PDFs.
* Preserve structure and content fidelity during table extraction.
* Export extracted data as `.csv` files for seamless database integration.
* Support analytical use cases like competitor evaluation and market trend insights.

--

Background:

Existing Methods:

1. Manual Data Entry – Inefficient and error-prone.
2. AI Tools (e.g., ChatGPT) – Require additional preprocessing and often lack direct PDF parsing capabilities.

--

Key Limitations

* ❌ Complex layouts result in misaligned or lost data.
* 🕓 Manual formatting is slow and tedious.
* ⚠️ High risk of human error.
* 🧩 Lack of direct PDF integration in most AI tools.

--

Our Approach

We focused on extracting **financial tables** from various PDF sources using automated tools. The data is exported as `.csv` files to allow integration into relational databases for analysis and visualization.

Testing & Results

Input Files

* File 1: 146 pages, 141 tables
* File 2: 96 pages, 40 tables
* File 3: 113 pages, 60 tables

--

Evaluation Metrics

* Accuracy – Were the correct tables detected and data captured?
* Formatting– Was the structure of the original table preserved?

Selected Test Cases

| Test Case | Scenario                         | Accuracy | Formatting | Key Observations                       |
| --------- | -------------------------------- | -------- | ---------- | -------------------------------------- |
| #1        | Short, well-aligned rows/columns | 100%     | 83%        | Slight variation in one column         |
| #2        | Irregular headers                | 100%     | 68%        | Headers split across multiple columns  |
| #3        | Long sentences                   | 100%     | 66%        | Sentence splitting into multiple cells |
| #4        | Multiple tables per page         | 50%      | 53%        | Non-tabular content included           |
| #6        | Irregular headers (File 2)       | 80%      | 40%        | Captured all headers, poor format      |
| #9        | Large tables with long headers   | 95%      | 81%        | One row lost, formatting misaligned    |

Overall

* Accuracy: 84%
* Formatting: 67%
* Best performance on simple, single-table pages
* Issues with long headers and complex layouts

---

Known Challenges

* Header splitting across columns
* Misinterpretation of column boundaries
* Wrapping of long text into incorrect columns
* Identification of multiple tables on a single page

---

Future Vision

* Improve parsing for irregular headers and multi-table layouts.
* Generate **automated business reports** from extracted tables.
* Build **interactive dashboards** with:

  * Revenue trend visualizations
  * Competitor performance comparisons
  * Regional financial insights

---

Output Format

* Clean `.csv` files for each extracted table
* Ready for import into SQL/NoSQL databases
* Suitable for integration into BI tools like Power BI or Tableau

---

Example Use Cases

* Competitive market analysis
* Financial trend analysis
* Automated reporting pipelines

---

Acknowledgments

Special thanks to Prof. Dr. Randy Lin, and Aanya Goel for their contributions and insights in shaping this project.

