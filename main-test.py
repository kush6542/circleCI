from main import Add


def TestAdd():
        assert Add(21,3) == 24
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()