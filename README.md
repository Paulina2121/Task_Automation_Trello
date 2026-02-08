# Trello Task Automation - VAT Checker Automation in Selenium
## Overview
This project is a **Python automation simulating a real business workflow** found in many departments in corporation world.

The automation reads tasks from a Trello board - To do List, identifies VAT verification requests (by the title of the card), downloads the card's attachment containig VAT numbers to verify and validates VAT numbers via the EU VIES website using Selenium, then saves the results back into an Excel file.

The project demonstrates **API integration (Trello), web automation (VIES), data processing (excel), and clean project structuring**.

---

## Business Use Case
In many organizations, VAT numbers must be manually verified for invoices or suppliers.  
This process is repetitive, time-consuming, and error-prone.

This automation shows how such a workflow can be handled **end-to-end** using Python:
- Task intake via Trello
- Decision logic based on task title
- Web verification via Selenium
- Automated Excel updates

---

## Features
- Reads tasks from a Trello “To Do” list
- Filters tasks titled **“VAT checker”**
- Moves unrelated tasks to another Trello list (for example Manual Handling)
- Downloads Excel files attached to Trello cards
- Validates VAT numbers using the EU VIES website
- Saves validation results back into the same Excel file
- Moves processed task either to "Done" list or "Exception" list

---

## Tech info
- Python
- Selenium
- Requests
- Pandas
- REST API (Trello)
- Excel (xlsx)
- Git & GitHub

---

## Project Structure

FinalProject/
├── main.py
├── config.py
├── exceptions.py
├── requirements.txt
├── processing/
│   ├── fetch_tasks.py
│   ├── process.py
│   └── __init__.py
├── scenarios/
│   └── scenario_vat_checker.py
├── web_scrapper/
│   ├── workflows.py
│   ├── core/
│   └── pages/
├── utils/
│   └── utility_task.py
└── README.md
