# Evonic Fire API Client

## About

This package allows you to control and monitor an Evonic Fire, over a local WebSocket connection.  It has been tested 
with the Linnea, so other fires may or may not be compatible

## Installation

`pip install pyevonic`

## Usage

```py
import asyncio

from pyevonic import Evonic

ev = Evonic("192.168.1.190")

async def main():
    await ev.connect()
    await ev.listen(callback=log)

def log(e):
    print(e.__dict__)


if __name__ == "__main__":
    asyncio.run(main())
```

## Available Methods

### Connect to the WebSocket of an Evonic Fire.
```py
connect()
```

### Listen for events on the Evonic WebSocket.
```py
listen(callback=method)
```

### Disconnect from a WebSocket
```py
disconnect()
```

### Control the main lighting for the Evonic Fire.
```python
light_power(cmd) 
```
Valid `cmd` values: `on` `off` `toggle`

### Toggles the feature light of an Evonic Fire
```python
toggle_feature_light()
```

### Sets the brightness of each RGB strip
```python
set_light_brightness(rgb_id, brightness)
```
`rgb_id` values can be found in `Device.info.modules`

`brightness` must be an integer from `0` to `255`

### Sets the animation speed of each RGB strip
```python
set_animation_speed(rgb_id, speed)
```
`rgb_id` values can be found in `Device.info.modules`

`speed` must be an integer from `0` to `255`

### Sets the heater temperature on an Evonic Fire
```python
set_temperature(temp)
```
`temp` must be an integer between `50` and `90` for fahrenheit, and `10` and `33` for celsius

### Controls the Heater for the Evonic Fire.
```python
heater_power(cmd)
```
Valid `cmd` values: `on` `off` `toggle`