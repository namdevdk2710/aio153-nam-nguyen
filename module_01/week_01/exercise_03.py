import math
import random

def regression_loss():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if num_samples.isnumeric() == False:
        print("number of samples must be an integer number")
        return
    
    loss_name = input("Input loss name (MSE|MAE|RMSE): ")
    if loss_name != 'MSE' and loss_name != 'MAE' and loss_name != 'RMSE':
        print(f"loss name {loss_name} is not supportted")
        return
    
    if loss_name == 'MSE':
        for i in range(int(num_samples)):
            pred = random.uniform(0, 10)
            target = random.uniform(0, 10)
            loss = (pred - target) ** 2
            print(f"loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")
    
    if loss_name == 'MAE':
        for i in range(int(num_samples)):
            pred = random.uniform(0, 10)
            target = random.uniform(0, 10)
            loss = abs(pred - target)
            print(f"loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")

    if loss_name == 'RMSE':
        for i in range(int(num_samples)):
            pred = random.uniform(0, 10)
            target = random.uniform(0, 10)
            loss = math.sqrt((pred - target) ** 2)
            print(f"loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")


regression_loss()
