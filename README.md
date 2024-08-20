# ioptron-python

This code is used to communicate with the SkyHunter AltAz mount. 

## Modifications
This code was forked from [ioprton-python](https://github.com/chimerasaurus/ioptron-python) and the list of modifications is presented below:
 * Modifying the $PYTHONPATH env variable is not needed anymore. The path structure is handled by `os`.
 * Debug of the initialization of the `Parking`  class.
 * Warning messages about the mount park state.
 * Added SkyHunter to the list of mount versions, see `mount_values.yaml`
 * A new demo notebook.

## Citations and sources

This project has used parts of other OSS projects, or has implemented ideas shown in them, including: 

* [ioprton-python](https://github.com/chimerasaurus/ioptron-python) 
* [python-lx200](https://github.com/telescopio-montemayor/python-lx200)
* [onstep-python](https://github.com/kbahey/onstep-python)

This project uses the following open specifications:

* [iOptron® Mount RS-232 Command Language](https://www.ioptron.com/v/ASCOM/RS-232_Command_Language2014V310.pdf)
