from fpdf import FPDF


# create function to generate the pdf report
def generate_analyst_report(startup_name, country, pep_results, null_checks, risk_score, qualification):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
#report title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "Startup Compliance Report", align="C")
# Information about the startup
    pdf.set_font("Arial", size=12)
    pdf.cell(200,10, f"Startup Name: {startup_name}", ln=True)
    pdf.cell(200,10, f"Country: {country}", ln=True)
    pdf.cell(200,10, f"PEP Results: {pep_results}", ln=True)
    for match in pep_results:
        pdf.cell(200, 10, f" - Name: {match['name']}, Score: {match['score']}", ln=True)
    pdf.cell(200,10, f"Overall Risk Score: {risk_score}", ln=True)
    pdf.cell(200,10, f"Qualification Score: {qualification}", ln=True)
    pdf.cell(200,10, f" - Status: {qualification[0]}", ln=True)
    pdf.cell(200,10, f" - Reason: {qualification[1]}", ln=True)

    filename = f"{startup_name}_report.pdf"
    pdf.output(filename)
    print(f" PDF Report generated: {filename}")


