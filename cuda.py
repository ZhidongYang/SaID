from __future__ import print_function, division

import warnings
import torch
import os

def _format(message, category, filename, lineno, line=None):
    w = '{}: {}\n'.format(category.__name__, message)
    return w
warnings.formatwarning = _format


class CudaWarning(UserWarning):
    pass


def set_device(device, error=False, warn=True):
    use_cuda = False
    # print(device)
    if int(device[0]) >= 0: # try to set GPU when device >= 0
        # device = int(device)
        os.environ["CUDA_VISIBLE_DEVICES"] = device
        use_cuda = torch.cuda.is_available()
        # try:
        #     torch.cuda.set_device(-2)
        # except Exception as e:
        #     ## setting the device failed
        #     if error:
        #         raise e
        #     if warn:
        #         # warn the user
        #         message = str(e) + '\nFalling back to CPU.'
        #         warnings.warn(message, CudaWarning)
        #     # fallback to CPU
        #     use_cuda = False
    return use_cuda
