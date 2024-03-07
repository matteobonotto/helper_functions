from joblib import Parallel, delayed
from pathlib import Path


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