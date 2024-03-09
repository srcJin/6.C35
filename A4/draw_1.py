import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def create_hierarchy_chart():
    # Define the hierarchy levels and positions
    hierarchy_levels = {
        'Higher Level Positions': ['Chief of Department'],
        'Mid Level Positions': ['Detective'],
        'Lower Level Positions': ['Police Officer', 'Probationary Police Officer', 'Recruit Officer', 'Cadet'],
        'First-Line Supervisors': ['Lieutenant and Sergeants'],
        'Company Officers': ['Captain'],
        'Field Officers': ['Deputy Inspector']
    }

    # Define the connections between positions
    connections = {
        'Chief of Department': ['Bureau Chief, Supervising Chief, Surgeon', 'Assistant Chief Chaplain, Assistant Chief, Assistant Chief Surgeon', 'Deputy Chief, Deputy Chief Chaplain, Deputy Chief Surgeon', 'Inspector, Chaplain, Police Surgeon'],
        'Detective': [],
        'Police Officer': ['Detective'],
        'Probationary Police Officer': ['Police Officer'],
        'Recruit Officer': ['Police Officer'],
        'Cadet': ['Probationary Police Officer', 'Recruit Officer'],
        'Lieutenant and Sergeants': ['Police Officer'],
        'Captain': ['Lieutenant and Sergeants'],
        'Deputy Inspector': ['Captain']
    }

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hide axes
    ax.axis('off')

    # Set a style
    plt.style.use('ggplot')

    # Create a scatter plot to define the positions of the hierarchy levels
    # Using scatter plot is a trick to keep positions even though they are not used directly
    y_positions = list(range(len(hierarchy_levels), 0, -1))  # Reverse the order for display
    x_positions = [2] * len(hierarchy_levels)
    ax.scatter(x_positions, y_positions)

    # Annotate the positions with the text
    for y, (level, positions) in zip(y_positions, hierarchy_levels.items()):
        for position in positions:
            ax.text(2, y, position, ha='center', va='center', fontsize=12)
            sub_positions = connections.get(position, [])
            if sub_positions:
                sub_y = y - 1
                for sub_position in sub_positions:
                    ax.text(2, sub_y, sub_position, ha='center', va='center', fontsize=9)
                    sub_y -= 0.5

    # Add lines to show the connections between levels
    for level, positions in hierarchy_levels.items():
        y = y_positions[len(y_positions) - list(hierarchy_levels.keys()).index(level) - 1]
        sub_positions = connections.get(positions[0], [])
        for sub_position in sub_positions:
            # Calculate the y position for sub_positions with respect to the number of items in between
            sub_y = y - 1 - 0.5 * (sub_positions.index(sub_position))
            plt.plot([2, 2], [y - 0.1, sub_y + 0.1], color='gray', linestyle='-', linewidth=1)

    # Add title
    plt.title('New York Police Hierarchy Chart', fontsize=16)

    # Adjust layout to make room for title and display the plot
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

create_hierarchy_chart()
