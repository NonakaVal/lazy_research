import os 

# Function to select the PDF in the 'transcripts/' folder
def select_pdf():
    pdf_folder = './documents/'  # Folder where PDFs are stored
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the 'documents/' folder. Check the path and try again.")
        return None
    
    print("Available PDFs:")
    for i, pdf_file in enumerate(pdf_files, start=1):
        print(f"{i}. {pdf_file}")
    
    while True:
        try:
            choice = int(input(f"Enter the number of the PDF you want to use (1-{len(pdf_files)}): "))
            if 1 <= choice <= len(pdf_files):
                selected_pdf = pdf_files[choice - 1]
                return os.path.join(pdf_folder, selected_pdf)
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to set the output directory path
def select_output_directory():
    output_dir = input("Escolha o nome do diretório que será criado para salvar seus resumos \n ")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir