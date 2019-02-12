from pymoku import *
from pymoku.instruments import SpectrumAnalyzer

# Connect to your Moku by its device name
# Alternatively, use Moku.get_by_serial('#####') or Moku('192.168.###.###')
m = Moku.get_by_serial('000307')

# Deploy the Spectrum Analyzer to your Moku
i = m.deploy_instrument(SpectrumAnalyzer)

try:
    # DC to 10MHz span
    i.set_span(0, 1e3)
  
    # Get the scan results and print them out (power vs frequency, two channels)
    data = i.get_data()
    print(dir(data))
    print(data._metadata)
    #print(data.ch1, data.ch2, data.frequency)

finally:
    # Close the connection to the Moku.
    m.close()
