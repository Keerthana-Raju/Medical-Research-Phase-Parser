# Medical Text Extraction Tool

A Python-based tool designed to parse and extract structured data from complex medical text strings with irregular formatting. This project uses regular expressions to efficiently process multi-phase descriptions of medical conditions and treatments, transforming them into readable and structured outputs.

## Features

- **Phase-Based Extraction**: Extracts text up to a defined delimiter (e.g., " - ") for the initial phase.
- **Segment Parsing**: Captures and extracts each segment found between custom delimiters (e.g., after ";" and before " - ").
- **Automated Structuring**: Organizes extracted segments into a structured format, making data more readable and usable.

## Use Cases

This tool is designed to assist in automating the structuring of complex text fields, particularly useful for:
- Medical or clinical data processing.
- Parsing multi-phase or categorized data strings.
- Structuring information from delimited text fields for easy access and analysis.

## Project Structure

- **`medical_text_extractor.py`**: Main script that processes input strings, applies regular expressions, and outputs structured results.
- **Sample Input**:  
  ```plaintext
  'Phase I - PSORIASIS,Moderate to severe Graves' orbitopathy,AXIAL SPONDYLOARTHRITIS;Pre-registration - Active ankylosing spondylitis;Phase II - LUPUS NEPHRITIS,CHRONIC PLAQUE PSORIASIS,PSORIATIC ARTHRITIS;Launched - MODERATE TO SEVERE PLAQUE PSORIASIS'
