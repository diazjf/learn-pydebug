# Counts the amount of characters in words input
# by a user after removing the spaces
def count(message=""):
    msg = message.split()

    # NOTE: Error is here, since it thinks
    # any amount of words over 3 is too much
    # and doesn't state it in the error
    if len(msg) > 3:
        return "TOO MANY WORDS, TRY AGAIN"

    no_spaces = message.strip()
    no_spaces = no_spaces.replace(" ", "")
    return len(no_spaces)

if __name__ == "__main__":
    # ask for user input
    input = input("Enter some words: ")

    import pdb; pdb.set_trace()

    # count the number if characters
    num_chars = count(input)
    print("Number of Characters: %s" % num_chars)