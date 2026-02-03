import math
import plotly.graph_objects as go

# Simulated time points (0 to 10, step 0.1)
time = [i / 10 for i in range(0, 101)]

# Example "median" time-course (just a toy function)
median = [math.exp(-t / 3.0) * math.cos(t) for t in time]

# Simple uncertainty band: +/- 20% around the median
lower = [m * 0.8 for m in median]
upper = [m * 1.2 for m in median]

fig = go.Figure()

# Lower bound (plotted first, no fill)
fig.add_trace(
    go.Scatter(
        x=time,
        y=lower,
        line=dict(color="lightblue"),
        name="Lower bound (e.g. 5th percentile)",
        showlegend=False,
    )
)

# Upper bound with fill down to previous trace (shaded band)
fig.add_trace(
    go.Scatter(
        x=time,
        y=upper,
        line=dict(color="lightblue"),
        fill="tonexty",
        fillcolor="rgba(173, 216, 230, 0.4)",
        name="Uncertainty band (e.g. 5–95%)",
    )
)

# Median curve on top
fig.add_trace(
    go.Scatter(
        x=time,
        y=median,
        line=dict(color="blue"),
        name="Median time-course",
    )
)

fig.update_layout(
    title="Example time-course with uncertainty band",
    xaxis_title="Time",
    yaxis_title="Output",
    template="plotly_white",
)

fig.show()