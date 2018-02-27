# Winnipeg_Transit_API_Handler
A Python-based API handler for the Winnipeg Transit API. Currently it only finds stops near a geolocation and finds estimated bus times for a given stop number. The end goal is to make this a fully-fledged API handler that can access any features of the Winnipeg Transit API.

## Getting Started

### Prequisites
This code is written for Python 3, and makes use of the requests library. If you don't have requests installed in your Python 3 environment, it can be obtained via:
```
pip3 install requests
```

## Usage
To create a winnipeg_tranist object for usage in a Python project, you can place the file winnipeg_transit.py file into your project directory. A handler object can be initialized as such:
```
import winnipeg_transit

transit = winnipeg_transit.winnipeg_transit("API key here")
```
The class methods (such as get_stops() and get_times()) can then be called:
```
stops = transit.get_stops(lat,lon,dist)
times = transit.get_times(stop)
```

## Code of Conduct

Please read CODE_OF_CONDUCT.md for details on our code of conduct.

## Authors
* **Ryan M. Spies** - *Initial Work* - [spiesr](https://github.com/spiesr)

## License
This project is licensed under the MIT license. - See the LICENSE file for details.
