def main():
    print("Enter two strings and I'll tell you if they are anagrams: ")

    first_string = input("Enter the first string: ")
    second_string = input("Enter the second string: ")

    if isAnagram(first_string, second_string):
        print(f'"{first_string}" and "{second_string}" are anagrams.')
    else:
        print("They are not anagrams.")

def isAnagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    
    return sorted(first_string) == sorted(second_string)

main()