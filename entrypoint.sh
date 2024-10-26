#!/bin/bash
# Function to convert shorthand intervals to cron syntax
interval_to_cron() {
    case "$1" in
        10m) echo "*/10 * * * *" ;;
        30m) echo "*/30 * * * *" ;;
        1h) echo "0 * * * *" ;;
        1d) echo "0 0 * * *" ;;
        1w) echo "0 0 * * 0" ;;
        *) echo "*/5 * * * *" ;;  # Default to every 5 minutes
    esac
}

# Default interval if not provided
: "${INTERVAL:=5m}"
# Convert interval to cron syntax
CRON_SCHEDULE=$(interval_to_cron "$INTERVAL")

# Write out current cron jobs
echo "$CRON_SCHEDULE root python /app/process_subtitles.py /app/subtitles /app/remove_lines.txt /app/log/processed_files.log" > 
chmod 0644 /etc/cron.d/container_cronjob
crontab /etc/cron.d/container_cronjob

cron
tail -f /app/log/processed_files.log
