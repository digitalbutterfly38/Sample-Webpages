import pandas as pd
from openpyxl import load_workbook
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_from_excel(sample_file, source_file, output_folder):
    # Load sample Excel file
    sample_df = pd.read_excel(sample_file)
    
    # Load source Excel file
    source_df = pd.read_excel(source_file)
    
    for index, row in source_df.iterrows():
        pdf_file = f"{output_folder}/output_{index + 1}.pdf"
        
        c = canvas.Canvas(pdf_file, pagesize=letter)
        width, height = letter
        
        # Add data from sample_df
        for i, col in enumerate(sample_df.columns):
            c.drawString(50, height - 50 - (i * 15), f"{col}: {sample_df[col].values[0]}")
        
        # Add data from source_df
        for i, col in enumerate(source_df.columns):
            c.drawString(50, height - 150 - (i * 15), f"{col}: {row[col]}")
        
        c.showPage()
        c.save()

sample_excel_path = 'sample.xlsx'
source_excel_path = 'source.xlsx'
output_directory = 'output_pdfs'

create_pdf_from_excel(sample_excel_path, source_excel_path, output_directory)