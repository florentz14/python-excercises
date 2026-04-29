"""
Pie Chart Visualization Script
Displays a pie chart comparing market share of phone brands.
"""
import matplotlib.pyplot as plt


def create_pie_chart(labels, values, colors, explode=None, title='A Pie Chart',
                     figsize=(8, 6), save_path=None):
    """
    Create and display a customizable pie chart.

    Args:
        labels (list): Labels for each slice
        values (list): Values for each slice
        colors (list): Colors for each slice
        explode (list, optional): Offset values for slices
        title (str): Chart title
        figsize (tuple): Figure size (width, height)
        save_path (str, optional): Path to save the figure

    Raises:
        ValueError: If labels and values have different lengths
    """
    if len(labels) != len(values):
        raise ValueError("Labels and values must have the same length")

    # Create figure with specified size
    plt.figure(figsize=figsize)

    # Create the pie chart
    plt.pie(
        values,
        labels=labels,
        colors=colors,
        explode=explode or [0] * len(labels),
        shadow=True,
        autopct='%1.1f%%',
        startangle=180,
        textprops={'fontsize': 10, 'weight': 'bold'}
    )

    # Customize chart
    plt.title(title, fontsize=14, weight='bold', pad=20)
    plt.axis('equal')

    # Save if path provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")

    plt.show()


# Main execution
if __name__ == '__main__':
    # Data
    labels = ['Nokia', 'Samsung', 'Apple', 'Lumia']
    values = [10, 30, 45, 15]
    # Hex colors for better control
    colors = ['#FFD700', '#32CD32', '#FF4500', '#4169E1']
    explode = (0.3, 0, 0, 0)  # Explode Nokia slice

    # Create the pie chart
    create_pie_chart(
        labels=labels,
        values=values,
        colors=colors,
        explode=explode,
        title='Phone Market Share',
        figsize=(10, 7)
        # Uncomment to save: save_path='pie_chart.png'
    )
