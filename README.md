# AI-Powered Workout Excel Column Generator

## Overview

This script provides a Command-Line Interface (CLI) for generating new columns in an Excel file using AI. It utilizes AI models from OpenAI or Ollama to generate new column values based on existing data.

## Prerequisites

- Python 3.x
- A valid Excel file containing the column data

## Installation

### Creating a Virtual Environment (.venv) in Python

A virtual environment (`.venv`) is an isolated workspace that allows you to manage dependencies for different projects separately, avoiding conflicts between packages.
```sh
python -m venv .venv
```

On Windows (Command Prompt):
```cmd
.venv\Scripts\activate
```
On macOS/Linux:
```zsh
source .venv/bin/activate
```

### Requirements
1. Clone or download the repository containing this script.
2. Install required dependencies using pip:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables if needed using a `.env` file.

## Usage

Run the script from the command line:

```sh
python cli.py generate_column --path <file_path> --new_column <column_name> --model <model_name> --provider <provider> --column <existing_column>
```

### Arguments

| Argument       | Type   | Required | Default         | Description                                          |
| -------------- | ------ | -------- | --------------- | ---------------------------------------------------- |
| `--path`       | string | Yes      | N/A             | Path to the Excel file                               |
| `--new_column` | string | Yes      | N/A             | Name of the new column to generate                   |
| `--model`      | string | Yes      | N/A             | AI model to use for text generation                  |
| `--provider`   | string | No       | `openai`        | AI provider: `openai` or `ollama`                    |
| `--column`     | string | No       | `Exercise Name` | Name of the existing column to base AI generation on |

### Example Usage

#### Using OpenAI
```sh
python cli.py generate_column --path data.xlsx --new_column AI_Description --model gpt-4o --column Exercise Name
```

#### Using Ollama
```sh
python cli.py generate_column --path data.xlsx --new_column AI_Description --model gemma2 --provider ollama --column Exercise Name
```

## How It Works

1. Parses command-line arguments using `argparse`.
2. Calls `generate_new_column()` from `exercise_details.scripts.generate_details` with provided parameters.
3. Uses AI to generate values for the new column based on an existing column.
4. Saves the updated Excel file.

## Notes

- Ensure the specified Excel file exists before running the script.
- The AI provider must be either `openai` or `ollama`.
- The script loads environment variables using `dotenv`.
