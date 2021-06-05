# Chemistry

### xTB

[xTB](https://github.com/grimme-lab/xtb) is an open-source semi-empirical calculation package, primarily focusing on GFNn-xTB. For the theoretical background of the method, please refer to [this review](https://doi.org/10.1002/wcms.1493) (open-access). Besides single point calculation and geometry optimization, the application offers the capability of powerful metadynamics simulations and reaction path methods as well.

```
> xtb CO2.xyz --opt > CO2.out
normal termination of xtb
> cat xtbopt.xyz
3
 energy: -10.308452237208 gnorm: 0.000357524329 xtb: 6.4.0 (d4b70c2)
C         1.05140999996228   -0.07321999998829   -0.04467999999286
O        -0.09213262105570   -0.07322000000585   -0.04468000000357
O         2.19495262109342   -0.07322000000585   -0.04468000000357
```

With `--opt` xTB will yield a carbon monoxide molecule with an optimized structure. The detailed log can be found in CO.out and final structure in xtbopt.xyz.


### OpenBabel

[OpenBabel](http://openbabel.org/) is a open-source versatile chemical toolkit.

```
obabel H2O.xyz -O H2O.cml 
```

Convert a chemical file with a specific format into the one with another.
The app supports various sorts of file formats.


```
obabel -i smi -:"C1=CC=C(C=C1)C(=O)O" -O BenzoicAcid.xyz --gen3d
```

Create a 3d molecular structure from a SMILES string. 
It generates a reasonable 3d structure from molecular connectivity information. 
It also can generate multiple conformers.
You can find SMILES of a certain molecule on online databases like [PubChem](https://pubchem.ncbi.nlm.nih.gov/).
