# False Binocular Rivalry Project (not completed yet)
   This is our repository of our FalseBinocularRivalry project. The binocular rivalry is one of the most often used phenomenon in cognitive neuroscience to observe conscious perception. Binocular rivalry is the phenomenon where visual perception of images alternates subjects are asked to see one visual image to the right eye and another image to the left eye. In our project, we sought to find its phenomenological characteristics by accessing to introspection of subjects with multiple phenomenological interview methods. We contrasted introspective reports of the subjects during binocular rivalry stimuli with reports with false stimuli.

![FBR](FBR.gif#style=centerme)

## Introduction

We referred to the binocular rivalry model by [Li et al., PNAS, 2018](http://www.pnas.org/content/114/30/E6192). We leveraged an attention model of binocular rivalry stimuli to emulate dynamics of binocular rivalry transistions. Our report sheds light on difference of the phenomenological reports between real and peusdo binocular rivalry stimuli.

## Prerequisite
- MATLAB codes available from [Li et al., 2018](http://www.pnas.org/content/114/30/E6192).

## Contents and Files
- A program for generatoring False Binocular Rivalry Stimuli:
```bash
/8stateRandomTransition_forExp201802/ImageSynthesisFromAttentionModel2017(Feb16thNishida).ipynb
```
- Time-series of binocular rivalry from the monocular-summation neurons in the attention model [Li et al., PNAS, 2018](http://www.pnas.org/content/114/30/E6192)
```bash
/8stateRandomTransition_forExp201802/summation_120sec.txt
```
- 5 sample movies generated from ImageSynthesisFromAttentionModel2017(Feb16thNishida).ipynb
```bash
/8stateRandomTransition_forExp201802/8state_trand_noise_1.mp4
/8stateRandomTransition_forExp201802/8state_trand_noise_2.mp4
/8stateRandomTransition_forExp201802/8state_trand_noise_3.mp4
/8stateRandomTransition_forExp201802/8state_trand_noise_4.mp4
/8stateRandomTransition_forExp201802/8state_trand_noise_5.mp4
```
- A program for the main experiment
```bash
RivalryExp/PseudoRivalryPilot.py
```
- Movies for the main experiment
```bash
/RivalryExp/src/8state_trand_noise_1.mp4
/RivalryExp/src/8state_trand_noise_2.mp4
/RivalryExp/src/8state_trand_noise_3.mp4
/RivalryExp/src/8state_trand_noise_4.mp4
/RivalryExp/src/8state_trand_noise_5.mp4
```

## Committed by
- Dr. Takuya Niikawa, Dr. Katsunori Miyahara, Dr. Hiro Taiyo Hamada, Dr. Satoshi Nishida.

# Acknowledgments
This work was partly supported by the grants from the Japan Society for the Promotion of Science (JSPS; KAKENHI 18K00032) to TN, KM, and SN, and from JSPS (KAKENHI 18K18141) to SN.

# Publication
- not yet

# References
- Li, HH., Rankin, J., Rinzel, J., Carrasco, M., and Heeger, DJ. (2017) Attention model of binocular rivalry. Proceedings of the National Academy of Sciences. 114(30), pp.6192-6201. doi: [https://doi.org/10.1073/pnas.1620475114](https://doi.org/10.1073/pnas.1620475114)
nmar
