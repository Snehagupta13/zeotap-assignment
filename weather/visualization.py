import matplotlib.pyplot as plt

def plot_daily_summary(daily_summary):
    """Create visualizations of daily weather summaries."""
    cities = [summary['city'] for summary in daily_summary]
    avg_temps = [summary['average_temp'] for summary in daily_summary]
    max_temps = [summary['max_temp'] for summary in daily_summary]
    min_temps = [summary['min_temp'] for summary in daily_summary]
    dates = [summary['date'] for summary in daily_summary]

    # Create a figure and axis
    plt.figure(figsize=(12, 6))
    
    # Plot average, max, and min temperatures
    plt.plot(dates, avg_temps, marker='o', label='Average Temperature (°C)', color='blue')
    plt.plot(dates, max_temps, marker='o', label='Maximum Temperature (°C)', color='red')
    plt.plot(dates, min_temps, marker='o', label='Minimum Temperature (°C)', color='green')
    
    # Add title and labels
    plt.title('Daily Weather Summary', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Temperature (°C)', fontsize=14)
    plt.xticks(rotation=45)
    plt.legend()
    
    # Show grid
    plt.grid()
    
    # Show the plot
    plt.tight_layout()
    plt.show()


def plot_alerts(alert_data):
    """Create visualizations for alerts triggered."""
    alert_types = [alert['type'] for alert in alert_data]
    counts = [alert['count'] for alert in alert_data]

    # Create a bar chart for alerts
    plt.figure(figsize=(8, 5))
    plt.bar(alert_types, counts, color='orange')
    
    # Add title and labels
    plt.title('Weather Alerts Triggered', fontsize=16)
    plt.xlabel('Alert Type', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    
    # Show grid
    plt.grid(axis='y')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
