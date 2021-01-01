# EISCP Micropython #

[![PyPI](https://img.shields.io/pypi/v/eiscp-micropython)](https://pypi.org/project/eiscp-micropython/)

This is an implementation of the Onkyo EISCP protocol for running on Microcontrollers utilizing [MicroPython](http://www.micropython.org/).

It is a heavily stripped down version of the [Onkyo EISCP](https://github.com/miracle2k/onkyo-eiscp) library and supports
sending commands to connected devices in the same IP-Network.

Compared to the original library, this one is also utilizing [uasyncio](https://docs.micropython.org/en/latest/library/uasyncio.html) for being able to run the project easily with other code.


## Usage ##

As an example turning on the first device in the network and changing the audio input.

```python
import uasyncio
import machine
from eiscp import discover

wifi = machine.WLAN(machine.)

loop = uasyncio.get_event_loop()

clients = loop.run_until_complete(discover())

client = clients[0]

loop.run_until_complete(client.power_on())
loop.run_until_complete(client.command("SLI", "11"))
```


## Testing ##

The EISCP library has been real world tested with an ESP32 microcontroller inside of the [ESP32 IR Remote Protocol](https://github.com/cbrand/esp32-ir-remote).

It communicates successfully to a [SX-S30DAB](https://intl.pioneer-audiovisual.com/products/2ch_components/sx-s30dab/).


## License ##

The project has been published via the MIT license.
