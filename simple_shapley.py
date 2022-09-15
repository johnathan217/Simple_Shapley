import json


def main():
    # Asks user to state a value for worker_value, repeats until user provides an input of data type int
    # The worker value is how much a worker can produce on their own
    while True:
        try:
            worker_value = int(input("How much can a worker make on their own?:"))
        except ValueError:
            print("Enter an integer")
        else:
            break

    # Asks user to state a value for owner_worker_value, repeats until user provides an input of data type int
    # owner_worker_value is how much a worker can make combined with a factory owner

    while True:
        try:
            owner_worker_value = int(input("How much can a worker make at a factory?:"))
        except ValueError:
            print("Enter an integer")
        else:
            break

    # Asks user to state a value for n_workers, repeats until user provides an input of data type int
    # n_workers is the number of workers. 1 factory owner is assumed in all cases.

    while True:
        try:
            n_workers = int(input("How many workers?:"))
        except ValueError:
            print("Enter an integer")
        else:
            break

    # Runs the calculation.
    worker_shapley = owner_worker_value / 2 + worker_value / 2

    owner_shapley = n_workers * (owner_worker_value - worker_value) / 2

    # Formats the output of the calculation.
    x = (
        "Worker Shapley = " + str(worker_shapley),
        "Owner Shapley = " + str(owner_shapley)
    )

    # Writes a json file, and adds the calculation output to it.
    file = open("shapley.json", "w")
    file.write(json.dumps(x, indent=2))
    file.close()


main()
