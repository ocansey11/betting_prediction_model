@echo off
set TESSDATA_PREFIX=C:\Program Files\Tesseract-OCR\tessdata
set GROUND_TRUTH_DIR=data\eng\betway-ground-truth
set OUTPUT_DIR=data\eng\output

mkdir %OUTPUT_DIR%

for %%f in (%GROUND_TRUTH_DIR%\*.png) do (
    tesseract %%f %OUTPUT_DIR%\%%~nf --psm 6 lstm.train
)

lstmtraining --continue_from %TESSDATA_PREFIX%\eng.lstm \
             --model_output %OUTPUT_DIR%\my_model \
             --traineddata %TESSDATA_PREFIX%\eng.traineddata \
             --train_listfile %OUTPUT_DIR%\train.list \
             --max_iterations 10000
