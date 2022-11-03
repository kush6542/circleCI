from main import Add


def TestAdd():
        assert Add(21,3) == 24
        assert Add(1, 3) == 464
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()