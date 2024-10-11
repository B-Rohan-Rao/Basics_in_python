def search_word_in_file(filename,word):
    def file_reader(file_path):
        with open(file_path, 'r') as lines:
            yield lines  # Yield one line at a time instead of loading the entire file

    for lines in file_reader(filename):
        if word in lines:
            yield lines

# Usage example:
filename = 'largetextfile.txt' # Path to your large txt file
word_to_search = 'Python'

# Searching for the word 'Python' in the file
for matching_lines in search_word_in_file(filename, word_to_search):
    print(matching_lines)