import re
import os
from collections import Counter

def analyze_log(log_file):
    """
    Analyzes a log file and returns a summary.

    Args:
        log_file (str): The path to the log file.

    Returns:
        dict: A dictionary containing the analysis results.
    """
    # Regex to capture IP, timestamp, method, URL, status code, and user agent
    log_pattern = re.compile(
        r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - '
        r'\[(?P<timestamp>.+?)\] '
        r'"(?P<method>GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH) (?P<url>.+?) HTTP/1.1" '
        r'(?P<status>\d{3}) .+ '
        r'"(?P<user_agent>.+?)"'
    )

    requests_per_ip = Counter()
    requests_per_url = Counter()
    status_code_counts = Counter()

    with open(log_file, 'r') as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                requests_per_ip[data['ip']] += 1
                requests_per_url[data['url']] += 1
                status_code_counts[data['status']] += 1

    return {
        "requests_per_ip": requests_per_ip,
        "requests_per_url": requests_per_url,
        "status_code_counts": status_code_counts,
    }