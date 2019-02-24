from random import shuffle


def generate_prisoner(pick, assigned):
    return {'pick': pick, 'assigned': assigned}


def generate_prisoners(assigned_numbers):
    picked_nums = list(range(1, len(assigned_numbers) + 1))
    shuffle(picked_nums)
    zipped = zip(picked_nums, assigned_numbers)
    mapped = map(lambda p: generate_prisoner(p[0], p[1]), zipped)
    return list(mapped)


def get_prisoners_assigned_numbers(prisoners):
    return list(map(lambda p: p['assigned'], prisoners))


def calculate_guess(others, pick, verbose):
    guess = None
    total_sum = sum(others)
    prisoners_count = len(others) + 1
    for i in range(1, prisoners_count + 1):
        calc = (total_sum + i) % prisoners_count
        if verbose:
            print('{} + {} % {} == {}'.format(total_sum, i, prisoners_count, pick - 1))
        if calc == (pick - 1):
            guess = i
            break

    return guess


def prisoner_guess(other_prisoners, pick, verbose):
    numbers_in_view = get_prisoners_assigned_numbers(other_prisoners)
    return calculate_guess(numbers_in_view, pick, verbose)


def solve(assigned_numbers, verbose=False):
    answer = None
    if verbose:
        print(assigned_numbers)

    prisoners = generate_prisoners(assigned_numbers)

    for i, prisoner in enumerate(prisoners):
        if verbose:
            print('prisoner {} guess'.format(i))

        others = list(filter(lambda p: prisoner != p, prisoners))
        guess = prisoner_guess(others, prisoner['pick'], verbose)

        if guess == prisoner['assigned']:
            answer = prisoner
            break

    return answer
