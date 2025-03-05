# SECDown

**SECDown** is a Python library designed to facilitate the downloading and management of financial datasets from the U.S. Securities and Exchange Commission (SEC). It streamlines the process of accessing and organizing SEC filings for analysis and research purposes.

## Features

- **Automated Downloads**: Retrieve historical SEC filings efficiently.
- **User Identification**: Comply with SEC's fair access policies by setting a user identity.

## Installation

Clone the repository:

```bash
git clone https://github.com/orr21/secdown.git
cd secdown
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Here's a basic example of how to use SECDown:

```python
from secdown.downloader import SECDatasetDownloader

# Initialize the downloader
downloader = SECDatasetDownloader()

# Set your email to identify yourself to the SEC
downloader.set_identity('your.email@example.com')

# Download all available historical data to the 'data' directory
downloader.get_historical_data(base_folder='data')
```

This script initializes the downloader, sets the user identity, and downloads all available historical data to the specified directory.

## Contributing

We welcome contributions to enhance SECDown. Please follow these steps:

1. Fork the repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:  
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push to the branch:  
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request detailing your changes.

---
*Note: Ensure compliance with the SEC's [fair access policy]([https://www.sec.gov/os/webmaster-faq#code-support](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data)) when using this library.*
