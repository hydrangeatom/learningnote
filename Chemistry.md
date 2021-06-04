# Chemistry

### OpenBabel

[OpenBabel](http://openbabel.org/) is a open-source versatile chemical toolkit.

```
obabel -i smi -:"C1=CC=C(C=C1)C(=O)O" -O BenzoicAcid.xyz --gen3d
```

Create a 3d molecular structure from a SMILES string. 
It generates a reasonable 3d structure from molecular connectivity information. 
It also can generate multiple conformers.
You can find SMILES of a certain molecule on online databases like [PubChem](https://pubchem.ncbi.nlm.nih.gov/).
