# 🔍 JobWatch CLI

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Click](https://img.shields.io/badge/Click-CLI-orange?style=flat-square)
![Requests](https://img.shields.io/badge/Requests-HTTP-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> A command-line tool to search, filter, and track engineering job listings from multiple sources. Built for engineers actively job hunting.

---

## 📌 Features

- 🔍 **Search jobs** by keyword, location, and job type
- 🏷️ **Filter results** by salary range, experience level, or company
- 📂 **Save listings** to a local JSON database
- 📊 **Export results** to CSV for spreadsheet analysis
- 🔔 **Track applications** — mark jobs as applied, saved, or rejected
- 🔄 **Refresh listings** automatically on a schedule

---

## 📁 Project Structure

```
jobwatch-cli/
├── jobwatch/
│   ├── __init__.py
│   ├── cli.py          # Click CLI entry points
│   ├── scraper.py      # Job listing scrapers
│   ├── storage.py      # Local database management
│   └── filters.py      # Filtering and ranking logic
├── data/
│   └── jobs.json
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

```bash
git clone https://github.com/TED-E/jobwatch-cli.git
cd jobwatch-cli
pip install -r requirements.txt

# Search for Python jobs in Addis Ababa
python -m jobwatch search --keyword "python engineer" --location "Addis Ababa"

# Save results to CSV
python -m jobwatch export --format csv --output jobs.csv
```

---

## 💻 CLI Commands

```
Usage: jobwatch [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  search    Search for job listings
  save      Save a job to your local database
  list      List all saved jobs
  apply     Mark a job as applied
  export    Export listings to CSV or JSON
  refresh   Refresh job listings from all sources
```

### Examples

```bash
# Search with filters
jobwatch search --keyword "data engineer" --location "remote" --level "junior"

# List all saved jobs
jobwatch list --status saved

# Mark a job as applied
jobwatch apply --id 42

# Export to CSV
jobwatch export --format csv
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| Click | CLI framework |
| Requests | HTTP requests |
| BeautifulSoup4 | HTML parsing |
| Rich | Terminal formatting |
| TinyDB | Local JSON database |

---

## 📄 License

MIT License © 2026 [TED-E](https://github.com/TED-E)
