from function import get_operations,

def main():
    operations = get_operations('operations.json')
    for op in operations:
        print(op)

if __name__ == '__main__':
    main()
