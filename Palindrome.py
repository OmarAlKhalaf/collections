def sample_tests():
    question = input('typ the name that u like to check : ')
    reverse = question[::-1]
    if (question == reverse):
        print('yes it is a paliadrome')
    else:
        print('No it is not a paliadrome')
sample_tests()