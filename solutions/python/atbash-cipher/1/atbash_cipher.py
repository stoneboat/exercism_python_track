def gen_coding_book():
    plaintext = 'abcdefghijklmnopqrstuvwxyz1234567890'
    ciphertext = 'zyxwvutsrqponmlkjihgfedcba1234567890'

    encoding_book = {}
    decoding_book = {}
    book_len = len(plaintext)

    for i in range(book_len):
        encoding_book[plaintext[i]] = ciphertext[i]
        decoding_book[ciphertext[i]] = plaintext[i]
    
    return encoding_book, decoding_book


def encode(plain_text):
    encoding_list = []
    encoding_book, _ = gen_coding_book()

    # Get a pre-proceed plaintext 
    plain_text_list = []
    plain_text = plain_text.lower()
    for char in plain_text:
        if encoding_book.get(char, None) is None:
            continue 
        else:
            plain_text_list.append(char)
    plain_text = "".join(plain_text_list)

    # start encoding 
    for chunk in range(0, len(plain_text), 5):
        piece = plain_text[chunk:chunk+5]
        encoding_piece_list = []
        for i in range(len(piece)):
            encoding_piece_list.append(encoding_book[piece[i]])
        
        encoding_list.append("".join(encoding_piece_list))
    
    return " ".join(encoding_list)


def decode(ciphered_text):
    plaintext_list = []
    _, decoding_book = gen_coding_book()

    ciphered_text = ciphered_text.replace(" ", "")
    for char in ciphered_text:
        if decoding_book.get(char, None) is None:
            plaintext_list.append(char)
        else:
            plaintext_list.append(decoding_book[char])
    
    return "".join(plaintext_list)
