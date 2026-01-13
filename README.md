# Log Analyzer Project

This project is a Python-based tool designed for analyzing log files. Its primary goal is to process log data, extract meaningful insights, and potentially visualize patterns or anomalies.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/log_analyzer_project.git
    cd log_analyzer_project
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Note: A `requirements.txt` file needs to be created or generated based on project dependencies.)

## Usage

To use the log analyzer, run the `log_analyzer.py` script with the path to your log file as an argument.

```bash
python log_analyzer.py <path_to_your_log_file>
```

Example:
```bash
python log_analyzer.py /var/log/apache2/access.log
```

## Project Status and Future Enhancements

The log analyzer is now a functional command-line tool.

**Current Features:**
*   Parses common web server log formats (Apache/Nginx access logs).
*   Counts requests per IP address, URL, and HTTP status code.
*   Handles `FileNotFoundError` gracefully.
*   Presents results in a human-readable format, showing top 10 IPs and URLs.

**Known Limitations / Future Enhancements:**
*   **Log Format Flexibility:** Currently, the tool assumes a specific log format. Future versions could allow custom log formats via configuration.
*   **Advanced Filtering:** Implement options to filter logs by date range, IP address, URL patterns, or status codes.
*   **Output Options:** Add support for different output formats (e.g., CSV, JSON) or direct output to a file.
*   **Performance Optimization:** For very large log files, consider optimizations for faster processing.
*   **Visualization:** Integrate with libraries to generate graphs or charts of the analysis data.