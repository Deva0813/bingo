from fpdf import FPDF

class PDF_GENERATOR:
    def create_bingo_cards_pdf(cards, pdf_filename='bingo_cards.pdf'):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        for i, card in enumerate(cards):
            pdf.add_page()

            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, f"Bingo Card {i+1}", ln=True, align='C')
            pdf.ln(10)  

            pdf.set_font("Arial", 'B', 20)
            pdf.cell(0, 10, "B   I   N   G   O", ln=True, align='C')
            pdf.ln(10)  

            card_width = card.shape[1] * 15
            horizontal_position = (pdf.w - card_width) / 2

            pdf.set_font("Arial", 'B', 12)
            for row in card:
                pdf.set_x(horizontal_position)
                for num in row:
                    if(num == 0):
                        pdf.cell(15, 15, str(" "), border=1,align='C')
                    else:
                        pdf.cell(15, 15, str(num), border=1,align='C')
                pdf.ln()

        pdf.output(pdf_filename)
