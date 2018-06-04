def fizzbuzz(num):
    def working(new_num):
        if new_num > 0:
            if new_num % 3 == 0 and new_num % 5 == 0:
                print('fizzbuzz')
                working(new_num-1)
            elif new_num % 5 == 0:
                print('buzz')
                working(new_num - 1)
            elif new_num % 3 == 0:
                print('fizz')
                working(new_num - 1)
            else:
                print(new_num)
                working(new_num - 1)
        else:
            print('done')

    working(num)


fizzbuzz(10)
