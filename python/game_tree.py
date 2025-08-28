import matplotlib.pyplot as plt

def draw_minimax_tree():
    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))

    # Define node positions (x, y) coordinates
    positions = {
        "Root (BOT)": (0.5, 1.0),
        "Move A (HUMAN)": (0.25, 0.7),
        "Move B (HUMAN)": (0.5, 0.7),
        "Move C (HUMAN)": (0.75, 0.7),
        "Move A1 (BOT)": (0.15, 0.4),
        "Move A2 (BOT)": (0.35, 0.4),
        "Move B1 (BOT)": (0.5, 0.4),
        "Move C1 (BOT)": (0.65, 0.4),
        "Move C2 (BOT)": (0.85, 0.4),
        "A1 Wins (BOT)": (0.15, 0.1),
        "A2 Draw": (0.35, 0.1),
        "B1 Loses (HUMAN)": (0.5, 0.1),
        "C1 Wins (BOT)": (0.65, 0.1),
        "C2 Draw": (0.85, 0.1)
    }

    # Define edges (connections between nodes)
    edges = [
        ("Root (BOT)", "Move A (HUMAN)"),
        ("Root (BOT)", "Move B (HUMAN)"),
        ("Root (BOT)", "Move C (HUMAN)"),
        ("Move A (HUMAN)", "Move A1 (BOT)"),
        ("Move A (HUMAN)", "Move A2 (BOT)"),
        ("Move B (HUMAN)", "Move B1 (BOT)"),
        ("Move C (HUMAN)", "Move C1 (BOT)"),
        ("Move C (HUMAN)", "Move C2 (BOT)"),
        ("Move A1 (BOT)", "A1 Wins (BOT)"),
        ("Move A2 (BOT)", "A2 Draw"),
        ("Move B1 (BOT)", "B1 Loses (HUMAN)"),
        ("Move C1 (BOT)", "C1 Wins (BOT)"),
        ("Move C2 (BOT)", "C2 Draw")
    ]

    # Draw nodes
    for node, (x, y) in positions.items():
        ax.scatter(x, y, s=500, color="lightblue", edgecolors="black", zorder=3)
        ax.text(x, y, node, ha="center", va="center", fontsize=8, zorder=4)

    # Draw edges
    for start, end in edges:
        x_start, y_start = positions[start]
        x_end, y_end = positions[end]
        ax.plot([x_start, x_end], [y_start, y_end], color="black", zorder=2)

    # Hide axes
    ax.axis("off")

    # Set title
    plt.title("Minimax Algorithm Game Tree", fontsize=16)

    # Show the plot
    plt.show()

# Call the function to draw the tree
draw_minimax_tree()
