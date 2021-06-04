# Chemistry

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
