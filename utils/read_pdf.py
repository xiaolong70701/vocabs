import pdfplumber, re
import numpy as np
from miscell import *

def read_pdf(filename):
    ## define English chars
    en_letter = '[\u0041-\u005a|\u0061-\u007a]+' # result: '[A-Z|a-z]+'

    ## read pdf file
    pdf = pdfplumber.open(filename) # open the target pdf file

    ## find all vocabularies
    vocabs = []
    for i in range(1, len(pdf.pages)):
        page = pdf.pages[i].extract_text().replace('\n', '')
        for vocab in re.findall(en_letter,page):
            vocabs.append(vocab)
    
    vocabs = np.unique(vocabs).tolist() # remove repeated values
    vocbas = remove_alphas(vocabs) # remove alphabets
    return to_lower(sorted(vocabs, reverse=False))