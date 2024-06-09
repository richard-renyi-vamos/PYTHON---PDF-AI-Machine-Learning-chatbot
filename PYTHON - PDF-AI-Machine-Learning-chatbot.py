import fitz  # PyMuPDF
from transformers import pipeline

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Load a pre-trained question-answering model
qa_pipeline = pipeline("question-answering")

# Function to answer questions based on the extracted text
def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Main function to integrate the steps
def main(pdf_path, question):
    # Step 1: Extract text from the PDF
    context = extract_text_from_pdf(pdf_path)
    
    # Step 2: Answer the question
    answer = answer_question(question, context)
    
    return answer

# Command-line interface
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Ask questions based on a PDF document.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF document.")
    parser.add_argument("question", type=str, help="The question to ask.")
    
    args = parser.parse_args()
    
    answer = main(args.pdf_path, args.question)
    print(f"Question: {args.question}")
    print(f"Answer: {answer}")
