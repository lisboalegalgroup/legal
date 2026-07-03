import os
import re
import fitz  # PyMuPDF

def extract_terms_from_pdf(pdf_path, keywords, output_file):
    try:
        doc = fitz.open(pdf_path)
        base_name = os.path.basename(pdf_path)
        output_file.write(f"\n{'='*50}\n")
        output_file.write(f"DOCUMENT: {base_name}\n")
        output_file.write(f"{'='*50}\n")

        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            
            # Split by articles or paragraphs
            # Often Ecuadorian laws use "Art. " or "Artículo "
            paragraphs = re.split(r'(?i)(?=artículo \d+|art\. \d+)', text)
            
            for para in paragraphs:
                para_lower = para.lower()
                if any(kw in para_lower for kw in keywords):
                    # Clean up newlines for easier reading
                    clean_para = " ".join(para.split())
                    output_file.write(f"--- Page {page_num + 1} ---\n")
                    output_file.write(clean_para + "\n\n")

    except Exception as e:
        output_file.write(f"Error processing {pdf_path}: {str(e)}\n")

def main():
    folder = r"c:\Users\ja_Ca\Desktop\NORMATIVA"
    output_path = r"c:\Users\ja_Ca\Desktop\lisboa legal group\resultados_plazos.txt"
    
    # Target specific PDFs
    targets = [
        "CODIGO ORGANICO GENERAL DE PROCESOS.pdf",
        "CÓDIGO ORGÁNICO INTEGRAL_PENAL COIP.pdf",
        "CODIGO DEL TRABAJO-CT.pdf",
        "CODIGO ORGANICO ADMINISTRATIVO-COA.pdf",
        "LEY ORGANICA DE GARANTIAS JURISDICCIONALEs.pdf",
        "CODIGO DE LA NIÑEZ Y ADOLESCENCIA..pdf",
        "LEY ORGÁNICA DE TRANSPORTE TERRESTRE, TRÁNSITO Y SEGURIDAD VIAL - LOTTTSV.pdf"
    ]
    
    keywords = ["término de ", "plazo de ", "días", "horas"]
    
    with open(output_path, "w", encoding="utf-8") as out_f:
        for file in targets:
            pdf_path = os.path.join(folder, file)
            if os.path.exists(pdf_path):
                print(f"Processing {file}...")
                extract_terms_from_pdf(pdf_path, keywords, out_f)
            else:
                out_f.write(f"FILE NOT FOUND: {pdf_path}\n")

if __name__ == '__main__':
    main()
