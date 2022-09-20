import json

list1 = []
list2 = []


# User is prompted with the function input, if they enter data of type int their input is saved to a list.
def userinput(string):
    while True:
        try:
            list1.append(int(input(string)))
            break
        except ValueError:
            print("Enter an integer")


# Calculates the Shapley values from the function inputs. Results are saved to a list.
def calculate(worker_value, owner_worker_value, n_workers):
    list2.append(owner_worker_value / 2 + worker_value / 2)  # worker shapley
    list2.append(n_workers * (owner_worker_value - worker_value) / 2)  # owner shapley


# Formats and creates a json file containing the Shapley values.
def json1(w_shapley, o_shapley):
    x = ("Worker Shapley = " + str(w_shapley),
         "Owner Shapley = " + str(o_shapley))
    file = open("shapley.json", "w")
    file.write(json.dumps(x, indent=2))
    file.close()


userinput("How much can a worker make on their own?:")
userinput("How much can a worker make at a factory?:")
userinput("How many workers?:")

calculate(list1[0], list1[1], list1[2])

json1(list2[0], list2[1])
