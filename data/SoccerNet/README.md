Since SoccerNet data is taking huge amount of memory, it was downloaded locally, using following github repo. 
All instructions how to download the data are contained there.

https://github.com/taxfromdk/soccernet-test

Repository has to be cloned, following packages has to be installed in the working environment:

```
conda create -n SoccerNet python pip
pip install SoccerNet
```

and ***soccer.py*** script will download the dataset.

The data may be visualised by unpacking zip files and selecting proper folder as an input to the function contained in tools folder, using the ***visualization.py*** script in __tools__ subfolder of this repository.
