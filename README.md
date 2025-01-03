# Python-Automation

## Overview

This repository is a collection of Python scripts developed as part of an internship at FOSSEE, IIT Bombay. The scripts demonstrate automation capabilities in file encryption, decryption, web scraping, and basic file conversions. The repository is designed to showcase practical Python programming and automation skills.

  

## Table of Contents

*   Requirements
*   Scripts Overview
*   PDF to DOCX Conversion
*   Web Scraping and Data Analysis
*   Encryption
*   Decryption
*   Image Conversion
*   PDF to Audio
*   Setup Instructions
*   How to Use
*   Running Individual Scripts
*   Contact

  

## Requirements

The project requires the following Python libraries:

*   `pdf2docx`
*   `requests`
*   `beautifulsoup4`
*   `matplotlib`
*   `pandas`
*   `xlsxwriter`
*   `cryptography`
*   `Pillow`
*   `pyttsx3`
*   `pdfplumber`
*   `PyPDF2`

Install all dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
  

## Scripts Overview

### PDF to DOCX Conversion

*   **File:** `pdftodoc.py`
*   **Description:** Converts a PDF file to a Word document (DOCX format) for easy editing.
*   **Libraries Used:** `pdf2docx`
*   **Usage:**
*   Update the `pdf_file` and `docx_file` variables with the desired file paths.
*   Run the script to convert the PDF to DOCX.

### Web Scraping and Data Analysis

*   **File:** `webscraping.py`
*   **Description:** Scrapes cricket match data from Cricbuzz, processes it, and generates Excel reports with data visualizations.
*   **Libraries Used:** `requests`, `BeautifulSoup`, `matplotlib`, `pandas`
*   **Usage:**
*   Modify the `cricbuzz_url` variable if needed.
*   Run the script to scrape and analyze data.

### Encryption

*   **File:** `encryption.py`
*   **Description:** Encrypts files in a folder using the Fernet symmetric encryption method.
*   **Libraries Used:** `cryptography`
*   **Usage:**
*   Update the `folder_path` variable with the folder to encrypt.
*   Run the script to encrypt files and generate an encryption key.

### Decryption

*   **File:** `decryption.py`
*   **Description:** Decrypts files in a folder encrypted using the above encryption script.
*   **Libraries Used:** `cryptography`
*   **Usage:**
*   Update the `encrypted_folder_path` and `key` variables with the folder path and key.
*   Run the script to decrypt files.

### Image Conversion

*   **File:** `imgconversion.py`
*   **Description:** Converts images to PNG format for uniformity and compatibility.
*   **Libraries Used:** `Pillow`
*   **Usage:**
*   Update the `input_file` and `output_file` variables with the file paths.
*   Run the script to convert the image.

### PDF to Audio

*   **File:** `pdftoaudio.py`
*   **Description:** Converts the text content of a PDF into audio files, making it accessible in audio format.
*   **Libraries Used:** `pyttsx3`, `pdfplumber`, `PyPDF2`
*   **Usage:**
*   Update the `file` variable with the PDF file path.
*   Run the script to generate audio files for each page of the PDF.

  

## Setup Instructions

1.  Clone the repository:

```bash
git clone https://github.com/wixx7/Python-Automation.git
cd Python-Automation
```

2.  Install dependencies:

```bash
pip install -r requirements.txt
```

3.  Ensure all necessary input files are available and correctly referenced in the scripts.

  

## How to Use

### Running Individual Scripts

Each script can be executed independently using Python. Below are general steps:

1.  Open the script file and update any required variables.
2.  Run the script in a terminal or IDE:

```bash
python <script\_name>.py
``` 

## Contact

For questions or collaboration inquiries, please contact:

*   **Name:** Sai Sathwik Matury
*   **Email:** sathwik.790@gmail.com

  

Enjoy automating with Python!
