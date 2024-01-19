# # 1. Даний текстовий файл. Необхідно створити новий файл,
# # який потрібно переписати з першого файлу всі слова, що складаються не менше ніж з семи літер.
# def filter_long_words(input_text):
#     words = input_text.split()
#     long_words = [word if len(word) >= 7 else "*" * len(word) for word in words]
#     return " ".join(long_words)
# # 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
# def count_words(input_text):
#     words = input_text.split()
#     return len(words)
# # 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
# def censor_forbidden_words(input_text, forbidden_word):
#     regex = re.compile(r"\b" + re.escape(forbidden_word) + r"\b", re.IGNORECASE)
#     return regex.sub("*" * len(forbidden_word), input_text)
#
# # Текст для прикладу
# input_text = """
# Say, can you see
# By the dawn's early light
# What so proudly we hailed
# At the twilight's last gleaming?
# Whose broad stripes and bright stars
# Through the perilous fight
# O'er the ramparts we watched
# Were so gallantly, yeah, streaming?
# And the rockets' red glare
# The bombs bursting in air
# Gave proof through the night
# That our flag was still there
# O say, does that star-spangled banner yet wave
# O'er the land of the free and the home of the brave.
# """
#
# forbidden_word = "the"
#
# def replace_the(text):
#     return text.replace("the", "***")
#
# input_text = """
# Say, can you see
# By the dawn's early light
# What so proudly we hailed
# At the twilight's last gleaming?
# Whose broad stripes and bright stars
# Through the perilous fight
# O'er the ramparts we watched
# Were so gallantly, yeah, streaming?
# And the rockets' red glare
# The bombs bursting in air
# Gave proof through the night
# That our flag was still there
# O say, does that star-spangled banner yet wave
# O'er the land of the free and the home of the brave.
# """
#
# result_text = replace_the(input_text)
# print(result_text)
#
#
#
#
#
#
#
