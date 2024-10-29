def main():
	book = ""
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()

	book = file_contents

	print(word_count(book))

def word_count(book):
	words = book.split()
	count = 0
	for word in words:
		count += 1
	return count

main()
