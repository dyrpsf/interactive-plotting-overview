# Interactive Plotting Frameworks in Python for Web‑based Reporting

## 1. Context and requirements

This document gives a first overview of several interactive plotting frameworks in Python that could be used for automated reporting in the **sbmlsim** project.  
The automated reporting workflow needs plotting tools that:

- work well with **Python** and scientific/numerical data (time courses, parameter scans, sensitivity analyses),
- can be embedded into **HTML‑based web reports** (e.g. Quarto, GitHub Pages),
- optionally support **static export** (PNG/SVG/PDF) for inclusion in **Typst/PDF** reports,
- are reasonably mature, documented, and maintained,
- do not make CI/CD workflows overly complex (dependencies, build steps).

Below is a high‑level comparison followed by short notes on each framework.

## 2. High‑level comparison

| Library              | Primary style              | Interactivity level                            | HTML / web embedding                                    | Static export for PDF reports                     | Quarto integration                              | Strengths                                                                 | Main limitations / trade‑offs                                                                 |
|----------------------|---------------------------|------------------------------------------------|---------------------------------------------------------|---------------------------------------------------|--------------------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Plotly**           | Imperative (Python API)   | Very high (zoom, pan, hover, legends, widgets) | Embeds as self‑contained HTML/JavaScript               | PNG/SVG/PDF via `kaleido` or `orca` (extra dep.)  | Good support; interactive figures work in Quarto | Rich interactive plots; large ecosystem; good time‑series support        | Heavier JavaScript payload; static export adds extra dependency; styling can be verbose       |
| **Altair (Vega‑Lite)** | Declarative (“grammar of graphics”) | High (tooltips, selection, brushing, linked views) | Exports to Vega‑Lite JSON + JS; easy HTML embedding    | PNG/SVG/PDF via Vega‑Lite export tools            | Native support for Vega/Vega‑Lite in Quarto      | Concise syntax; good for statistical/relational data; powerful linked interaction | Large raw datasets can be an issue (JSON size); requires export tooling for static images     |
| **Bokeh**            | Imperative / object model | High (pan/zoom, hover, linked plots, widgets)  | Generates HTML + JS; supports standalone pages or apps | Static PNG/SVG via extra tools (e.g. Selenium)    | Works in Quarto via embedded Bokeh components    | Flexible interactive plots; can power small dashboards or apps           | More complex stack for export; heavier setup for dashboards (Bokeh server)                    |
| **HoloViews + Panel**| High‑level on top of Bokeh/Matplotlib/Plotly | High (dynamic maps, widgets, dashboards)        | Panel apps/pages can be served or embedded as HTML     | Uses backend capabilities (e.g. Matplotlib/Plotly)| Embedding possible; works well in notebooks      | Very productive for exploratory work and dashboards; integrates several backends | Additional abstraction layer to learn; may be more than needed for simple plots               |
| **Matplotlib**       | Imperative, static‑oriented| Low–medium (basic interactivity via backends)  | Images embedded as PNG/SVG in HTML                     | Excellent static PNG/SVG/PDF output               | Quarto supports Matplotlib figures well          | Standard scientific plotting library; stable; excellent for publication‑quality static figs    | Limited browser‑side interactivity; interactive HTML usually needs extra tools (e.g. mpld3)   |

## 3. Framework notes

### 3.1 Plotly

- **Usage style:** object‑oriented Python API; also has a “plotly express” high‑level API for quick figures.
- **Interactivity:** rich built‑in interactivity (zoom, pan, hover tooltips, legends, animation, sliders, selection).
- **Web embedding:** produces HTML + JavaScript that can be saved as a standalone HTML file or embedded into web pages.  
  Works well in Jupyter notebooks and other notebook environments.
- **Static export:** uses additional tools such as `kaleido` (recommended) to export to PNG/SVG/PDF. This extra dependency would need to be available in CI for automatic report builds.
- **Quarto:** Quarto supports Plotly out of the box; interactive figures are preserved in rendered HTML documents.
- **Suitability for sbmlsim:** good candidate for interactive **time‑course plots**, **parameter scans**, and **sensitivity analysis** visualizations in HTML reports. Also supports subplots and small multiples.

### 3.2 Altair (Vega‑Lite)

- **Usage style:** declarative; the user specifies *what* should be shown (encodings, marks, data) instead of step‑by‑step drawing commands.
- **Interactivity:** uses Vega‑Lite’s interaction model: hover tooltips, selection, filtering, zooming, brushing, linked plots, etc.
- **Web embedding:** renders to Vega‑Lite JSON plus a small JavaScript runtime; easy to embed into static HTML pages.
- **Static export:** uses Vega/Vega‑Lite export tools to generate PNG/SVG/PDF. This typically requires a small helper tool installed (e.g. `vl-convert` or node‑based tooling) and would need to be configured for CI.
- **Quarto:** Quarto has native support for Vega‑Lite, which makes Altair plots integrate nicely into Quarto HTML reports.
- **Suitability for sbmlsim:** very good for **statistical summaries**, **distribution plots**, and **linked views** (e.g. exploring sensitivity analysis results across many parameters). The concise syntax may make templates easier to maintain.

### 3.3 Bokeh

