# Experimental RAG  
An RAG model that parses and retrieves data from PDF,XLSX,CSV,TXT,Word and JSON files, uses GROQ api for structuring the output.  
In this case I used a pdf file of my favourite non fiction book.

### Create virtual environment
`python -m venv .venv`
### Activate venv  
Windows:  
`.venv/scripts/activate`  

### Install dependencies:
`pip install -r requirements.txt`

### Create a dotenv file (.env) and input your GROQ api key:  
`GROQ_API_KEY="your-api-key-here"`  

### Run inference:  
`python app.py`  
Note: Make sure to uncomment the store.load() line and comment the line above it after running inference for the first time to avoid redundancy
