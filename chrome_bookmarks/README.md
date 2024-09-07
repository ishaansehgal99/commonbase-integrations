## README

### Overview

This project converts Google Chrome bookmarks into API calls. The process involves extracting bookmarks from a Chrome HTML export, saving them as a JSON file, and then uploading them to a specified endpoint via an API.

### Instructions

1. **Export Google Chrome Bookmarks:**
   - Open Chrome and go to the bookmarks manager by pressing `Ctrl+Shift+O` (Windows) or `Cmd+Shift+O` (Mac).
   - Click on the three-dot menu in the top-right corner and select "Export bookmarks".
   - Save the exported file as `bookmarks.html`.

2. **Convert Bookmarks to JSON:**
   - Run the `get_bookmarks.py` script to parse the `bookmarks.html` file and convert it into a JSON format:
     ```bash
     python get_bookmarks.py
     ```
   - This will create a `bookmarks.json` file in the same directory.

3. **Upload Bookmarks via API:**
   - Use the `upload_bookmarks.py` script to upload the bookmarks to the specified endpoint:
     ```bash
     python upload_bookmarks.py
     ```
   - Ensure to replace `<API_KEY>`, `<DB_NAME>`, and set the correct `endpoint` in `upload_bookmarks.py`.

### File Descriptions

- **get_bookmarks.py:** Converts the `bookmarks.html` file into a JSON format (`bookmarks.json`).
- **upload_bookmarks.py:** Uploads the bookmarks stored in `bookmarks.json` to the specified API endpoint.

### Prerequisites

- Python 3.x
- Required modules: `beautifulsoup4`, `requests`

### Install Dependencies

```bash
pip install beautifulsoup4 requests
```

### Notes
- Ensure your API key and database path are correctly set in upload_bookmarks.py before running.


