def main():
    import random
    random_generator = random.Random()
    random_number = random_generator.randint(0, 100)
    print(f"Random value: {random_number}")

    for _ in range(20):
        print(random_generator.randint(0, 100))


main()