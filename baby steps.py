def find_difference(A, B):
    correct_answer = A + B
    chef_output = A * B
    return abs(correct_answer - chef_output)

# Main function to read inputs and call the helper function
def main():
    A, B = map(int, input().strip().split())
    difference = find_difference(A, B)
    print(difference)

if __name__ == "__main__":
    main()
