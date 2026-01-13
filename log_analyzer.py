import re
import os
import argparse
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

    try:
        with open(log_file, 'r') as f:
            for line in f:
                match = log_pattern.match(line)
                if match:
                    data = match.groupdict()
                    requests_per_ip[data['ip']] += 1
                    requests_per_url[data['url']] += 1
                    status_code_counts[data['status']] += 1
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
        return None # Indicate an error by returning None

    return {
        "requests_per_ip": requests_per_ip,
        "requests_per_url": requests_per_url,
        "status_code_counts": status_code_counts,
    }

def main():
    parser = argparse.ArgumentParser(description="Analyze a log file to summarize requests.")
    parser.add_argument("log_file", help="The path to the log file to analyze.")
    args = parser.parse_args()

    results = analyze_log(args.log_file)
    if results is None:
        return # Exit if file not found or other error
def display_results(results):
    """
    Displays the log analysis results in a human-readable format.

    Args:
        results (dict): The dictionary containing the analysis results.
    """
    print("\n--- Log Analysis Results ---")

    print("\nTop 10 Requests per IP:")
    for ip, count in results["requests_per_ip"].most_common(10):
        print(f"  {ip}: {count}")

    print("\nTop 10 Requests per URL:")
    for url, count in results["requests_per_url"].most_common(10):
        print(f"  {url}: {count}")

    print("\nStatus Code Counts:")
    for status, count in sorted(results["status_code_counts"].items()):
        print(f"  {status}: {count}")

def main():
    parser = argparse.ArgumentParser(description="Analyze a log file to summarize requests.")
    parser.add_argument("log_file", help="The path to the log file to analyze.")
    args = parser.parse_args()

    results = analyze_log(args.log_file)
    if results is None:
        return # Exit if file not found or other error

    display_results(results) # Call the new display function