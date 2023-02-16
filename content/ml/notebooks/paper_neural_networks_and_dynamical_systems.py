import jax
import jax.numpy as jnp
import jax.random as random
import matplotlib.pyplot as plt
from jax import jit, tree_map, value_and_grad
from jax.lax import scan


def simulate_model(Y, R):
    """
    Y = [y_{k-2}, y_{k-2}]
    R = [r_{k-2}, r_{k-1}, r_k, ...]
    """
    Y = [Y[0], Y[1]]
    for r in R:
        y_next = 0.6*Y[-1] + 0.2*Y[-2] + r
        Y.append(y_next)

    return jnp.stack(Y)


def simulate_model_optimized(Y, R):
    """
    Y = [y_{k-2}, y_{k-2}]
    R = [r_{k-2}, r_{k-1}, r_k, ...]
    """
    def f(Y, r):
        y_next = 0.6*Y[1] + 0.2*Y[0] + r
        return jnp.array([Y[1], y_next]), y_next

    _, ys = scan(f, Y, R)

    return jnp.concatenate([Y, ys])


def simulate_plant_no_control(Y, R):

    Y = [Y[0], Y[1]]

    for r in R:
        y_next = Y[-1]*Y[-2]*(Y[-1]+2.5) / (1.0+Y[-1]**2+Y[-2]**2) + r
        Y.append(y_next)

    return jnp.stack(Y)


def simulate_plant_no_control_optimized(Y, R):
    """
    Y_p(k) = y_p(k-1)*y_p(k-2)*(y_p(k-1)+2.5)) / ( 1 + y_p^2(k-1) + y_p^2(k-2)) + r(k)
    Y = [y_{k-2}, y_{k-2}]
    R = [r_{k-2}, r_{k-1}, r_k, ...]
    """

    # while it is not clearly stated in the paper, setting u(k) = r(k)
    # seems to produce a plot that matches theirs. It seems that
    # "without control" is really means control IS reference input
    def f(Y, r):
        y_next = Y[1]*Y[0]*(Y[1]+2.5) / (1.0+Y[1]**2+Y[0]**2) + r
        return jnp.array([Y[1], y_next]), y_next

    _, ys = scan(f, Y, R)

    return jnp.concatenate([Y, ys])


def init_mlp_params(layer_widths, key):
    params = []
    for n_in, n_out in zip(layer_widths[:-1], layer_widths[1:]):
        params.append(
            {
                "weights": random.normal(key, (n_in, n_out)) * jnp.sqrt(2/n_in),
                "biases": jnp.zeros(shape=(n_out,))
            }
        )
    return params


def forward(x, params):
    *hidden, last = params
    for layer in hidden:
        x = jax.nn.relu(x @ layer['weights'] + layer['biases'])
    return (x @ last['weights'] + last['biases'])


def simulate_plant_control_optimized(Y, U, R, params):
    """
    Y_p(k) = y_p(k-1)*y_p(k-2)*(y_p(k-1)+2.5)) / ( 1 + y_p^2(k-1) + y_p^2(k-2)) + u(k)
    Y = [y_{k-2}, y_{k-2}]
    U = [u_{k-1}]
    R = [r_{k-2}, r_{k-1}, r_k, ...]
    """
    

    def f(YU, r):
        Y, U = YU
        Nc = forward(jnp.concatenate([Y,U]).T, params)
        u_new = Nc+r
        y_new = Y[1]*Y[0]*(Y[1]+2.5) / (1.0+Y[1]**2+Y[0]**2) + u_new

        return (jnp.concatenate([Y[1:], y_new]), u_new), y_new.reshape(-1)

    _, ys = scan(f, (Y,U), R)

    return jnp.concatenate([Y, ys])


def update(Y, U, R, Ym, params):

    lr = 0.000001

    def loss(params):
        Yp = simulate_plant_control_optimized(Y, U, R, params)
        return jnp.linalg.norm(Yp - Ym)

    loss, grads = value_and_grad(loss)(params)

    params = tree_map(lambda p, g: p - lr * g, params, grads)
    return loss, params


def run():
    key = random.PRNGKey(0)

    params = init_mlp_params([3,64,64,1],key)

    Y = jnp.array([[0.0], [0.0]])
    U = jnp.array(0.0).reshape(-1,1)
    k = jnp.arange(101)
    R = jnp.sin(2*jnp.pi*k/25).reshape(-1,1)
    Ym = simulate_model(Y, R)
    Ym_optimized = simulate_model_optimized(Y, R)
    Yp = simulate_plant_no_control(Y, R)
    Yp_optimized = simulate_plant_no_control_optimized(Y, R)
    

    update_jit = jit(update)
    from tqdm import tqdm
    losses = []
    for i in tqdm(range(100000)):
      loss, params = update_jit(Y,U,R,Ym,params)
      losses.append(loss)

    Yp_controlled_optimized = simulate_plant_control_optimized(Y,U,R, params)

    plt.plot(Ym, label="$Y_m(k)$", linestyle="dotted")
    plt.plot(Ym_optimized, label="$Y_m(k) [fast]$")
    plt.plot(Yp, label="$Y_p(k)$", linestyle="dotted")
    plt.plot(Yp_optimized, label="$Y_p(k) [fast]$")
    plt.plot(Yp_controlled_optimized, label="$Y_p(k) [controlled + fast]$")

    plt.legend()
    plt.show()

    plt.semilogy(losses)
    plt.show()


if __name__ == "__main__":
    run()
