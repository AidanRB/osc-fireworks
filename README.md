# osc-fireworks

This script is to bridge the gap between [QLab](https://qlab.app/) and fireworks using OSC and a [CC1101](https://www.ti.com/product/CC1101) connected to a Raspberry Pi.

- Works with a random [Bilusocn](https://www.bilusocn.com/) controller [from Amazon](https://www.amazon.com/dp/B0CR72CJXQ/).
- Only accepts commands ending in `/fire`.
- Uses the first two segments of the command that are integers as the firework controller area and cue number.  
  Example: Sending `/pyro/area/5/cue/3/fire` will fire area 5, cue 3. So will sending `/5/3/fire`.
- **Note**: Cue 14 is the All Fire button. 15 is the Rapid button. Use with caution.
- Wiring for the CC1101 is [default](https://pypi.org/project/cc1101/) based on the library I used.
