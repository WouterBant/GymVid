import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import datetime
import os


"""
The functions in this file generate a personal training scheme in pdf from an uploaded xlsx file.
The make_personal_scheme function is called in the last function in the views.py file which renders the page on which you can download the scheme.

Code for table from: https://levelup.gitconnected.com/how-to-write-a-pandas-dataframe-as-a-pdf-5cdf7d525488
"""


# Draws the table on the pdf
def _draw_as_table(df, pagesize):
    alternating_colors = [['white'] * len(df.columns), ['lightgray'] * len(df.columns)] * len(df)
    alternating_colors = alternating_colors[:len(df)]
    fig, ax = plt.subplots(figsize=pagesize)
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values,
             rowLabels=df.index,
             colLabels=df.columns,
             rowColours=['lightblue']*len(df),
             colColours=['lightblue']*len(df.columns),
             cellColours=alternating_colors,
             loc='center')
    return fig


# Generates a pdf containing personal information and the table with exercises, sets, reps, and weights
def dataframe_to_pdf(df, filename, name_receiver, name_creator, subject, user_input, date=datetime.datetime.now(), pagesize=(11, 8.5)):
    with PdfPages(filename) as pdf:
        plt.figure()
        plt.axis('off')

        # Display personal information
        plt.text(0.5, 0.5,
                 f"Training plan for: {name_receiver}\n1 RM: {user_input}kg\nCreated by: {name_creator}\nProgram: {subject}\nTime created: {date}",
                 ha='center', va='center')
        pdf.savefig()
        plt.close()

        # On the next page draw the table
        nh, nv = 1, 1
        rows_per_page = len(df) // nh
        cols_per_page = len(df.columns) // nv
        for i in range(0, nh):
            for j in range(0, nv):
                page = df.iloc[(i*rows_per_page):min((i+1)*rows_per_page, len(df)), (j*cols_per_page):min((j+1)*cols_per_page, len(df.columns))]
                fig = _draw_as_table(page, pagesize)
                if nh > 1 or nv > 1:
                    fig.text(0.5, 0.5/pagesize[0], "Part-{}x{}: Page-{}".format(i+1, j+1, i*nv + j + 1), ha='center', fontsize=8)
                pdf.savefig(fig, bbox_inches='tight')
                plt.close()


# Transforms the data such that the scheme is personal
def make_personal_scheme(df, name_receiver, name_creator, subject, user_input, file_count):
    # Use pandas to read excel file
    data = pd.read_excel(df)

    # Update weight column based on max weight entered by user
    data['Weight'] *= user_input

    # When a cell is left empty in the description column, say no notes
    data = data.fillna("No notes")

    # Generate name of new pdf file
    filename = f"{subject}_{name_receiver}_{file_count}.pdf"

    # Get the path of the new pdf file, this is in an external directory mediafiles_cdn
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(os.path.dirname(BASE_DIR), 'mediafiles_cdn') + "\\" + filename

    return dataframe_to_pdf(data, filepath, name_receiver, name_creator, subject, user_input)
