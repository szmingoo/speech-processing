import jieba
from pypinyin import lazy_pinyin, Style
import json
import os
from loguru import logger


def load_polyphonic_word_dict(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    with open(config_path, 'r', encoding='utf-8') as file:
        word_dict = json.load(file)
    logger.info("Loaded polyphonic word dictionary from config.")
    return word_dict


config_path = os.getenv('CONFIG_PATH', 'config/polyphonic_word_config.json')
polyphonic_word_dict = load_polyphonic_word_dict(config_path)


# 获取词的拼音，并根据多音字字典进行判断
def get_correct_pinyin(word, polyphonic_word_dict, index, words):
    pinyin_list = lazy_pinyin(word, style=Style.TONE3)
    for i, char in enumerate(word):
        if char in polyphonic_word_dict:
            # 获取前后文进行匹配
            context_start = max(0, index - 1)
            context_end = min(len(words), index + 2)
            context = ''.join(words[context_start:context_end])

            for pinyin, contexts in polyphonic_word_dict[char].items():
                for context_phrase in contexts:
                    if context_phrase in context:
                        pinyin_list[i] = pinyin
                        break
    return pinyin_list


# 生成 SSML
def generate_ssml(text: str) -> str:
    words = jieba.lcut(text)
    ssml = ""
    for index, word in enumerate(words):
        word_pinyin = get_correct_pinyin(word, polyphonic_word_dict, index, words)
        word_ssml = ""
        for char, char_pinyin in zip(word, word_pinyin):
            if char in polyphonic_word_dict:
                word_ssml += f'<phoneme alphabet="pinyin" ph="{char_pinyin}">{char}</phoneme>'
            else:
                word_ssml += char
        ssml += word_ssml
    return ssml
