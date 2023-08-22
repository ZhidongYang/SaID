python denoise_cmd.py \
         --save-prefix ./models/ \
         -a [path_to_noisy_micrographs] \
         -b [path_to_clean_micrographs] \
         --normalize \
         -c 640 \
         --arch unet \
         -o ./denoised_micrographs \
         --num-epochs 200 \
         -d 0,1 \
         --holdout 0.2 \
         -wgu 0.0 \
         -wgd 0.0 \
         -ret abinitMaxpool \
         --batch-size 32


python denoise_cmd.py \
        -o ./denoised_micrographs \
        -m ./pre_trained_models/model_epoch200.sav \
        -d 0,1 \
        --patch-size 512 \
        -ret abinitMaxpool \
        ./test_data/10052.mrc 
