import plotly.graph_objects as go

# Example parameter names and "total Sobol indices"
parameters = ["p1", "p2", "p3", "p4", "p5"]
total_indices = [0.45, 0.25, 0.15, 0.10, 0.05]

fig = go.Figure(
    go.Bar(
        x=parameters,
        y=total_indices,
        text=[f"{v:.2f}" for v in total_indices],
        textposition="outside",
    )
)

fig.update_layout(
    title="Example total-order sensitivity indices",
    xaxis_title="Parameter",
    yaxis_title="Total Sobol index",
    yaxis=dict(range=[0, 1]),
    template="plotly_white",
)

fig.show()