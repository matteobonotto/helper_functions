# from joblib import Parallel, delayed
from pathlib import Path
from time import time
import numpy as np

    # with utils.Timer() as gentime:
    #     rngs = np.random.randint(np.iinfo(np.int32).max, size=num_samples)
    #     fluid_field, velocity_corrected = zip(
    #         *Parallel(n_jobs=n_parallel)(delayed(genfunc)(idx, rngs[idx]) for idx in tqdm(range(num_samples)))
    #     )

def touch_dir(dir_path: str) -> None:
    """
    Create dir if not exist

    :param dir_path: directory path

    """
    Path(dir_path).mkdir(parents=True, exist_ok=True)



def timer_func(func):
    """
    Decorator to time function execution

    :param func: function to be timed
    :return: timed function

    """
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'{func.__name__}() executed in {(t2-t1):.6f}s')
        return result
    return wrapper


def linspace(
        start,
        stop,
        step=1.
):
    """
    Like np.linspace but uses step instead of num
    This is inclusive to stop, so if start=1, stop=3, step=0.5
    Output is: array([1., 1.5, 2., 2.5, 3.])
  """
    return np.linspace(start, stop, int((stop - start) / step + 1))




def get_params(
        dd,
        separator='___',
        prefix=''
):
    """
    Get params from nested dict

    :param dd: dict to be unrolled
    :param separator: separator to be used
    :param prefix: prefix to be used
    :return: unrolled dict

    """
    if isinstance(dd, dict):
        mapped_dd = {f'{prefix}{separator}{k}' if prefix else k: v for kk, vv in dd.items() for k, v in
                     get_params(vv, separator, kk).items()
                     }
        return mapped_dd
    else:
        return {
            prefix: dd
        }

