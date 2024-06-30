import cc1101
from pythonosc import osc_server, dispatcher

cc = cc1101.CC1101()

def osc_to_cc(area, cue):
    '''Converts from an area and cue number to the 433MHz code to send'''

    # Value calculated from signals captured from the Bilusocn controller
    value = 0x14B430

    value += cue
    value += area << 8

    return value

# OSC Message Handler
def osc_message_handler(address):
    '''Sends command from OSC command'''

    addr = address.split('/')

    # Exit if not /fire at the end
    if addr[-1] != 'fire':
        return

    # Output area and cue firing
    addr = [x for x in addr if x.isdigit()]
    print(f"Triggering area {addr[0]} cue {addr[1]}")

    # Calculate code to send
    cccommand = osc_to_cc(int(addr[0]), int(addr[1]))

    # Set frequency and send command
    freq = 433.92e6
    # cc.set_base_frequency_hertz(freq)
    # cc.transmit(cccommand.to_bytes(length=3))

    print(f"Transmitted 0x{cccommand:X} at {freq / 1000000}MHz")

# OSC Server Configuration
dispatcher = dispatcher.Dispatcher()
dispatcher.set_default_handler(osc_message_handler)

# Start OSC Server
server = osc_server.BlockingOSCUDPServer(("0.0.0.0", 53000), dispatcher)
print(f"Listening on {server.server_address}")
server.serve_forever()
