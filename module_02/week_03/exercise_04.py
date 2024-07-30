import numpy as np


def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'No'],
        ['Sunny', 'Hot', 'High', 'Strong', 'No'],
        ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
        ['Sunny', 'Mild', 'High', 'Weak', 'No'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']
    ]
    return np.array(data)


train_data = create_train_data()
# print(train_data)


def compute_prior_probability(train_data):
    y = train_data[:, -1]
    y_unique, counts = np.unique(y, return_counts=True)
    prior_probability = counts / len(y)
    return prior_probability


prior_probablity = compute_prior_probability(train_data)
# print("P( play tennis = No", prior_probablity[0])
# print("P( play tennis = Yes", prior_probablity[1])
# Question 14 => A


def compute_conditional_probability(train_data):
    x = train_data[:, :-1]
    y = train_data[:, -1]
    y_unique = np.unique(y)
    conditional_probability = []
    list_x_name = []

    for i in range(x.shape[1]):
        x_i = x[:, i]
        x_i_unique = np.unique(x_i)
        list_x_name.append(x_i_unique)
        cond_prob = np.zeros((len(y_unique), len(x_i_unique)))

        for j, y_val in enumerate(y_unique):
            y_idx = np.where(y == y_val)[0]
            x_i_y = x_i[y_idx]
            for k, x_val in enumerate(x_i_unique):
                cond_prob[j, k] = np.sum(x_i_y == x_val) / len(x_i_y)

        conditional_probability.append(cond_prob)

    return conditional_probability, list_x_name


conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
# print("x1 = ", list_x_name[0])
# print("x2 = ", list_x_name[1])
# print("x3 = ", list_x_name[2])
# print("x4 = ", list_x_name[3])
# Question 15 => B


def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)
    return prior_probability, conditional_probability, list_x_name


def get_index_from_value(value, value_list):
    return np.where(value_list == value)[0][0]


outlook = list_x_name[0]

i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)

# print(i1, i2, i3)
# Question 16 => C


x1 = get_index_from_value("Sunny", list_x_name[0])
# print("P(Outlook=Sunny | 'Play Tennis'=Yes) = ", np.round(
#     conditional_probability[0][1, x1], 2))
# Question 17 => D


# print("P(Outlook=Sunny | 'Play Tennis'=No) = ", np.round(conditional_probability
#                                                          [0][0, x1], 2))
# Question 18 => A


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x_indices = [get_index_from_value(X[i], list_x_name[i])
                 for i in range(len(X))]
    p0 = prior_probability[0]
    p1 = prior_probability[1]

    for i in range(len(X)):
        p0 *= conditional_probability[i][0, x_indices[i]]
        p1 *= conditional_probability[i][1, x_indices[i]]

    if p0 > p1:
        y_pred = 0  # No
    else:
        y_pred = 1  # Yes

    return y_pred


X = ['Sunny', 'Cool', 'High', 'Strong']
train_data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(
    train_data)
pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability)

if pred:
    print("Ad should go!")
else:
    print("Ad should not go!")

# Question 19 => A
