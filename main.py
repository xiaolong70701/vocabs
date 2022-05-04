import sys, os, time
import pandas as pd
sys.path.append('/Users/anthonysung/Desktop/dict/utils')
from lookup import lookup
from read_pdf import read_pdf
from tqdm import tqdm
from miscell import *
from word import *

if __name__=="__main__":
    cwd = os.getcwd()
    simple_words = simple()
    result = []
    for file in range(107, 112):
        print('...開啟檔案中...')
        exams = read_pdf(cwd + f'/{file}.pdf')
        for index in range(0, len(simple_words)):
            if simple_words[index] in exams:
                exams.remove(simple_words[index])
        exams = sorted(exams, reverse=False)
        time.sleep(1)
        print(f'已成功開啟檔案：{file}.pdf')
        for exam in exams:
            print(f'目前查詢單字進度：{exam}')
            result.append(lookup(exam))
        pd.DataFrame(result).to_excel(cwd + f'/{file}.xlsx')