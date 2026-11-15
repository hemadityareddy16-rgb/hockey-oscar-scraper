from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

file = "hockey_teams.xlsx"
wb = load_workbook(file)

wb.worksheets[0].title = "Hockey Teams"

header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill("solid", fgColor="1F4E78")

for ws in wb.worksheets:
    for cell in ws[1]:
        cell.font = header_font
        cell.fill = header_fill

    ws.freeze_panes = "A2"

    for col in ws.columns:
        longest = max(len(str(c.value)) if c.value is not None else 0
                      for c in col)
        ws.column_dimensions[col[0].column_letter].width = longest + 3

wb.save(file)
print("Formatting done for", len(wb.worksheets), "sheets")