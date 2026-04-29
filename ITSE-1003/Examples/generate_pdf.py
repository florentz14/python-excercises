from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer, Image

doc = SimpleDocTemplate(
    'invoice.pdf',
    pagesize=A4,
    rightMargin=20*mm,
    leftMargin=20*mm,
    topMargin=20*mm,
    bottomMargin=20*mm
)

styles = getSampleStyleSheet()
story = []

logo_path = 'nn_logo.jpg'
try:
    logo = Image(logo_path, width=35*mm, height=35*mm)
    story.append(logo)
except:
    logo = Paragraph('<b>ACME Corporation</b>', styles['Title'])
    story.append(logo)

story.append(Spacer(1, 12*mm))

title = Paragraph('INVOICE', styles['Heading1'])
story.append(title)

story.append(Spacer(1, 6*mm))

invoice_data = [
    ['Invoice #:', '001', 'Date:', '27/04/2026'],
    ['Client:', 'John Doe', 'Due Date:', '30/05/2026'],
]

invoice_table = Table(invoice_data)
story.append(invoice_table)

story.append(Spacer(1, 12*mm))

line_items = [
    ['Item', 'Quantity', 'Unit Price', 'Total'],
    ['Product A', '5', '$100.00', '$500.00'],
    ['Product B', '3', '$50.00', '$150.00'],
    ['Service C', '1', '$200.00', '$200.00'],
]

items_table = Table(line_items)
items_table.setStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
])

story.append(items_table)

story.append(Spacer(1, 12*mm))

total = Paragraph('<b>Total: $850.00</b>', styles['Heading2'])
story.append(total)

doc.build(story)
print("PDF generated successfully: invoice.pdf")
