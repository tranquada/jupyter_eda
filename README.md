# Jupyter EDA (jupyter_eda)
Jupyter EDA is a small set of tools designed to assist with exploratory data
analysis (EDA) in Jupyter Notebook by wrapping around and providing convenient
access to tools for data munging, analysis, and visualization from modules such
as:

* Matplotlib (for data visualization)
* NumPy (for data handling and manipulation)
* Pandas (for data handling and manipulation)
* SciKit-learn (for data handling and manipulation)
* Seaborn (for data visualization)

It also relies on a few other modules for reporting and functionality:

* IPython (for output formatting in Jupyter Notebook)
* Jinja2 (for HTML and CSS templating)
* TQDM (for graphical progress bars)
* Weasyprint (for PDF output)

## Data wrangling for machine learning and the "TAPE" model for EDA
We all know that before you can start loading your data into statistical models
for machine learning, there is a lot of cleaning and general data "munging" or
"wrangling" that has to be done so that your dataset is ready to start throwing
linear algebra at it. Unfortunately, despite the power of tools like NumPy,
Pandas, and SciKit-learn, it can be difficult to really get down and dirty with
the data while also ensuring process reproducibility and repeatability. With
that in mind, Jupyter EDA focuses on providing four kinds of functionality to
speed up and improve your EDA and data preprocessing workflows:

1. **Tracking**
    * Organize and track your data to ensure you know what you're working with,
    when it was edited, and how
    * Log your cleaning and feature engineering process to ensure reproducibility
    * Segregate training/testing data and different variable types to ensure
    proper data handling
2. **Analyzing**
    * Perform a variety of automated initial data analysis (IDA) and exploratory
    data analysis (EDA) functions
    * Use special analysis tools for data such as text and datetime objects to
    examine useful patterns prior to feature engineering
3. **Producing**
    * Use automated functions to clean your data and impute missing values based
    on various best practices
    * Generate pre-designed reports and plots to get a snapshot of key aspects
    of your dataset
    * Engineer new features using built-in or ad hoc "recipes"
4. **Exporting**
    * Export your data, logs, or even a whole pickled Dataset object in case you
    need to move your work somewhere else
    * Save your reports and visualizations in a variety of useful formats,
    including PDF and embed-ready HTML
    * Repackage your data preprocessing steps as pipeline-ready objects with
    fit() and transform() functions
    * Create custom data objects that are ready for monitoring
