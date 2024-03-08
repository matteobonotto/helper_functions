import os
import sys
import h5py
import numpy as np
import time


def write_h5(
        data : dict,
        filename: str,
        dtype : str = 'float64',
        compression : str = 'lzf',
        compression_opts : int = 1,
        chunk_1st_dim = None,
        verbose : bool = False,
        ):
    
    if os.path.isfile(filename):
         os.remove(filename)
    
    kwargs = {
        'dtype' : dtype,
        'compression' : compression, 
        }
    if compression == 'gzip':
            kwargs.update({'compression_opts' : compression_opts})

    t_start = time.time()
    with h5py.File(filename + '.h5', 'w') as hf:
        for key,item in data.items():
            if chunk_1st_dim is not None:
                if chunk_1st_dim == True:
                    chunks = True
                else:
                    chunks = [chunk_1st_dim]
                    chunks.extend(item.shape[1:])
                    chunks = tuple(chunks)
            else:
                chunks = None

            # print(chunks)
            if verbose:
                print('Processing key: {}, dims: {}, size: {:.2f}MB'.format(
                    key, 
                    item.shape,
                    sys.getsizeof(item)/1e+6))

            hf.create_dataset(
                key,
                data = item,
                shape = item.shape,
                chunks=chunks,
                **kwargs)
        if verbose:
            print(' -> DonE! Elapsed time: {:.3f}s, final size: {:.2f}MB'.format(
                time.time()-t_start,
                os.path.getsize(filename + '.h5')/1e+6))
    hf.close()

def read_h5_numpy(
        filename : str, 
        ):
    data = {}
    with h5py.File(filename, 'r') as hf:
        for key,item in hf.items():
            data.update({
                    key : item[()]
            })
    return data
                 
def hdf5_to_dict(h5_file):
    def read_hdf5_file(h5_file):
        for key,val in h5_file.items():
            if type(val) == h5py._hl.dataset.Dataset:
                d[key] = np.array(val)
            else:
                d[key] = read_hdf5_file(val)
        return d
    
    d = dict()
    return read_hdf5_file(h5_file)
























