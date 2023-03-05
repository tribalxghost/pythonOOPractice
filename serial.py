"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start):
        """User decides starting point"""
        self.start = start
        self.step = 0
        self.res = start
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"


    def generate(self):
        """Generate serial number"""
        
        for count in range(1):
            self.start += self.step
            if(self.step == 1):
                self.step = 1
            else:
                self.step += 1
            return self.start
    
    def reset(self):
        """Resets serial number to first serial number generated."""
        self.start = self.res
        self.step = 0
      