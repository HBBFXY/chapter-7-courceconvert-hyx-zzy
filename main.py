# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 1. 读取random_int.py文件内容
with open("random_int.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 2. 处理每一行内容（非保留字转大写）
processed_lines = []
for line in lines:
    # 按空格分割单词（保留符号/缩进）
    parts = []
    current_word = ""
    for char in line:
        if char.isalnum() or char == "_":  # 单词的组成部分（字母/数字/下划线）
            current_word += char
        else:
            if current_word:  # 处理当前积累的单词
                # 判断是否是保留字，非保留字则转大写
                if current_word not in reserved_words:
                    current_word = current_word.upper()
                parts.append(current_word)
                current_word = ""
            parts.append(char)  # 添加非单词字符（空格、符号等）
    # 处理行末尾的单词
    if current_word:
        if current_word not in reserved_words:
            current_word = current_word.upper()
        parts.append(current_word)
    # 拼接处理后的行
    processed_line = "".join(parts)
    processed_lines.append(processed_line)

# 3. 将处理后的内容写入新文件（比如output.py）
with open("converted_random_int.py", "w", encoding="utf-8") as f:
    f.writelines(processed_lines)

print("转换完成！结果已保存到 converted_random_int.py")
