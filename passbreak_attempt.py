# EasyPGPeasy.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os, pgpy


def word():
    """Extract words from list with certain length."""

    f = open("words_alpha.txt", "r")
    wd_list = []

    for i in f:
        if len(i.strip()) == 10:
            wd_list.append(i)

    f.close()

    return wd_list


def word_caps(wl):
    """Returns all caps variations for each word in the word list provided."""

    mod_wl = []

    for i in wl:
        i = i.strip()
        mod_wl.append(i)
        wd = i

        # Change 1 letter to caps
        for j in range(0, 10):
            mod_word = "".join(c.upper() if i == j else c for i, c in enumerate(wd))
            mod_wl.append(mod_word.strip())

        # Change 2 letters to caps
        for j in range(0, 9):
            mod_word = "".join(c.upper() if i in [j, (j + 1)] else c for i, c in enumerate(wd))
            mod_wl.append(mod_word.strip())

        # Change 3 letters to caps
        for j in range(0, 8):
            mod_word = "".join(c.upper() if i in [j, (j + 1), (j + 2)] else c for i, c in enumerate(wd))
            mod_wl.append(mod_word.strip())

        # Change 4 letters to caps
        for j in range(0, 7):
            mod_word = "".join(c.upper() if i in [j, (j + 1), (j + 2), (j + 3)] else c for i, c in enumerate(wd))
            mod_wl.append(mod_word.strip())

        # Change 5 letters to caps
        for j in range(0, 6):
            mod_word = "".join(
                c.upper() if i in [j, (j + 1), (j + 2), (j + 3), (j + 4)] else c for i, c in enumerate(wd))
            mod_wl.append(mod_word.strip())

        # Change 6 letters to caps
        for j in range(0, 5):
            mod_word = "".join(
                c.upper() if i in [j, (j + 1), (j + 2), (j + 3), (j + 4), (j + 5)] else c for i, c in enumerate(wd))
            mod_wl.append(mod_word.strip())

        # Change 7 letters to caps
        for j in range(0, 4):
            mod_word = "".join(
                c.upper() if i in [j, (j + 1), (j + 2), (j + 3), (j + 4), (j + 5), (j + 6)] else c for i, c in
                enumerate(wd))
            mod_wl.append(mod_word.strip())

        # Change 8 letters to caps
        for j in range(0, 3):
            mod_word = "".join(
                c.upper() if i in [j, (j + 1), (j + 2), (j + 3), (j + 4), (j + 5), (j + 6), (j + 7)] else c for i, c in
                enumerate(wd))
            mod_wl.append(mod_word.strip())

        # Change 9 letters to caps
        for j in range(0, 2):
            mod_word = "".join(
                c.upper() if i in [j, (j + 1), (j + 2), (j + 3), (j + 4), (j + 5), (j + 6), (j + 7), (j + 8)] else c for
                i, c in enumerate(wd))
            mod_wl.append(mod_word.strip())

        mod_word = wd.upper()
        mod_wl.append(mod_word.strip())

    with open("capitalized_words.txt", "w") as f:
        for i in mod_wl:
            f.write("%s\n" % i)

    f.close()

    return mod_wl


def caesar_shift(m_w_l):
    """Shift letters X positions, in this case ten."""

    s_w_l = []

    for i in m_w_l:
        result = ""

        for j in range(len(i)):
            char = i[j]

            # Encrypt uppercase characters
            if char.isupper():
                result += chr((ord(char) + 10 - 65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + 10 - 97) % 26 + 97)

        s_w_l.append(result)

    with open("shifted_words.txt", "w") as f:
        for i in s_w_l:
            f.write("%s\n" % i)

    f.close()

    return s_w_l


def pgpy_decrypt(enc_mes, s_w_l):
    """Decrypt a plaintext message with a given encrypted message and passphrase."""

    result = ""

    for i in s_w_l:
        print(i)
        try:
            result = enc_message.decrypt(i)
        except pgpy.errors.PGPDecryptionError:
            pass

    return result


enc_message = pgpy.PGPMessage.from_file("pgp_message.txt")

word_list = word()

if not (os.path.exists("capitalized_words.txt")):
    mod_word_list = word_caps(word_list)
else:
    file1 = open("capitalized_words.txt", "r")
    mod_word_list = []

    for item in file1:
        mod_word_list.append(item.strip())

    file1.close()

if not (os.path.exists("shifted_words.txt")):
    shifted_word_list = caesar_shift(mod_word_list)
else:
    file2 = open("shifted_words.txt", "r")
    shifted_word_list = []

    for item in file2:
        shifted_word_list.append(item.strip())

    file2.close()

output = pgpy_decrypt(enc_message, shifted_word_list)


# try word
# output
