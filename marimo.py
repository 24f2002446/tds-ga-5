# app.py
# Marimo interactive notebook
# Author contact: 24f2002446@ds.study.iitm.ac.in

import marimo

app = marimo.App()


# ---------------------------------------------------------
# Cell 1 — Imports and simple dataset
# ---------------------------------------------------------
@app.cell
def _():
    import numpy as np
    import pandas as pd

    # Example synthetic dataset
    df = pd.DataFrame({
        "x": np.linspace(0, 50, 100),
        "y": lambda x=np.linspace(0, 50, 100): 3 * x + 10 + np.random.randn(100) * 8
    })

    df
    return df
# Data flows → next cells (plotting, filtering)


# ---------------------------------------------------------
# Cell 2 — Create interactive slider widget
# ---------------------------------------------------------
@app.cell
def _(mo):
    # Slider controls the window size for smoothing the data
    window_slider = mo.ui.slider(start=1, stop=20, value=5, label="Smoothing Window")

    window_slider
    return window_slider
# window_slider → used in smoothing & markdown output


# ---------------------------------------------------------
# Cell 3 — Apply smoothing based on slider (dependency)
# ---------------------------------------------------------
@app.cell
def _(df, window_slider):
    # Smooth y using rolling window based on slider
    smoothed = df["y"].rolling(window_slider.value).mean()

    smoothed
    return smoothed
# smoothed depends on df + slider


# ---------------------------------------------------------
# Cell 4 — Interactive plot
# ---------------------------------------------------------
@app.cell
def _(df, smoothed, mo):
    import plotly.graph_objects as go

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["x"], y=df["y"], mode="markers", name="Original"))
    fig.add_trace(go.Scatter(x=df["x"], y=smoothed, mode="lines", name="Smoothed"))

    fig.update_layout(title="Relationship between X and Y (interactive smoothing)")
    fig
    return fig
# Plot depends on smoothed → changes when slider moves


# ---------------------------------------------------------
# Cell 5 — Dynamic markdown based on slider value
# ---------------------------------------------------------
@app.cell
def _(window_slider, mo):
    mo.md(
        f"""
### 📊 Dynamic Analysis Summary

- You selected a smoothing window of **{window_slider.value}**
- Larger windows → more smoothing, fewer fluctuations  
- Smaller windows → more noise preserved  

Move the slider to see the effect in real-time.
        """
    )
# Markdown dynamically updates using widget state


if __name__ == "__main__":
    app.run()
