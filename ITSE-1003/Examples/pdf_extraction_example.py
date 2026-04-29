import pandas as pd
import pdfplumber

tables = []

with pdfplumber.open('digital-ocean.pdf') as pdf:
    for page in pdf.pages:
        tables_on_page = page.extract_tables({
            'vertical_strategy': 'text',
            'horizontal_strategy': 'text',
            'intersection_x_tolerance': 10,
            'intersection_y_tolerance': 10
        })

        if tables_on_page:
            for table in tables_on_page:
                if table:
                    tables.append({
                        'page': pdf.pages.index(page) + 1,
                        'data': table
                    })

for table in tables:
    print('Page:', table['page'])
    print(pd.DataFrame(table['data']))
