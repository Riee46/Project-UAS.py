def fizz_buzz(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Example usage:
n = 6
output = fizz_buzz(n)
print("".join(output))

n = 9
output = fizz_buzz(n)
print("".join(output))



def is_same_hand(word):
    left_hand = set("qwertasdfgzxcvb")
    right_hand = set("yuiophjklmnm")

    left_count = right_count = 0

    for char in word:
        if char in left_hand:
            left_count += 1
        elif char in right_hand:
            right_count += 1

    return left_count == 0 or right_count == 0

# Example usage:
print(is_same_hand("helo"))  # False
print(is_same_hand("world"))  # True


def tangan_nya_sama(word):
    kiri = set("helo")
    kanan = set("world")

    kiri = kanan = 0

    for right in kanan:
        if right in kiri:
            kiri += 1
        elif right in kanan:
            kanan += 1

    return kiri == 0 or kanan == 0

print(tangan_nya_sama("helo")) 
print(tangan_nya_sama("world")) 




def count_words_with_broken_letters(sentence):
    broken_letters = set('ed')
    words = sentence.split()
    count = 0
    
    for word in words:
        if any(char in broken_letters for char in word):
            count += 1
            
    return count

# Example usage:
input_sentence = "Hello World"
output = count_words_with_broken_letters(input_sentence.lower())
print(output)  # Output: 2

input_sentence = "Aku sangat senang ngoding di pagi hari yang cerah ini"
output = count_words_with_broken_letters(input_sentence.lower())
print(output)  # Output: 14