- **Usage style:** Python object model; users construct figures, glyphs, and layouts using Python.
- **Interactivity:** supports many interactive features (hover, zoom, pan, selection, linked panning/zooming) and interactive widgets.
- **Web embedding:** can output standalone HTML files, script + div components that can be embedded in other pages, or full Bokeh server apps.
- **Static export:** static PNG/SVG export is possible but usually requires a headless browser and Selenium; CI configuration may be more involved.
- **Quarto:** Bokeh figures can be embedded into Quarto documents when rendered from Python code cells.
- **Suitability for sbmlsim:** useful if the project later wants more *dashboard‑like* interfaces (e.g. interactive exploration of many simulation scenarios), but might be heavier than necessary for simple report figures.

### 3.4 HoloViews + Panel

- **Usage style:** HoloViews provides a high‑level interface where users describe data and visual mappings; the actual rendering backend can be Bokeh, Matplotlib, or Plotly.  
  Panel is used to build interactive apps and dashboards from these components.
- **Interactivity:** strong support for interactive widgets, sliders, and dynamic updating of plots as parameters change.
- **Web embedding:** Panel apps can be served as standalone web applications or embedded into existing pages as components.
- **Static export:** depends on the chosen backend (e.g. Matplotlib for high‑quality static figures, Plotly/Bokeh for interactive ones).
- **Suitability for sbmlsim:** could be interesting for advanced dashboards (e.g. interactively changing parameters and seeing sbmlsim outputs), but it introduces another abstraction layer on top of the base plotting libraries.

### 3.5 Matplotlib (baseline)

- **Usage style:** imperative plotting library; standard in the scientific Python ecosystem.
- **Interactivity:** mainly limited to interactive backends in desktop or notebook environments; browser‑side interactivity is not the main focus.
- **Web embedding:** usually used by exporting PNG/SVG images which can be embedded into HTML or PDF.
- **Static export:** very strong; widely used for publication‑quality figures in PNG/SVG/PDF formats.
- **Suitability for sbmlsim:** excellent for **static figures** in PDF/Typst reports and for reproducible, publication‑ready plots. For fully interactive HTML reports, it would likely need to be complemented by another library.

## 4. Initial thoughts for sbmlsim automated reporting

- For **interactive HTML reports**, **Plotly** and **Altair** appear to be the most straightforward options due to their good Quarto integration and rich interactivity.
- **Matplotlib** remains valuable for **high‑quality static figures** in PDF/Typst reports.
- **Bokeh** (and higher‑level tools like **HoloViews + Panel**) become more attractive if there is a future goal of building **dashboards or small web apps** for exploring simulation results, beyond static reports.
- A possible approach is to start with a small set of **standard plot types** (e.g. time‑course plots, parameter scan plots, sensitivity bar charts) in one main interactive library, and keep Matplotlib for static exports.

---
## 5. Plot types for sensitivity and uncertainty analysis

Based on typical workflows for sensitivity analysis (SA) and uncertainty quantification (UQ), the automated reporting in sbmlsim will likely need at least the following plot types:

1. **Time‑course plots with uncertainty bands**
   - Show simulation output over time together with uncertainty (e.g. 5th–95th percentile).
   - Often displayed as a mean or median curve with a shaded region around it.
   - Important for visualizing the effect of parameter uncertainty on key observables.

2. **Bar plots of sensitivity indices**
   - One bar per parameter, with height equal to a sensitivity index (e.g. first‑order or total‑order Sobol index, eFAST index, Morris measure).
   - Useful for ranking parameters by importance.
   - Frequently used both for local and global sensitivity summaries.

3. **Heatmaps / matrices of sensitivities**
   - Parameters on one axis, outputs or time points on the other.
   - Color encodes sensitivity strength.
   - Highlights how parameter influence changes across outputs or time.

4. **Scatter plots and correlation plots**
   - Scatter plots of parameter values vs. outputs.
   - Correlation‑based methods (e.g. PRCC, Spearman) can be visualized as:
     - scatter plots with regression lines, or
     - bar plots of correlation coefficients.
   - Useful to inspect monotonic but nonlinear relationships.

5. **Distribution plots for key outputs**
   - Histograms, kernel density estimates, or violin/box plots of important outputs (e.g. maximum concentration, AUC).
   - Derived from Monte Carlo simulations.
   - Show overall uncertainty distribution, not just point estimates.

### Mapping of plot types to candidate libraries

- **Plotly**
  - Time‑course with uncertainty bands: straightforward using multiple traces with `fill='tonexty'`.
  - Sensitivity bar plots and correlation bar plots: basic bar/scatter plots with hover information.
  - Heatmaps: built‑in heatmap support with good interactivity.
  - Distribution plots: histograms, violin plots, box plots are available.

- **Altair (Vega‑Lite)**
  - Time‑course plots and uncertainty bands: can be expressed declaratively with layered charts.
  - Sensitivity bar plots and heatmaps: well suited for tidy/tabular data, with good support for faceting and linked views.
  - Distribution plots: histograms and density plots can be defined in a compact way.

- **Bokeh / HoloViews + Panel**
  - All plot types above are possible, with additional options for interactive widgets (e.g. sliders for selecting time windows or parameter subsets).
  - Well suited if interactive dashboards for exploring SA/UQ results are desired.

- **Matplotlib**
  - Very good for static versions of these plots (especially time‑course with uncertainty bands and bar plots of sensitivities) to be used in PDF/Typst reports.
  - Less suitable for fully interactive HTML plots by itself, but can serve as a baseline for publication‑quality static figures.

These plot types and library mappings can serve as a starting point when designing the automated reporting templates for sbmlsim.

Author - Deepak Yadav