def word_count(file_contents):
        counted_words = 0
        all_words = file_contents.split()
        for words in all_words:
                counted_words += 1
        return counted_words

def char_count(file_contents):
	chars = {}
	low_text = file_contents.lower()
	for character in low_text:
		if character in chars:
			chars[character] = chars[character]+1
		else:
			chars[character] = 1
	return chars

def sorter(unsorted_dict):
	sorted_list = sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True)
	return sorted_list
