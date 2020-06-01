def reverseLookup(dict, value):
    return [pair[0] for pair in dict.items() if pair[1] == value]

def main():
    dict = {'Labrador Retriever' : 'dog',
            'Siberian Husky' : 'dog',
            'Ragdoll' : 'cat',
            'Poodle' : 'dog'}

    # Present the user with the original dictionary
    print("Base dictionary:", dict)
    # Check for multiple keys
    print("Checking for: dog")
    print("Matching keys:", reverseLookup(dict, 'dog'))
    # Check for one key
    print("Checking for: cat")
    print("Matching keys:", reverseLookup(dict, 'cat'))
    # Check for no keys
    print("Checking for: nothing")
    print("Matching keys:", reverseLookup(dict, 'nothing'))

if __name__ == '__main__':
    main()
