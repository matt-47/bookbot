import sys
arg_count = 0
for args in sys.argv:
	arg_count += 1

if arg_count < 2:
	print ("This program needs a path to a book to work correctly. Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book_path = sys.argv[1]

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	book_text = get_book_text(book_path)
	from stats import word_count
	book_words = word_count(book_text)
	from stats import char_count
	book_chars = char_count(book_text)
	from stats import sorter
	sorted_out = sorter(book_chars)
	print ("Found", book_words, "total words")
	for char, amount in sorted_out:
		if char.isalnum() == True:
			print (char+":", amount)
		else:
			pass


main()
