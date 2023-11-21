import os
import sys
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import pyperclip
from langdetect import detect


BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

# 中转英
zh_en_model = "opus-mt-zh-en"  # 中文到英文的模型名
zh_en_model_dir = os.path.join(BASE_DIR, '__models__', 'zh_en', zh_en_model)  # 中文到英文的模型缓存目录路径
print(f'正在检测 {zh_en_model} 模型......')
zh_en_model = AutoModelForSeq2SeqLM.from_pretrained(zh_en_model_dir)
zh_en_tokenizer = AutoTokenizer.from_pretrained(zh_en_model_dir)
zh_en_translation = pipeline('translation_zh_to_en', model=zh_en_model, tokenizer=zh_en_tokenizer)

print(f'加载完成\n'
      f'按下 Ctrl+C 退出程序')
try:
    while True:
        text = input('\n')
        res = zh_en_translation(text)[0]['translation_text']
        res = res.replace(' ', '_').replace('.', '').lower().strip('. ')

        pyperclip.copy(res)
        print(res)

except KeyboardInterrupt:
    print('\n您已经退出程序')
