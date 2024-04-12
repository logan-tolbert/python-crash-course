def make_sandwich(*ingredients):
    print("\nRequested ingredients:")
    for item in ingredients:
        print(f"-{item}")

make_sandwich('cheese', 'turkey', 'lettuce')
make_sandwich('cheese', 'ham', 'lettuce', 'tomato')
make_sandwich('cheese', 'roast beef', 'mustard')
