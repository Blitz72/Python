#!/usr/bin/python3

import random

x_init = 1000
a = 0.8
p_prev = 0.9
r_limit = 50
z_prev = x_init - random.randint(-r_limit, r_limit)
p = p_prev

x_vals = []
z_vals = []

def init(x_init, a):
    x_values = []
    z_values = []
    z_prev = x_init
    x_prev = x_init
    for x in range(10):
        x_values.append(round(x_prev, 2))
        x_prev *= a
        new_z = z_prev - random.randint(-r_limit, r_limit)
        z_values.append(round(new_z, 2))
        z_prev *= a
    return x_values, z_values

def kalman(x_vals, z_vals):
    pass

def predict(x_prev, p_prev):
    x_hat = a * x_prev
    p = a * p_prev * a
    return x_hat, p

def update(p, z_prev, x_prev):
    g = p / (p + random.randint(-r_limit, r_limit))
    z = z_prev - random.randint(-r_limit, r_limit)
    x_hat = x_prev + g * (z - x_prev)
    p = (1 - g) * p
    return z, x_hat, g, p


if __name__ == '__main__':
    x_vals, z_vals = init(x_init, a)
    print(x_vals)
    print(z_vals)
    
    # for x in range(10):
    #     x_hat, p = predict(x_prev, p_prev)
    #     z, x_prev, g, p_prev = update(p, z_prev, x_hat)
    #     print('x=', x_hat, 'z=', z, 'p=', p_prev, 'g=', g)
