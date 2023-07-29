# Open the first file in read mode
# with open(r"D:\\Cloud Lab/\file1.txt", 'r') as file1:
#     content1 = file1.read()

# # Open the second file in read mode
# with open(r"D:\\Cloud Lab\\file2.txt", 'r') as file2:
#     content2 = file2.read()

# # Open the first file in append mode and write the contents of the second file
# with open("D:\\Cloud Lab\\file1.txt", 'a') as file1:
#       file1.write(content)

# print("Files concatenated successfully.")
# print(content1)
# Calculate block size, rounding up)
import PyPDF2


file_path = r"C:\Users\Zeeshan Khan\Downloads\Lab 6-6-2023.pdf"

with open(file_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)
    num_pages = pdf_reader.numPages

    content = ""
    for page_number in range(num_pages):
        page = pdf_reader.getPage(page_number)
        content += page.extractText()

block_size = len(content) // 8
print("Block size:", block_size)
